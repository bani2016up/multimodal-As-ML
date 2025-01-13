from abc import ABC, abstractmethod
from typing import Generator


class ChatModel(ABC):

    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def ask(self, user_input: str) -> Generator[str, None, None]:
        pass

    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass

    @abstractmethod
    def load_context(self, init_prompt: str = "", history: str = "") -> None:
        pass
