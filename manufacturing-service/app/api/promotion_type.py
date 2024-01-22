from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import PromotionTypeOut, PromotionTypeCreate, PromotionTypeUpdate
from app.api import db_manager

promotion_type = APIRouter()


@promotion_type.post('/', response_model=PromotionTypeOut, status_code=201)
async def create_promotion_type(payload: PromotionTypeCreate):
    promotion_type_id = await db_manager.add_promotion_type(payload)
    response = {
        'id': promotion_type_id,
        **payload.dict()
    }
    return response


@promotion_type.get('/', response_model=List[PromotionTypeOut])
async def get_promotion_types():
    return await db_manager.get_all_promotion_types()


@promotion_type.get('/{id}/', response_model=PromotionTypeOut)
async def get_promotion_type(id: int):
    promotion_type = await db_manager.get_promotion_type(id)
    if not promotion_type:
        raise HTTPException(status_code=404, detail="Promotion type not found")
    return promotion_type


@promotion_type.put('/{id}/', response_model=PromotionTypeOut)
async def update_promotion_type(id: int, payload: PromotionTypeUpdate):
    promotion_type = await db_manager.get_promotion_type(id)
    if not promotion_type:
        raise HTTPException(status_code=404, detail="Promotion type not found")

    update_data = payload.dict(exclude_unset=True)
    return await db_manager.update_promotion_type(id, update_data)


@promotion_type.delete('/{id}/', response_model=None)
async def delete_promotion_type(id: int):
    promotion_type = await db_manager.get_promotion_type(id)
    if not promotion_type:
        raise HTTPException(status_code=404, detail="Promotion type not found")
    return await db_manager.delete_promotion_type(id)
