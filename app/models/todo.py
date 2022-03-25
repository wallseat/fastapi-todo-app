from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Sequence, String

from . import Base


class Todo(Base):
    __tablename__ = "todo"

    id = Column(
        Integer, Sequence("todo_id_seq", metadata=Base.metadata), primary_key=True
    )
    text = Column(String(4096))
    is_complete = Column(Boolean, default=False, nullable=False)

    created_at = Column(String(96))
    expires_at = Column(String(96))


class TodoLabels(Base):
    __tablename__ = "todo_labels"

    id = Column(
        Integer,
        Sequence("todo_labels_id_seq", metadata=Base.metadata),
        primary_key=True,
    )

    todo_id = Column(Integer, ForeignKey("todo.id"), nullable=False)
    label_id = Column(Integer, ForeignKey("label.id"), nullable=False)
