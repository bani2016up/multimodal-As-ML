from .schemas.message import Message
from .schemas.metadata import MessageMetadata, TimeLocMetadata




def NewMessage(msg: str, author: str, **kwargs) -> Message:
    return Message(content=msg, metadata=MessageMetadata(author=author, **kwargs))


__all__ = ["Message", "MessageMetadata", "TimeLocMetadata", "NewMessage"]
