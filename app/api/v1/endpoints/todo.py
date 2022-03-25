from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.crud.todo import todo, todo_labels
from app.schemas.todo import Todo, TodoCreate, TodoLabelsCreate, TodoUpdate

router = APIRouter()


@router.get("/", response_model=List[Todo])
async def get_todos(
    session: AsyncSession = Depends(deps.get_session), skip: int = 0, limit: int = 10
) -> Any:
    """
    Retrieve todo's
    """

    todos = await todo.get_many(session, skip=skip, limit=limit)
    return todos


@router.post("/", response_model=Todo, status_code=201)
async def create_todo(
    *,
    session: AsyncSession = Depends(deps.get_session),
    todo_in: TodoCreate,
    labels_ids: Optional[List[int]] = None
) -> Any:
    """
    Create new todo and assigns labels to it
    """

    result = await todo.create(session, create_obj=todo_in)

    if labels_ids:
        for label_id in labels_ids:
            await todo_labels.create(
                session,
                create_obj=TodoLabelsCreate(todo_id=result.id, label_id=label_id),
            )

    return result


@router.put("/{id}", response_model=Todo, status_code=200)
async def update_todo(
    *,
    session: AsyncSession = Depends(deps.get_session),
    id: int,
    todo_in: TodoUpdate,
    labels_ids: Optional[List[int]] = None
) -> Any:
    """
    Update todo
    """
    this_todo = await todo.get(session, id=id)
    if not this_todo:
        raise HTTPException(status_code=404, detail="Resource not found")
    result = await todo.update(session, db_obj=this_todo, update_obj=todo_in)

    if labels_ids:
        for label_id in labels_ids:
            await todo_labels.create(
                session,
                create_obj=TodoLabelsCreate(todo_id=result.id, label_id=label_id),
            )

    return result


@router.delete("/{id}", response_model=Todo, status_code=200)
async def remove_labels_from_todo(
    *, session: AsyncSession = Depends(deps.get_session), id: int, labels_ids: List[int]
) -> Any:
    """
    Remove labels from todo
    """
    this_todo = await todo.get(session, id=id)
    if not this_todo:
        raise HTTPException(status_code=404, detail="Resource not found")

    await todo_labels.delete_by_todo_id(session, todo_id=id, labels_ids=labels_ids)

    return this_todo
