import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey, DateTime
from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

product = Table(
    'product', metadata,
    Column('product_id', Integer, primary_key=True),
    Column('product_name', String(255)),
    Column('price', Float)
)

store = Table(
    'store', metadata,
    Column('store_id', Integer, primary_key=True),
    Column('store_name', String(255)),
    Column('store_area', String(255)),
    Column('store_country', String(255)),
    Column('store_city', String(255)),
    Column('store_address', String(255)),
    Column('store_type_id', Integer, ForeignKey('store_type.store_type_id'))
)

customer = Table(
    'customer', metadata,
    Column('customer_id', Integer, primary_key=True),
    Column('customer_name', String(255)),
    Column('customer_address', String(255)),
    Column('customer_vat', String(50)),
    Column('customer_code', String(50)),
    Column('gender_id', Integer, ForeignKey('gender.gender_id')),
    Column('customer_type', String(50))
)

salesperson = Table(
    'salesperson', metadata,
    Column('salesperson_id', Integer, primary_key=True),
    Column('max_discount', Float),
    Column('store_id', Integer, ForeignKey('store.store_id'))
)

sale = Table(
    'sale', metadata,
    Column('sale_id', Integer, primary_key=True),
    Column('sale_date', DateTime),
    Column('store_id', Integer, ForeignKey('store.store_id')),
    Column('salesperson_id', Integer, ForeignKey(
        'salesperson.salesperson_id')),
    Column('customer_id', Integer, ForeignKey('customer.customer_id'))
)

sale_detail = Table(
    'sale_detail', metadata,
    Column('sale_detail_id', Integer, primary_key=True),
    Column('product_id', Integer, ForeignKey('product.product_id')),
    Column('sale_id', Integer, ForeignKey('sale.sale_id')),
    Column('promotion_id', Integer, ForeignKey('promotion.promotion_id')),
    Column('quantity', Integer),
    Column('final_price', Float)
)

promotion = Table(
    'promotion', metadata,
    Column('promotion_id', Integer, primary_key=True),
    Column('promo_type_id', Integer, ForeignKey(
        'promotion_type.promo_type_id')),
    Column('promotion_start', DateTime),
    Column('promotion_end', DateTime)
)

promotion_type = Table(
    'promotion_type', metadata,
    Column('promo_type_id', Integer, primary_key=True),
    Column('promotion_type_name', String(50))
)

gender = Table(
    'gender', metadata,
    Column('gender_id', Integer, primary_key=True),
    Column('gender_name', String(50))
)

store_type = Table(
    'store_type', metadata,
    Column('store_type_id', Integer, primary_key=True),
    Column('store_type_name', String(50))
)

product_store = Table(
    'product_store', metadata,
    Column('product_store_id', Integer, primary_key=True),
    Column('product_id', Integer, ForeignKey('product.product_id')),
    Column('store_id', Integer, ForeignKey('store.store_id'))
)

database = Database(DATABASE_URI)
