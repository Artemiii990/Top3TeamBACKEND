from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware

import models.product

from sqlalchemy import create_engine, String, Integer, MetaData, Table, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session





class Base(DeclarativeBase):
  pass





app = FastAPI(
  title="Apple UA Backend",
  description="API for Apple products",
  version="Alpha: 1.0.0"
)

engine = create_engine("mssql+pyodbc://@localhost\\SQLEXPRESS/AppleUADB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes")

metadata = MetaData()

products = Table(
  "Products",
  metadata,
  autoload_with=engine
)



origins = [
  "http://127.0.0.1:8080"
]

app.add_middleware(
  CORSMiddleware,
  allow_origins=origins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)





@app.get("/products/get", tags=["Products"])
async def get_products():
  with engine.connect() as connection:
    result = connection.execute(select(products))

    return result.mappings().all()



@app.get("/products/get/{product_name}", tags=["Products"])
async def get_product_by_name(product_name: str):
  with engine.connect() as connection:
    product = select(products).where(products.c.ProductName.ilike(f"%{product_name}%"))

    result = connection.execute(product)

    return result.mappings().all()