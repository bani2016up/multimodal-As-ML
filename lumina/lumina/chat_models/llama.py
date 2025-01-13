

from collections.abc import Generator
from gpt4all import GPT4All
from .model_abc import ChatModel


class LlamaChatModel(ChatModel):

    def __init__(self, n_threads: int, n_ctx_size: int, max_tokens: int) -> None:
        self._n_threads = n_threads
        self._n_ctx_size = n_ctx_size
        self._max_tokens = max_tokens

        self.model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf", n_threads=self._n_threads, n_ctx=self._n_ctx_size)

    def load_context(self, init_prompt: str = "", history: str = "") -> None:
        self.model.generate(init_prompt + history)

    def ask(self, user_input: str) -> Generator[str, None, None]:
        yield from self.model.generate(user_input, streaming=True, max_tokens=self._max_tokens)

    def generate(self, prompt: str) -> str:
        return self.model.generate(prompt, max_tokens=self._max_tokens)
