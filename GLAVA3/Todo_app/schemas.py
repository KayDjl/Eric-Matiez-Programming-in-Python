from typing import Optional
from pydantic import BaseModel

class TodoItemCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TodoItemUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

class TodoItemResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool

    class Config:
        orm_mode = True