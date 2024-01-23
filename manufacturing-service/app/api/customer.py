from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import CustomerOut, CustomerCreate, CustomerUpdate
from app.api import db_manager

customer = APIRouter()


@customer.post("/", response_model=CustomerOut, status_code=201)
async def create_customer(payload: CustomerCreate):
    customer_id = await db_manager.add_customer(payload)
    response = {"customer_id": customer_id, **payload.dict()}
    return response


@customer.get("/", response_model=List[CustomerOut])
async def get_customers():
    return await db_manager.get_all_customers()


@customer.get("/{id}/", response_model=CustomerOut)
async def get_customer(id: int):
    customer = await db_manager.get_customer(id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@customer.put("/{id}/", response_model=CustomerOut)
async def update_customer(id: int, payload: CustomerUpdate):
    customer = await db_manager.get_customer(id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    update_data = payload.dict(exclude_unset=True)
    updated_customer = await db_manager.update_customer(id, update_data)
    if updated_customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_customer


@customer.delete("/{id}/", response_model=None, status_code=204)
async def delete_customer(id: int):
    customer = await db_manager.get_customer(id)
    if not customer:
        raise HTTPException(status_code=404, detail="Customer not found")
    await db_manager.delete_customer(id)
    return {"detail": "Customer deleted successfully"}
