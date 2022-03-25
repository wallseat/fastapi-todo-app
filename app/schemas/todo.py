from datetime import datetime
from typing import Optional

from pydantic import BaseModel, constr


class BaseTodo(BaseModel):
    text: constr(max_length=4096)  # type: ignore

    created_at: datetime
    expires_at: Optional[datetime]


class TodoCreate(BaseTodo):
    pass


class TodoUpdate(BaseTodo):
    pass


class Todo(BaseTodo):
    id: int

    class Config:
        orm_mode = True


class TodoLabelsBase(BaseModel):
    todo_id: int
    label_id: int


class TodoLabelsCreate(TodoLabelsBase):
    pass


class TodoLabelsUpdate(TodoLabelsBase):
    pass


class TodoLabels(TodoLabelsBase):
    id: int

    class Config:
        orm_mode = True
