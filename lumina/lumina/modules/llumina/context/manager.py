from chat_models.tokenizers import BPETokenizer

class LuminaContextManager:

    def __init__(self, model: str, max_context_size: int) -> None:
        self.__model = model
        self.__len = 0
        self.__max__len = max_context_size

    def evaluate_size(self,item: str) -> int:
        return len(BPETokenizer.tokenize(self.__model, item))

    def add_item(self, item: str) -> None:
        tokenized_item_size = self.evaluate_size(item)
        if self.__len + tokenized_item_size > self.__max__len:
            return

        self.__len += tokenized_item_size
        self.store_item(item)
