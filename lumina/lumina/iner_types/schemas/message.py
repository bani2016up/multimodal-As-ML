from .metadata import MessageMetadata
from pydantic import BaseModel


class Message(BaseModel):
    content: str
    metadata: MessageMetadata
