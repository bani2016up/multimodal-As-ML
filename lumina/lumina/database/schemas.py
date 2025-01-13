from typing import Optional
from iner_types import Message, TimeLocMetadata
from pydantic import BaseModel


class MessageResult(Message):
    _id: str

class MessagesQueryResult(BaseModel):
    results: list[MessageResult]
    metadata: Optional[TimeLocMetadata] = TimeLocMetadata()
