from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import ProductStoreOut, ProductStoreCreate, ProductStoreUpdate
from app.api import db_manager

product_store = APIRouter()


@product_store.post('/', response_model=ProductStoreOut, status_code=201)
async def create_product_store_entry(payload: ProductStoreCreate):
    entry_id = await db_manager.add_product_store_entry(payload)
    response = {'id': entry_id, **payload.dict()}
    return response


@product_store.get('/', response_model=List[ProductStoreOut])
async def get_product_store_entries():
    return await db_manager.get_all_product_store_entries()


@product_store.get('/{id}/', response_model=ProductStoreOut)
async def get_product_store_entry(id: int):
    entry = await db_manager.get_product_store_entry(id)
    if not entry:
        raise HTTPException(
            status_code=404, detail="Product-Store entry not found")
    return entry


@product_store.put('/{id}/', response_model=ProductStoreOut)
async def update_product_store_entry(id: int, payload: ProductStoreUpdate):
    entry = await db_manager.get_product_store_entry(id)
    if not entry:
        raise HTTPException(
            status_code=404, detail="Product-Store entry not found")
    updated_entry = await db_manager.update_product_store_entry(id, payload.dict(exclude_unset=True))
    if updated_entry is None:
        raise HTTPException(
            status_code=404, detail="Product-Store entry not found")
    return updated_entry


@product_store.delete('/{id}/', response_model=None, status_code=204)
async def delete_product_store_entry(id: int):
    entry = await db_manager.get_product_store_entry(id)
    if not entry:
        raise HTTPException(
            status_code=404, detail="Product-Store entry not found")
    await db_manager.delete_product_store_entry(id)
    return {"detail": "Product-Store entry deleted successfully"}
