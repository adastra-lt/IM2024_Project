from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import GenderOut, GenderCreate, GenderUpdate
from app.api import db_manager

gender = APIRouter()


@gender.post('/', response_model=GenderOut, status_code=201)
async def create_gender(payload: GenderCreate):
    gender_id = await db_manager.add_gender(payload)
    response = {'gender_id': gender_id, **payload.dict()}
    return response


@gender.get('/', response_model=List[GenderOut])
async def get_genders():
    return await db_manager.get_all_genders()


@gender.get('/{id}/', response_model=GenderOut)
async def get_gender(id: int):
    gender = await db_manager.get_gender(id)
    if not gender:
        raise HTTPException(status_code=404, detail="Gender not found")
    return gender


@gender.put('/{id}/', response_model=GenderOut)
async def update_gender(id: int, payload: GenderUpdate):
    gender = await db_manager.get_gender(id)
    if not gender:
        raise HTTPException(status_code=404, detail="Gender not found")
    update_data = payload.dict(exclude_unset=True)
    return await db_manager.update_gender(id, update_data)


@gender.delete('/{id}/', response_model=None)
async def delete_gender(id: int):
    gender = await db_manager.get_gender(id)
    if not gender:
        raise HTTPException(status_code=404, detail="Gender not found")
    return await db_manager.delete_gender(id)
