from fastapi import APIRouter, Depends, Request, Query
from fastapi.responses import JSONResponse
from sqlalchemy import select, insert, func
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Union

from database import get_async_session
from operations.models import application
from operations.schemas import ApplicationCreate


router = APIRouter(
    prefix="/operations",
    tags=["Operation"]
)

@router.get("/application")
async def get_specific_operations(
    page: int = 1,
    object: Union[str, None] = None,
    price: Union[int, None] = None,
    hour: Union[float, None] = None,
    session: AsyncSession = Depends(get_async_session)
):
    try:
        query = select(application)

        if object:
            query = query.where(application.c.object == object)
        if price:
            query = query.where(application.c.price == price)
        if hour:
            query = query.where(application.c.hour == hour)

        query = query.offset((page - 1) * 10).limit(10)
        result = await session.execute(query)
        items = result.mappings().all()
    
        count_query = select(func.count()).select_from(application)
        
        if object:
            count_query = count_query.where(application.c.object == object)
        if price:
            count_query = count_query.where(application.c.price == price)
        if hour:
            count_query = count_query.where(application.c.hour == hour)

        
        count_result = await session.execute(count_query)
        total_items = count_result.scalar()
    
        return {
            "items": list(items),
            "totalItems": total_items
        }
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})

@router.post("/filter_data")
async def get_filter_data(request: Request, session: AsyncSession = Depends(get_async_session)):
    # if not request:
    #     print("Пусто")
    #     return False
    
    data = await request.json()
    print(data.get("searchObject"))
    query = select(application).where(application.c.object == data.get("searchObject"))
    print(query)
    result = await session.execute(query)

    return result.mappings().all()