from fastapi import FastAPI
from app.api.db import metadata, database, engine
from app.api.products import products
from app.api.sales import sales
from app.api.inventory import inventory
from app.api.saledetails import saledetails
from app.api.salespersons import salespersons
from app.api.promotions import promotions
from app.api.promotiontypes import promotiontypes


metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/manufacturing/openapi.json", docs_url="/api/v1/manufacturing/docs")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Include your routers here
app.include_router(products, prefix='/api/v1/products', tags=['products'])
app.include_router(sales, prefix='/api/v1/sales', tags=['sales'])
app.include_router(inventory, prefix='/api/v1/inventory', tags=['inventory'])
app.include_router(saledetails, prefix='/api/v1/saledetails', tags=['saledetails'])
# app.include_router(customers, prefix='/api/v1/customers', tags=['customers'])
app.include_router(salespersons, prefix='/api/v1/salespersons', tags=['salespersons'])
app.include_router(promotions, prefix='/api/v1/promotions', tags=['promotions'])
app.include_router(promotiontypes, prefix='/api/v1/promotiontypes', tags=['promotiontypes'])
