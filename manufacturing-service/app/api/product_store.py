from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import ProductStoreOut
from app.api import db_manager

product_store = APIRouter()


@product_store.get('/', response_model=List[ProductStoreOut])
async def get_product_store_entries():
    return await db_manager.get_all_product_stores()


@product_store.get('/{id}/', response_model=ProductStoreOut)
async def get_product_store_entry(id: int):
    entry = await db_manager.get_product_store(id)
    if not entry:
        raise HTTPException(
            status_code=404, detail="Product-Store entry not found")
    return entry
