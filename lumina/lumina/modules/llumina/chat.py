from collections.abc import Generator
import json
import os
from database import DocumentStore
from chat_models.llama import LlamaChatModel
import path
import utils


class LuminaChat:

    def __init__(self, store: DocumentStore):
        self.ds = store
        self.model = LlamaChatModel(
            n_threads=os.cpu_count() or 1, n_ctx_size=8192, max_tokens=4048
        )

    def load_context(self) -> None:
        with open(path.start, "r") as f:
            start_prompt = f.read()
            history_prompt = ""  # TODO: Load previous context from the database
            self.model.generate(start_prompt + history_prompt)

    def ask(self, user_input: str, commands_response: list[str] | None = None) -> Generator[str, None, None]:
        _metadata = utils.metadata()
        yield from self.model.ask(self._get_prompt(_metadata, user_input, commands_response))

    @staticmethod
    def _get_prompt(
        _metadata, _user_input, commands_response: list[str] | None = None
    ) -> str:
        if commands_response is None:
            commands_response = []
        print(
            json.dumps(
            {
                "commands_response": commands_response,
                "user_input": _user_input,
                "metadata": _metadata,
            }
        )
        )
        return json.dumps(
            {
                "commands_response": commands_response,
                "user_input": _user_input,
                "metadata": _metadata,
            }
        )
