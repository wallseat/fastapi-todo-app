from sqlalchemy import Column, DateTime, Integer, Sequence, String, Table

from . import Base


class Label(Base):
    __tablename__ = "label"

    id = Column(
        Integer, Sequence("label_id_seq", metadata=Base.metadata), primary_key=True
    )
    name = Column(String(32), nullable=False)
    color = Column(String(7), default="#FFFFFF")
