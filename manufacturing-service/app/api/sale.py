from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import SaleOut, SaleCreate, SaleUpdate
from app.api import db_manager

sale = APIRouter()


@sale.post('/', response_model=SaleOut, status_code=201)
async def create_sale(payload: SaleCreate):
    sale_id = await db_manager.add_sale(payload)
    response = {
        'sale_id': sale_id,
        **payload.dict()
    }
    return response


@sale.get('/', response_model=List[SaleOut])
async def get_sales():
    return await db_manager.get_all_sales()


@sale.get('/{id}/', response_model=SaleOut)
async def get_sale(id: int):
    sale = await db_manager.get_sale(id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale


@sale.put('/{id}/', response_model=SaleOut)
async def update_sale(id: int, payload: SaleUpdate):
    sale = await db_manager.get_sale(id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")

    update_data = payload.dict(exclude_unset=True)
    return await db_manager.update_sale(id, update_data)


@sale.delete('/{id}/', response_model=None)
async def delete_sale(id: int):
    sale = await db_manager.get_sale(id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return await db_manager.delete_sale(id)
