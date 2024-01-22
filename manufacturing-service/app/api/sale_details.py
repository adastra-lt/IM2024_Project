from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import SaleDetailsOut, SaleDetailsCreate, SaleDetailsUpdate
from app.api import db_manager

sale_details = APIRouter()


@sale_details.post('/', response_model=SaleDetailsOut, status_code=201)
async def create_sale_detail(payload: SaleDetailsCreate):
    sale_detail_id = await db_manager.add_sale_detail(payload)
    response = {
        'id': sale_detail_id,
        **payload.dict()
    }
    return response


@sale_details.get('/', response_model=List[SaleDetailsOut])
async def get_sale_details():
    return await db_manager.get_all_sale_details()


@sale_details.get('/{id}/', response_model=SaleDetailsOut)
async def get_sale_detail(id: int):
    sale_detail = await db_manager.get_sale_detail(id)
    if not sale_detail:
        raise HTTPException(status_code=404, detail="Sale detail not found")
    return sale_detail


@sale_details.put('/{id}/', response_model=SaleDetailsOut)
async def update_sale_detail(id: int, payload: SaleDetailsUpdate):
    sale_detail = await db_manager.get_sale_detail(id)
    if not sale_detail:
        raise HTTPException(status_code=404, detail="Sale detail not found")

    update_data = payload.dict(exclude_unset=True)
    return await db_manager.update_sale_detail(id, update_data)


@sale_details.delete('/{id}/', response_model=None)
async def delete_sale_detail(id: int):
    sale_detail = await db_manager.get_sale_detail(id)
    if not sale_detail:
        raise HTTPException(status_code=404, detail="Sale detail not found")
    return await db_manager.delete_sale_detail(id)
