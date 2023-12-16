from fastapi import FastAPI
from app.api.db import metadata, database, engine
from app.api.products import products  # Import the products router
from app.api.sales import sales       # Import the sales router
from app.api.inventory import inventory  # Import the inventory router

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/manufacturing/openapi.json", docs_url="/api/v1/manufacturing/docs")

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Include your routers here
app.include_router(products, prefix='/api/v1/manufacturing', tags=['products'])
app.include_router(sales, prefix='/api/v1/manufacturing', tags=['sales'])
app.include_router(inventory, prefix='/api/v1/manufacturing', tags=['inventory'])
