from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, db: AsyncSession, id: Any) -> Optional[ModelType]:
        stmt = select(self.model).where(self.model.id == id)  # type: ignore
        result = await db.execute(stmt)

        return result.scalars().first()

    async def get_many(
        self, session: AsyncSession, *, skip: int = 0, limit: int = 10
    ) -> List[ModelType]:
        if skip and limit:
            stmt = select(self.model).offset(skip).limit(limit)
        elif limit:
            stmt = select(self.model).offset(0).limit(limit)
        else:
            stmt = select(self.model)

        result = await session.execute(stmt.order_by("id"))
        return result.scalars().all()

    async def create(
        self, session: AsyncSession, *, create_obj: CreateSchemaType
    ) -> ModelType:
        encoded_object_in = jsonable_encoder(create_obj)
        db_obj = self.model(**encoded_object_in)

        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)

        return db_obj

    async def update(
        self,
        session: AsyncSession,
        *,
        db_obj: ModelType,
        update_obj: Union[UpdateSchemaType, Dict[str, Any]]
    ) -> ModelType:
        encoded_db_obj = jsonable_encoder(db_obj)

        if isinstance(update_obj, dict):
            update_data = update_obj
        else:
            update_data = update_obj.dict(exclude_unset=True)

        for field in encoded_db_obj:
            if field in update_data:
                setattr(db_obj, field, update_data[field])

        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)

        return db_obj
