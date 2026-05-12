from pydantic import BaseModel, Field
from typing import Union

class Todo(BaseModel):
    title: str = Field(...)
    desc: str  = Field(...)
    isComplete: Union[bool, None] = False


# Field = to make required
# Union = like enum in node, means any type Union[bool, None] = false(default)