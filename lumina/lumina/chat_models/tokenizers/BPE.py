from .tokenizer import Tokenizer
from transformers import LlamaTokenizer


class BPETokenizer(Tokenizer):

    @staticmethod
    def tokenize(model: str, text: str) -> str:
        return LlamaTokenizer.from_pretrained(model).tokenizer.encode(text)
