from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import ProductOut, ProductIn, ProductUpdate
from app.api import db_manager

products = APIRouter()


@products.post('/', response_model=ProductOut, status_code=201)
async def create_product(payload: ProductIn):
    product_id = await db_manager.add_product(payload)
    response = {
        'id': product_id,
        **payload.dict()
    }
    return response


@products.get('/', response_model=List[ProductOut])
async def get_products():
    return await db_manager.get_all_products()


@products.get('/{id}/', response_model=ProductOut)
async def get_product(id: int):
    product = await db_manager.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@products.put('/{id}/', response_model=ProductOut)
async def update_product(id: int, payload: ProductUpdate):
    product = await db_manager.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    update_data = payload.dict(exclude_unset=True)
    return await db_manager.update_product(id, update_data)


@products.delete('/{id}/', response_model=None)
async def delete_product(id: int):
    product = await db_manager.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return await db_manager.delete_product(id)
