import os

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, ForeignKey, DateTime

from databases import Database

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

products = Table(
    'products', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('price', Float)
)

stores = Table(
    'stores', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('location', String(100))
)

customers = Table(
    'customers', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('address', String(100)),
    Column('vat', String(50)),
    Column('code', String(50)),
    Column('gender_id', Integer),
    Column('customer_type', String(50))
)

salespersons = Table(
    'salespersons', metadata,
    Column('id', Integer, primary_key=True),
    Column('max_discount', Float),
    Column('store_id', Integer, ForeignKey('stores.id'))
)

sales = Table(
    'sales', metadata,
    Column('id', Integer, primary_key=True),
    Column('date', DateTime),
    Column('store_id', Integer, ForeignKey('stores.id')),
    Column('salesperson_id', Integer, ForeignKey('salespersons.id')),
    Column('customer_id', Integer, ForeignKey('customers.id'))
)

saledetails = Table(
    'saledetails', metadata,
    Column('id', Integer, primary_key=True),
    Column('product_id', Integer, ForeignKey('products.id')),
    Column('sale_id', Integer, ForeignKey('sales.id')),
    Column('promotion_id', Integer, ForeignKey('promotions.id')),
    Column('quantity', Integer),
    Column('final_price', Float)
)

promotions = Table(
    'promotions', metadata,
    Column('id', Integer, primary_key=True),
    Column('type_id', Integer, ForeignKey('promotiontypes.id')),
    Column('start_date', DateTime),
    Column('end_date', DateTime)
)

promotiontypes = Table(
    'promotiontypes', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50))
)

database = Database(DATABASE_URI)
