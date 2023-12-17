from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import PromotionOut, PromotionIn, PromotionUpdate
from app.api import db_manager

promotions = APIRouter()


@promotions.post('/', response_model=PromotionOut, status_code=201)
async def create_promotion(payload: PromotionIn):
    promotion_id = await db_manager.add_promotion(payload)
    response = {
        'id': promotion_id,
        **payload.dict()
    }
    return response


@promotions.get('/', response_model=List[PromotionOut])
async def get_promotions():
    return await db_manager.get_all_promotions()


@promotions.get('/{id}/', response_model=PromotionOut)
async def get_promotion(id: int):
    promotion = await db_manager.get_promotion(id)
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return promotion


@promotions.put('/{id}/', response_model=PromotionOut)
async def update_promotion(id: int, payload: PromotionUpdate):
    promotion = await db_manager.get_promotion(id)
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")

    update_data = payload.dict(exclude_unset=True)
    return await db_manager.update_promotion(id, update_data)


@promotions.delete('/{id}/', response_model=None)
async def delete_promotion(id: int):
    promotion = await db_manager.get_promotion(id)
    if not promotion:
        raise HTTPException(status_code=404, detail="Promotion not found")
    return await db_manager.delete_promotion(id)
