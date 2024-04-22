from .llm import OpenAILLM
from .tools.all_tools import tools


class CPU:
    def __init__(self):
        self.llm = OpenAILLM(
            system_message="You are the cpu for an LLM OS. LLM OS is an operating system that is run by you, think of yourself as the brain of the operating system.",
            tools=tools,
        )

    def chat(self, prompt: str):
        return self.llm.chat(prompt)

    def streaming_chat(self, prompt: str):
        return self.llm.streaming_chat(prompt)
