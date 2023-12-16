from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import SaleOut, SaleIn, SaleUpdate
from app.api import db_manager

sales = APIRouter()


@sales.post('/', response_model=SaleOut, status_code=201)
async def create_sale(payload: SaleIn):
    sale_id = await db_manager.add_sale(payload)
    response = {
        'id': sale_id,
        **payload.dict()
    }
    return response


@sales.get('/', response_model=List[SaleOut])
async def get_sales():
    return await db_manager.get_all_sales()


@sales.get('/{id}/', response_model=SaleOut)
async def get_sale(id: int):
    sale = await db_manager.get_sale(id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale


@sales.put('/{id}/', response_model=SaleOut)
async def update_sale(id: int, payload: SaleUpdate):
    sale = await db_manager.get_sale(id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")

    update_data = payload.dict(exclude_unset=True)
    return await db_manager.update_sale(id, update_data)


@sales.delete('/{id}/', response_model=None)
async def delete_sale(id: int):
    sale = await db_manager.get_sale(id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return await db_manager.delete_sale(id)
