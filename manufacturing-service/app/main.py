from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError
from app.api.db import metadata, database, engine
from app.api.customer import customer
from app.api.gender import gender
from app.api.product import product
from app.api.product_store import product_store
from app.api.sale import sale
from app.api.sale_details import sale_details
from app.api.salesperson import salesperson
from app.api.store import store
from app.api.store_type import store_type
from app.api.promotion import promotion
from app.api.promotion_type import promotion_type
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException


metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/manufacturing/openapi.json",
              docs_url="/api/v1/manufacturing/docs")


# Custom exception handlers for development
# if os.getenv('ENV') == 'development':
if 1:
    @app.exception_handler(SQLAlchemyError)
    async def sqlalchemy_exception_handler(request: Request, exc: SQLAlchemyError):
        return JSONResponse(
            status_code=500,
            content={
                "message": "An error occurred with the database operation", "detail": str(exc)}
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(request: Request, exc: RequestValidationError):
        return JSONResponse(
            status_code=422,
            content={"detail": exc.errors(), "body": exc.body},
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={"message": exc.detail},
        )

    @app.exception_handler(Exception)
    async def general_exception_handler(request: Request, exc: Exception):
        return JSONResponse(
            status_code=500,
            content={"message": "An internal server error occurred.",
                     "detail": str(exc)},
        )


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# Include your routers here
app.include_router(product, prefix='/api/v1/product',
                   tags=['product'])
app.include_router(product_store, prefix='/api/v1/product_store',
                   tags=['product_store'])
app.include_router(sale, prefix='/api/v1/sale',
                   tags=['sale'])
app.include_router(sale_details, prefix='/api/v1/sale_details',
                   tags=['sale_details'])
app.include_router(customer, prefix='/api/v1/customer',
                   tags=['customer'])
app.include_router(salesperson, prefix='/api/v1/salesperson',
                   tags=['salesperson'])
app.include_router(gender, prefix='/api/v1/gender',
                   tags=['gender'])
app.include_router(store, prefix='/api/v1/store',
                   tags=['store'])
app.include_router(store_type, prefix='/api/v1/store_type',
                   tags=['store_type'])
app.include_router(promotion, prefix='/api/v1/promotion',
                   tags=['promotion'])
app.include_router(promotion_type, prefix='/api/v1/promotion_type',
                   tags=['promotion_type'])
