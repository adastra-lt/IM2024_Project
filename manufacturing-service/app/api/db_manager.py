from app.api.models import (
    ProductIn, ProductOut, ProductUpdate,
    StoreIn, StoreOut, StoreUpdate,
    CustomerIn, CustomerOut, CustomerUpdate,
    SalespersonIn, SalespersonOut, SalespersonUpdate,
    SaleIn, SaleOut, SaleUpdate,
    SaleDetailsIn, SaleDetailsOut, SaleDetailsUpdate,
    PromotionIn, PromotionOut, PromotionUpdate,
    PromotionTypeIn, PromotionTypeOut, PromotionTypeUpdate
)
from app.api.db import (
    products, stores, customers, salespersons, sales, saledetails, promotions, promotiontypes,
    database
)


# Product functions
async def add_product(payload: ProductIn):
    query = products.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_products():
    query = products.select()
    return await database.fetch_all(query=query)


async def get_product(id: int):
    query = products.select().where(products.c.id == id)
    return await database.fetch_one(query=query)


async def delete_product(id: int):
    query = products.delete().where(products.c.id == id)
    return await database.execute(query=query)


async def update_product(id: int, payload: ProductUpdate):
    query = products.update().where(products.c.id == id).values(**payload.dict())
    return await database.execute(query=query)


# Store functions
async def add_store(payload: StoreIn):
    query = stores.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_stores():
    query = stores.select()
    return await database.fetch_all(query=query)


async def get_store(id: int):
    query = stores.select().where(stores.c.id == id)
    return await database.fetch_one(query=query)


async def delete_store(id: int):
    query = stores.delete().where(stores.c.id == id)
    return await database.execute(query=query)


async def update_store(id: int, payload: StoreUpdate):
    query = stores.update().where(stores.c.id == id).values(**payload.dict())
    return await database.execute(query=query)


# Customer functions
async def add_customer(payload: CustomerIn):
    query = customers.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_customers():
    query = customers.select()
    return await database.fetch_all(query=query)


async def get_customer(id: int):
    query = customers.select().where(customers.c.id == id)
    return await database.fetch_one(query=query)


async def delete_customer(id: int):
    query = customers.delete().where(customers.c.id == id)
    return await database.execute(query=query)


async def update_customer(id: int, payload: CustomerUpdate):
    query = customers.update().where(customers.c.id == id).values(**payload.dict())
    return await database.execute(query=query)


# Salesperson functions
async def add_salesperson(payload: SalespersonIn):
    query = salespersons.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_salespersons():
    query = salespersons.select()
    return await database.fetch_all(query=query)


async def get_salesperson(id: int):
    query = salespersons.select().where(salespersons.c.id == id)
    return await database.fetch_one(query=query)


async def delete_salesperson(id: int):
    query = salespersons.delete().where(salespersons.c.id == id)
    return await database.execute(query=query)


async def update_salesperson(id: int, payload: SalespersonUpdate):
    query = salespersons.update().where(salespersons.c.id == id).values(**payload.dict())
    return await database.execute(query=query)


# Sale functions
async def add_sale(payload: SaleIn):
    query = sales.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_sales():
    query = sales.select()
    return await database.fetch_all(query=query)


async def get_sale(id: int):
    query = sales.select().where(sales.c.id == id)
    return await database.fetch_one(query=query)


async def delete_sale(id: int):
    query = sales.delete().where(sales.c.id == id)
    return await database.execute(query=query)


async def update_sale(id: int, payload: SaleUpdate):
    query = sales.update().where(sales.c.id == id).values(**payload.dict())
    return await database.execute(query=query)


# SaleDetails functions
async def add_sale_details(payload: SaleDetailsIn):
    query = saledetails.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_sale_details():
    query = saledetails.select()
    return await database.fetch_all(query=query)


async def get_sale_details(id: int):
    query = saledetails.select().where(saledetails.c.id == id)
    return await database.fetch_one(query=query)


async def delete_sale_details(id: int):
    query = saledetails.delete().where(saledetails.c.id == id)
    return await database.execute(query=query)


async def update_sale_details(id: int, payload: SaleDetailsUpdate):
    query = saledetails.update().where(saledetails.c.id == id).values(**payload.dict())
    return await database.execute(query=query)


# Promotion functions
async def add_promotion(payload: PromotionIn):
    query = promotions.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_promotions():
    query = promotions.select()
    return await database.fetch_all(query=query)


async def get_promotion(id: int):
    query = promotions.select().where(promotions.c.id == id)
    return await database.fetch_one(query=query)


async def delete_promotion(id: int):
    query = promotions.delete().where(promotions.c.id == id)
    return await database.execute(query=query)


async def update_promotion(id: int, payload: PromotionUpdate):
    query = promotions.update().where(promotions.c.id == id).values(**payload.dict())
    return await database.execute(query=query)


# PromotionType functions
async def add_promotion_type(payload: PromotionTypeIn):
    query = promotiontypes.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_promotion_types():
    query = promotiontypes.select()
    return await database.fetch_all(query=query)


async def get_promotion_type(id: int):
    query = promotiontypes.select().where(promotiontypes.c.id == id)
    return await database.fetch_one(query=query)


async def delete_promotion_type(id: int):
    query = promotiontypes.delete().where(promotiontypes.c.id == id)
    return await database.execute(query=query)


async def update_promotion_type(id: int, payload: PromotionTypeUpdate):
    query = promotiontypes.update().where(promotiontypes.c.id == id).values(**payload.dict())
    return await database.execute(query=query)
