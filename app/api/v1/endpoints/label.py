from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api import deps
from app.crud.label import label
from app.schemas.label import Label, LabelCreate, LabelUpdate

router = APIRouter()


@router.get("/", response_model=List[Label])
async def get_labels(
    session: AsyncSession = Depends(deps.get_session), skip: int = 0, limit: int = 10
) -> Any:
    """
    Retrieve labels
    """

    labels = await label.get_many(session, skip=skip, limit=limit)
    return labels


@router.post("/", response_model=Label, status_code=201)
async def create_label(
    *, session: AsyncSession = Depends(deps.get_session), label_in: LabelCreate
) -> Any:
    """
    Create new label
    """

    result = await label.create(session, create_obj=label_in)
    return result


@router.put("/{id}", response_model=Label, status_code=200)
async def update_label(
    *, session: AsyncSession = Depends(deps.get_session), id: int, label_in: LabelUpdate
) -> Any:
    """
    Update label
    """
    this_label = await label.get(session, id=id)
    if not this_label:
        raise HTTPException(status_code=404, detail="Resource not found")
    result = await label.update(session, db_obj=this_label, update_obj=label_in)
    return result
