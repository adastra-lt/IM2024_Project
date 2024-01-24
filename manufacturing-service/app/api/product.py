from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import ProductOut, ProductCreate, ProductUpdate
from app.api import db_manager

product = APIRouter()


@product.post('/', response_model=ProductOut, status_code=201)
async def create_product(payload: ProductCreate):
    product_id = await db_manager.add_product(payload)
    response = {
        'product_id': product_id,
        **payload.dict()
    }
    return response


@product.get('/', response_model=List[ProductOut])
async def get_products():
    return await db_manager.get_all_products()


@product.get('/{id}/', response_model=ProductOut)
async def get_product(id: int):
    product = await db_manager.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@product.put('/{id}/', response_model=ProductOut)
async def update_product(id: int, payload: ProductUpdate):
    product = await db_manager.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return await db_manager.update_product(id, payload)


@product.delete('/{id}/', response_model=None)
async def delete_product(id: int):
    product = await db_manager.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return await db_manager.delete_product(id)
