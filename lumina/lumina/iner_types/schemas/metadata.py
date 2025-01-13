from typing import Optional
from cfg import my_names, model_names
from pydantic import BaseModel, field_validator
from utils import current_location, current_timestamp


class AuthorMetadata(BaseModel):
    author: str

    @field_validator("author")
    def validate_author(cls, value: str) -> str:
        names = my_names + model_names
        if value not in names:
            raise ValueError(f"Modal name  should be in {names}")
        return value

class TimeLocMetadata(BaseModel):
    timestamp: Optional[str] = current_timestamp()
    location: Optional[str] = current_location()

class MessageMetadata(TimeLocMetadata, AuthorMetadata):
    ...
