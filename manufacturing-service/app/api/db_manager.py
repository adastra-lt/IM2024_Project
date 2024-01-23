from app.api.models import (
    ProductCreate, ProductOut, ProductUpdate,
    StoreCreate, StoreOut, StoreUpdate,
    CustomerCreate, CustomerOut, CustomerUpdate,
    SalespersonCreate, SalespersonOut, SalespersonUpdate,
    SaleCreate, SaleOut, SaleUpdate,
    SaleDetailsCreate, SaleDetailsOut, SaleDetailsUpdate,
    PromotionCreate, PromotionOut, PromotionUpdate,
    PromotionTypeCreate, PromotionTypeOut, PromotionTypeUpdate,
    GenderCreate, GenderOut, GenderUpdate,
    StoreTypeCreate, StoreTypeOut, StoreTypeUpdate,
    ProductStoreOut,
)
from app.api.db import (
    product, store, customer, salesperson, sale, sale_detail, promotion, promotion_type, store_type, gender, product_store,
    database
)


# Product functions
async def add_product(payload: ProductCreate):
    query = product.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_products():
    query = product.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in ProductOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]


async def get_product(id: int):
    query = product.select().where(product.c.product_id == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
            field: result[field]
            for field in ProductOut.__fields__.keys()
            if field in result
        }
    return result


async def delete_product(id: int):
    query = product.delete().where(product.c.product_id == id)
    return await database.execute(query=query)


async def update_product(id: int, payload: ProductUpdate):
    query = product.update().where(product.c.product_id == id).values(**payload.dict())
    return await database.execute(query=query)


# Store functions
async def add_store(payload: StoreCreate):
    query = store.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_stores():
    query = store.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in StoreOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]


async def get_store(id: int):
    query = store.select().where(store.c.store_id == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
            field: result[field]
            for field in StoreOut.__fields__.keys()
            if field in result
        }
    return result


async def delete_store(id: int):
    query = store.delete().where(store.c.store_id == id)
    return await database.execute(query=query)


async def update_store(id: int, payload: StoreUpdate):
    query = store.update().where(store.c.store_id == id).values(**payload.dict())
    return await database.execute(query=query)


# Customer functions
async def add_customer(payload: CustomerCreate):
    query = customer.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_customers():
    query = customer.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in CustomerOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]


async def get_customer(id: int):
    query = customer.select().where(customer.c.customer_id == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
            field: result[field]
            for field in CustomerOut.__fields__.keys()
            if field in result
        }
    return result


async def delete_customer(id: int):
    query = customer.delete().where(customer.c.customer_id == id)
    return await database.execute(query=query)


async def update_customer(id: int, payload: CustomerUpdate):
    query = customer.update().where(
        customer.c.customer_id == id).values(**payload.dict())
    return await database.execute(query=query)


# Salesperson functions
async def add_salesperson(payload: SalespersonCreate):
    query = salesperson.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_salespersons():
    query = salesperson.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in SalespersonOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]


async def get_salesperson(id: int):
    query = salesperson.select().where(salesperson.c.salesperson_id == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
            field: result[field]
            for field in SalespersonOut.__fields__.keys()
            if field in result
        }
    return result


async def delete_salesperson(id: int):
    query = salesperson.delete().where(salesperson.c.salesperson_id == id)
    return await database.execute(query=query)


async def update_salesperson(id: int, payload: SalespersonUpdate):
    query = salesperson.update().where(
        salesperson.c.salesperson_id == id).values(**payload.dict())
    return await database.execute(query=query)


# Sale functions
async def add_sale(payload: SaleCreate):
    query = sale.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_sales():
    query = sale.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in SaleOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]


async def get_sale(id: int):
    query = sale.select().where(sale.c.sale_id == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
            field: result[field]
            for field in SaleOut.__fields__.keys()
            if field in result
        }
    return result


async def delete_sale(id: int):
    query = sale.delete().where(sale.c.sale_id == id)
    return await database.execute(query=query)


async def update_sale(id: int, payload: SaleUpdate):
    query = sale.update().where(sale.c.sale_id == id).values(**payload.dict())
    return await database.execute(query=query)


# SaleDetails functions
async def add_sale_details(payload: SaleDetailsCreate):
    query = sale_detail.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_sale_details():
    query = sale_detail.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in SaleDetailsOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]


async def get_sale_details(id: int):
    query = sale_detail.select().where(sale_detail.c.sale_details_id == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
            field: result[field]
            for field in SaleDetailsOut.__fields__.keys()
            if field in result
        }
    return result


async def delete_sale_details(id: int):
    query = sale_detail.delete().where(sale_detail.c.sale_details_id == id)
    return await database.execute(query=query)


async def update_sale_details(id: int, payload: SaleDetailsUpdate):
    query = sale_detail.update().where(
        sale_detail.c.sale_details_id == id).values(**payload.dict())
    return await database.execute(query=query)


# Promotion functions
async def add_promotion(payload: PromotionCreate):
    query = promotion.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_promotions():
    query = promotion.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in PromotionOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]


async def get_promotion(id: int):
    query = promotion.select().where(promotion.c.promotion_id == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
            field: result[field]
            for field in PromotionOut.__fields__.keys()
            if field in result
        }
    return result


async def delete_promotion(id: int):
    query = promotion.delete().where(promotion.c.promotion_id == id)
    return await database.execute(query=query)


async def update_promotion(id: int, payload: PromotionUpdate):
    query = promotion.update().where(
        promotion.c.promotion_id == id).values(**payload.dict())
    return await database.execute(query=query)


# PromotionType functions
async def add_promotion_type(payload: PromotionTypeCreate):
    query = promotion_type.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_promotion_types():
    query = promotion_type.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in PromotionTypeOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]


async def get_promotion_type(id: int):
    query = promotion_type.select().where(promotion_type.c.promo_type_id == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
            field: result[field]
            for field in PromotionTypeOut.__fields__.keys()
            if field in result
        }
    return result


async def delete_promotion_type(id: int):
    query = promotion_type.delete().where(promotion_type.c.promo_type_id == id)
    return await database.execute(query=query)


async def update_promotion_type(id: int, payload: PromotionTypeUpdate):
    query = promotion_type.update().where(
        promotion_type.c.promo_type_id == id).values(**payload.dict())
    return await database.execute(query=query)

# Gender functions


async def add_gender(payload: GenderCreate):
    query = gender.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_genders():
    query = gender.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in GenderOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]


async def get_gender(id: int):
    query = gender.select().where(gender.c.gender_id == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
            field: result[field]
            for field in GenderOut.__fields__.keys()
            if field in result
        }
    return result


async def delete_gender(id: int):
    query = gender.delete().where(gender.c.gender_id == id)
    return await database.execute(query=query)


async def update_gender(id: int, payload: GenderUpdate):
    query = gender.update().where(gender.c.gender_id == id).values(**payload.dict())
    return await database.execute(query=query)


# StoreType functions
async def add_store_type(payload: StoreTypeCreate):
    query = store_type.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_store_types():
    query = store_type.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in StoreTypeOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]


async def get_store_type(id: int):
    query = store_type.select().where(store_type.c.store_type_id == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
            field: result[field]
            for field in StoreTypeOut.__fields__.keys()
            if field in result
        }
    return result


async def delete_store_type(id: int):
    query = store_type.delete().where(store_type.c.store_type_id == id)
    return await database.execute(query=query)


async def update_store_type(id: int, payload: StoreTypeUpdate):
    query = store_type.update().where(
        store_type.c.store_type_id == id).values(**payload.dict())
    return await database.execute(query=query)


# ProductStore functions

async def get_all_product_stores():
    query = product_store.select()
    results = await database.fetch_all(query=query)
    return [
        {
            field: result[field]
            for field in ProductStoreOut.__fields__.keys()
            if field in result
        }
        for result in results
    ]


async def get_product_store(id: int):
    query = product_store.select().where(product_store.c.product_store_id == id)
    result = await database.fetch_one(query=query)
    if result:
        return {
            field: result[field]
            for field in ProductStoreOut.__fields__.keys()
            if field in result
        }
    return result
