from typing import List
from fastapi import APIRouter, HTTPException

# Assuming InventoryIn, InventoryOut, and InventoryUpdate are defined in your models
from app.api.models import InventoryOut, InventoryIn, InventoryUpdate
from app.api import db_manager

inventory = APIRouter()


@inventory.post('/', response_model=InventoryOut, status_code=201)
async def add_inventory_item(payload: InventoryIn):
    item_id = await db_manager.add_inventory_item(payload)
    response = {
        'id': item_id,
        **payload.dict()
    }
    return response


@inventory.get('/', response_model=List[InventoryOut])
async def get_inventory():
    return await db_manager.get_all_inventory_items()


@inventory.get('/{id}/', response_model=InventoryOut)
async def get_inventory_item(id: int):
    item = await db_manager.get_inventory_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return item


@inventory.put('/{id}/', response_model=InventoryOut)
async def update_inventory_item(id: int, payload: InventoryUpdate):
    item = await db_manager.get_inventory_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")

    update_data = payload.dict(exclude_unset=True)
    return await db_manager.update_inventory_item(id, update_data)


@inventory.delete('/{id}/', response_model=None)
async def delete_inventory_item(id: int):
    item = await db_manager.get_inventory_item(id)
    if not item:
        raise HTTPException(status_code=404, detail="Inventory item not found")
    return await db_manager.delete_inventory_item(id)
