from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime, date


class ProductBase(BaseModel):
    product_name: str
    price: float
    # Add any additional fields present in your products table
    # description: Optional[str] = None


class ProductCreate(ProductBase):
    pass


class ProductOut(ProductBase):
    product_id: int

    class Config:
        orm_mode = True


class ProductUpdate(BaseModel):
    product_name: Optional[str] = None
    price: Optional[float] = None


class StoreBase(BaseModel):
    store_name: str
    store_area: str
    store_country: str
    store_city: str
    store_address: str
    store_type_id: int


class StoreCreate(StoreBase):
    pass


class StoreOut(StoreBase):
    store_id: int

    class Config:
        orm_mode = True


class StoreUpdate(BaseModel):
    store_name: Optional[str] = None
    store_area: Optional[str] = None
    store_country: Optional[str] = None
    store_city: Optional[str] = None
    store_address: Optional[str] = None
    store_type_id: Optional[int] = None


class StoreTypeBase(BaseModel):
    store_type_name: str


class StoreTypeCreate(StoreTypeBase):
    pass


class StoreTypeOut(StoreTypeBase):
    store_type_id: int

    class Config:
        orm_mode = True


class StoreTypeUpdate(BaseModel):
    store_type_name: Optional[str] = None


class ProductStoreBase(BaseModel):
    product_id: int
    store_id: int


class ProductStoreOut(ProductStoreBase):
    product_store_id: int

    class Config:
        orm_mode = True


class GenderBase(BaseModel):
    gender_name: str


class GenderCreate(GenderBase):
    pass


class GenderOut(GenderBase):
    gender_id: int

    class Config:
        orm_mode = True


class GenderUpdate(BaseModel):
    gender_name: Optional[str] = None


class CustomerBase(BaseModel):
    customer_name: str
    customer_address: str
    customer_vat: float
    customer_code: int
    gender_id: int
    customer_type: str


class CustomerCreate(CustomerBase):
    pass


class CustomerOut(CustomerBase):
    customer_id: int

    class Config:
        orm_mode = True


class CustomerUpdate(BaseModel):
    customer_name: Optional[str] = None
    customer_address: Optional[str] = None
    customer_vat: Optional[float] = None
    customer_code: Optional[int] = None
    gender_id: Optional[int] = None
    customer_type: Optional[str] = None


class SalespersonBase(BaseModel):
    max_discount: float
    store_id: int


class SalespersonCreate(SalespersonBase):
    pass


class SalespersonOut(SalespersonBase):
    salesperson_id: int

    class Config:
        orm_mode = True


class SalespersonUpdate(BaseModel):
    max_discount: Optional[float] = None
    store_id: Optional[int] = None


class SaleBase(BaseModel):
    sale_date: datetime
    store_id: int
    salesperson_id: int
    customer_id: int


class SaleCreate(SaleBase):
    pass


class SaleOut(SaleBase):
    sale_id: int

    class Config:
        orm_mode = True


class SaleUpdate(BaseModel):
    sale_date: Optional[datetime] = None
    store_id: Optional[int] = None
    salesperson_id: Optional[int] = None
    customer_id: Optional[int] = None


class SaleDetailsBase(BaseModel):
    product_id: int
    sale_id: int
    promotion_id: Optional[int] = None
    quantity: int
    final_price: float


class SaleDetailsCreate(SaleDetailsBase):
    pass


class SaleDetailsOut(SaleDetailsBase):
    sale_details_id: int

    class Config:
        orm_mode = True


class SaleDetailsUpdate(BaseModel):
    product_id: Optional[int] = None
    sale_id: Optional[int] = None
    promotion_id: Optional[int] = None
    quantity: Optional[int] = None
    final_price: Optional[float] = None


class PromotionBase(BaseModel):
    promotion_type_id: int
    promotion_start: date
    promotion_end: date


class PromotionCreate(PromotionBase):
    pass


class PromotionOut(PromotionBase):
    promotion_id: int

    class Config:
        orm_mode = True


class PromotionUpdate(BaseModel):
    promotion_type_id: Optional[int] = None
    promotion_start: Optional[datetime] = None
    promotion_end: Optional[datetime] = None


class PromotionTypeBase(BaseModel):
    promotion_type_name: str


class PromotionTypeCreate(PromotionTypeBase):
    pass


class PromotionTypeOut(PromotionTypeBase):
    promotion_type_id: int

    class Config:
        orm_mode = True


class PromotionTypeUpdate(BaseModel):
    promotion_type_name: Optional[str] = None
