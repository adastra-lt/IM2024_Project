from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import StoreOut, StoreCreate, StoreUpdate
from app.api import db_manager

store = APIRouter()


@store.post('/', response_model=StoreOut, status_code=201)
async def create_store(payload: StoreCreate):
    store_id = await db_manager.add_store(payload)
    response = {'store_id': store_id, **payload.dict()}
    return response


@store.get('/', response_model=List[StoreOut])
async def get_stores():
    return await db_manager.get_all_stores()


@store.get('/{id}/', response_model=StoreOut)
async def get_store(id: int):
    store = await db_manager.get_store(id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store


@store.put('/{id}/', response_model=StoreOut)
async def update_store(id: int, payload: StoreUpdate):
    store = await db_manager.get_store(id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return await db_manager.update_store(id, payload.dict(exclude_unset=True))


@store.delete('/{id}/', response_model=None)
async def delete_store(id: int):
    store = await db_manager.get_store(id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return await db_manager.delete_store(id)
