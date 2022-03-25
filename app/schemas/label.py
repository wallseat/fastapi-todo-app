from typing import Optional

from pydantic import BaseModel, constr


class LabelBase(BaseModel):
    name: constr(max_length=32)  # type: ignore
    color: Optional[constr(max_length=7)]  # type: ignore


class LabelCreate(LabelBase):
    pass


class LabelUpdate(LabelBase):
    pass


class Label(LabelBase):
    id: int
    color: constr(max_length=7)  # type: ignore

    class Config:
        orm_mode = True
