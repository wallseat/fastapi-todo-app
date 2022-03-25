from typing import List

from sqlalchemy import and_, delete
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Todo, TodoLabels
from app.schemas.todo import TodoCreate, TodoLabelsCreate, TodoLabelsUpdate, TodoUpdate

from .base import CRUDBase


class CRUDTodo(CRUDBase[Todo, TodoCreate, TodoUpdate]):
    pass


todo = CRUDTodo(Todo)


class CRUDTodoLabels(CRUDBase[TodoLabels, TodoLabelsCreate, TodoLabelsUpdate]):
    async def delete_by_todo_id(
        self, session: AsyncSession, *, todo_id: int, labels_ids: List[int]
    ):
        stmt = delete(self.model).where(
            and_(self.model.todo_id == todo_id, self.model.label_id.in_(labels_ids))
        )
        await session.execute(stmt)
        await session.commit()


todo_labels = CRUDTodoLabels(TodoLabels)
