from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import PromotionOut, PromotionCreate, PromotionUpdate
from app.api import db_manager

promotion = APIRouter()


@promotion.post('/', response_model=PromotionOut, status_code=201)
async def create_promotion(payload: PromotionCreate):
    promotion_id = await db_manager.add_promotion(payload)
    response = {
        'promotion_id': promotion_id,
        **payload.dict()
    }
    return response


@promotion.get('/', response_model=List[PromotionOut])
async def get_promotions():
    return await db_manager.get_all_promotions()


@promotion.get('/{id}/', response_model=PromotionOut)
async def get_promotion(id: int):
    promotion = await db_manager.get_promotion(id)
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion


@promotion.put('/{id}/', response_model=PromotionOut)
async def update_promotion(id: int, payload: PromotionUpdate):
    promotion = await db_manager.get_promotion(id)
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")

    update_data = payload.dict(exclude_unset=True)
    return await db_manager.update_promotion(id, update_data)


@promotion.delete('/{id}/', response_model=None)
async def delete_promotion(id: int):
    promotion = await db_manager.get_promotion(id)
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return await db_manager.delete_promotion(id)
