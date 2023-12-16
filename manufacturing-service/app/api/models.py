from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


# Base models for common attributes
class ProductBase(BaseModel):
    name: str
    price: float


class StoreBase(BaseModel):
    name: str
    area: float
    country: str
    city: str
    address: str
    store_type_id: int


class CustomerBase(BaseModel):
    name: str
    address: str
    vat: str
    code: str
    gender_id: int
    customer_type: str


class SalespersonBase(BaseModel):
    max_discount: float
    store_id: int


class SaleBase(BaseModel):
    date: datetime
    store_id: int
    salesperson_id: int
    customer_id: int


class SaleDetailsBase(BaseModel):
    product_id: int
    sale_id: int
    promotion_id: Optional[int] = None
    quantity: int
    final_price: float


class PromotionBase(BaseModel):
    type_id: int
    start_date: datetime
    end_date: datetime


class PromotionTypeBase(BaseModel):
    name: str


# Models for creating new entries
class ProductCreate(ProductBase):
    pass


class StoreCreate(StoreBase):
    pass


class CustomerCreate(CustomerBase):
    pass


class SalespersonCreate(SalespersonBase):
    pass


class SaleCreate(SaleBase):
    pass


class SaleDetailsCreate(SaleDetailsBase):
    pass


class PromotionCreate(PromotionBase):
    pass


class PromotionTypeCreate(PromotionTypeBase):
    pass


# Models for outputting existing entries with ID
class ProductOut(ProductBase):
    id: int

    class Config:
        orm_mode = True


class StoreOut(StoreBase):
    id: int

    class Config:
        orm_mode = True


class CustomerOut(CustomerBase):
    id: int

    class Config:
        orm_mode = True


class SalespersonOut(SalespersonBase):
    id: int

    class Config:
        orm_mode = True


class SaleOut(SaleBase):
    id: int

    class Config:
        orm_mode = True


class SaleDetailsOut(SaleDetailsBase):
    id: int

    class Config:
        orm_mode = True


class PromotionOut(PromotionBase):
    id: int

    class Config:
        orm_mode = True


class PromotionTypeOut(PromotionTypeBase):
    id: int

    class Config:
        orm_mode = True


# Models for updating existing entries
class ProductUpdate(ProductBase):
    name: Optional[str] = None
    price: Optional[float] = None


class StoreUpdate(StoreBase):
    name: Optional[str] = None
    area: Optional[float] = None
    country: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None
    store_type_id: Optional[int] = None


class CustomerUpdate(CustomerBase):
    name: Optional[str] = None
    address: Optional[str] = None
    vat: Optional[str] = None
    code: Optional[str] = None
    gender_id: Optional[int] = None
    customer_type: Optional[str] = None


class SalespersonUpdate(SalespersonBase):
    max_discount: Optional[float] = None
    store_id: Optional[int] = None


class SaleUpdate(SaleBase):
    date: Optional[datetime] = None
    store_id: Optional[int] = None
    salesperson_id: Optional[int] = None
    customer_id: Optional[int] = None


class SaleDetailsUpdate(SaleDetailsBase):
    product_id: Optional[int] = None
    sale_id: Optional[int] = None
    promotion_id: Optional[int] = None
    quantity: Optional[int] = None
    final_price: Optional[float] = None


class PromotionUpdate(PromotionBase):
    type_id: Optional[int] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class PromotionTypeUpdate(PromotionTypeBase):
    name: Optional[str] = None


class ProductIn(BaseModel):
    name: str
    price: float
    # Add any other fields that are required for creating a product


class InventoryIn(BaseModel):
    item_name: str
    quantity: int
    price_per_unit: float


class InventoryOut(BaseModel):
    id: int
    item_name: str
    quantity: int
    price_per_unit: float


class InventoryUpdate(BaseModel):
    item_name: Optional[str]
    quantity: Optional[int]
    price_per_unit: Optional[float]


class SaleIn(BaseModel):
    product_id: int
    quantity: int
    date: datetime
    customer_id: int


class StoreIn(BaseModel):
    pass


class CustomerIn(BaseModel):
    pass


class SalespersonIn(BaseModel):
    pass


class SaleDetailsIn(BaseModel):
    pass


class PromotionIn(BaseModel):
    pass


class PromotionTypeIn(BaseModel):
    pass
