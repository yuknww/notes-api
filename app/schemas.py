from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class NoteBase(BaseModel):
    id: int
    title: str = Field(
        ...,
        min_length=1,
        max_length=100,
    )
    content: str
    done: bool = False


class NoteCreate(NoteBase):
    pass


class NoteUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    done: Optional[bool] = None


class NoteResponse(BaseModel):
    id: int

    model_config = ConfigDict(from_attributes=True)
