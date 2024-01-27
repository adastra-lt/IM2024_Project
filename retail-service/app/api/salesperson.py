from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import SalespersonOut, SalespersonCreate, SalespersonUpdate
from app.api import db_manager

salesperson = APIRouter()


@salesperson.post('/', response_model=SalespersonOut, status_code=201)
async def create_salesperson(payload: SalespersonCreate):
    salesperson_id = await db_manager.add_salesperson(payload)
    response = {
        'salesperson_id': salesperson_id,
        **payload.dict()
    }
    return response


@salesperson.get('/', response_model=List[SalespersonOut])
async def get_salespersons():
    return await db_manager.get_all_salespersons()


@salesperson.get('/{id}/', response_model=SalespersonOut)
async def get_salesperson(id: int):
    salesperson = await db_manager.get_salesperson(id)
    if not salesperson:
        raise HTTPException(status_code=404, detail="Salesperson not found")
    return salesperson


@salesperson.put('/{id}/', response_model=SalespersonOut)
async def update_salesperson(id: int, payload: SalespersonUpdate):
    salesperson = await db_manager.get_salesperson(id)
    if not salesperson:
        raise HTTPException(status_code=404, detail="Salesperson not found")

    return await db_manager.update_salesperson(id, payload)


@salesperson.delete('/{id}/', response_model=None)
async def delete_salesperson(id: int):
    salesperson = await db_manager.get_salesperson(id)
    if not salesperson:
        raise HTTPException(status_code=404, detail="Salesperson not found")
    return await db_manager.delete_salesperson(id)
