from abc import ABC, abstractmethod


class BaseLLM(ABC):
    @abstractmethod
    def chat(self, prompt: str, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def streaming_chat(self, prompt: str, **kwargs):
        raise NotImplementedError
