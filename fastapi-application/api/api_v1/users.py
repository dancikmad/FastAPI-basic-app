from typing import Annotated
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db_helper, User
from core.schemas.user import UserRead, UserCreate
from .crud.users import get_all_users, create_user

router = APIRouter(tags=['Users'])

@router.get("")
async def get_users(
    # session: AsyncSession = Depends(db_helper.session_getter)
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)]
) -> list[UserRead]:
    users = await get_all_users(session=session)
    return users


@router.post("")
async def add_user(
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter)
    ],
    user_create: UserCreate
) -> UserRead:
    user = await create_user(
        session=session,
        user_create=user_create
    )
    return user