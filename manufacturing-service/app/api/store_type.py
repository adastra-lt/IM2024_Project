from typing import List
from fastapi import APIRouter, HTTPException
from app.api.models import StoreTypeOut, StoreTypeCreate, StoreTypeUpdate
from app.api import db_manager

store_type = APIRouter()


@store_type.post('/', response_model=StoreTypeOut, status_code=201)
async def create_store_type(payload: StoreTypeCreate):
    store_type_id = await db_manager.add_store_type(payload)
    response = {'id': store_type_id, **payload.dict()}
    return response


@store_type.get('/', response_model=List[StoreTypeOut])
async def get_store_types():
    return await db_manager.get_all_store_types()


@store_type.get('/{id}/', response_model=StoreTypeOut)
async def get_store_type(id: int):
    store_type = await db_manager.get_store_type(id)
    if not store_type:
        raise HTTPException(status_code=404, detail="Store Type not found")
    return store_type


@store_type.put('/{id}/', response_model=StoreTypeOut)
async def update_store_type(id: int, payload: StoreTypeUpdate):
    store_type = await db_manager.get_store_type(id)
    if not store_type:
        raise HTTPException(status_code=404, detail="Store Type not found")
    return await db_manager.update_store_type(id, payload.dict(exclude_unset=True))


@store_type.delete('/{id}/', response_model=None)
async def delete_store_type(id: int):
    store_type = await db_manager.get_store_type(id)
    if not store_type:
        raise HTTPException(status_code=404, detail="Store Type not found")
    return await db_manager.delete_store_type(id)
