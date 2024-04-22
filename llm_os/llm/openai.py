from openai import OpenAI
from .base import BaseLLM
from pydantic import BaseModel
from typing import Literal, List

from ..settings import settings


class Message(BaseModel):
    role: Literal["user", "assistant", "system"]
    content: str


class OpenAILLM(BaseLLM):
    def __init__(self, system_message: str):
        super().__init__()

        self.client = OpenAI()
        self.conversation_history: List[Message] = []

        self.system_message = system_message
        self._add_system_message(system_message)

    def _add_user_message(self, message: str):
        self.conversation_history.append(Message(role="user", content=message))

    def _add_assistant_message(self, message: str):
        self.conversation_history.append(Message(role="assistant", content=message))

    def _add_system_message(self, message: str):
        self.conversation_history.append(Message(role="system", content=message))

    def _format_messages(self):
        messages = []
        for message in self.conversation_history:
            messages.append({"role": message.role, "content": message.content})
        return messages

    def chat(self, prompt: str, **kwargs):
        self._add_user_message(prompt)

        response = self.client.chat.completions.create(
            model=settings.OPENAI_MODEL_NAME,
            messages=self._format_messages(),
            functions=kwargs.get("functions", None),
        )

        response_message = response.choices[0].message["content"]  # type: ignore
        self._add_assistant_message(response_message)

        return response_message

    def streaming_chat(self, prompt: str, **kwargs):
        self._add_user_message(prompt)

        response = self.client.chat.completions.create(
            model=settings.OPENAI_MODEL_NAME,
            messages=self._format_messages(),
            functions=kwargs.get("functions", None),
            stream=True,
        )

        response_message = ""
        for chunk in response:
            character = chunk.choices[0].delta.content or ""
            print(character, end="", flush=True)
            response_message += character

        self._add_assistant_message(response_message)

        return response_message
