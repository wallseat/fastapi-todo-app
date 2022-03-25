from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base

metadata = MetaData()

Base = declarative_base(metadata=metadata)

from .label import Label
from .todo import Todo, TodoLabels

__all__ = ["metadata", "Todo", "Label", "TodoLabels"]
