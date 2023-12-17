from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import CustomerOut, CustomerIn, CustomerUpdate
from app.api import db_manager

customers = APIRouter()


@customers.post('/', response_model=CustomerOut, status_code=201)
async def create_customer(payload: CustomerIn):
    customer_id = await db_manager.add_customer(payload)
    response = {
        'id': customer_id,
        **payload.dict()
    }
    return response


@customers.get('/', response_model=List[CustomerOut])
async def get_customers():
    return await db_manager.get_all_customers()


@customers.get('/{id}/', response_model=CustomerOut)
async def get_customer(id: int):
    customer = await db_manager.get_customer(id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@customers.put('/{id}/', response_model=CustomerOut)
async def update_customer(id: int, payload: CustomerUpdate):
    customer = await db_manager.get_customer(id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")

    update_data = payload.dict(exclude_unset=True)
    return await db_manager.update_customer(id, update_data)


@customers.delete('/{id}/', response_model=None)
async def delete_customer(id: int):
    customer = await db_manager.get_customer(id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return await db_manager.delete_customer(id)
