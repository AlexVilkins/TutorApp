from fastapi import APIRouter, Depends
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_async_session
from operations.models import application
from operations.schemas import ApplicationCreate

router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)


@router.get("/application")
async def get_specific_operations(session: AsyncSession = Depends(get_async_session)):
    query = select(application)
    result = await session.execute(query)
    return result.mappings().all()