
from abc import ABC, abstractmethod

class Tokenizer(ABC):

    @abstractmethod
    @staticmethod
    def tokenize(model: str, text: str) -> str:
        pass
