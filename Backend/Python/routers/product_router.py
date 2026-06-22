from fastapi import Depends, APIRouter

from dtos.products.product_user_response import *
from services.authentication import get_current_admin

from sqlalchemy import select

from sql.database import engine
from sql.tables import products





product_router = APIRouter()





@product_router.get("/admin/products/get", tags=["Admin"], dependencies=[Depends(get_current_admin)])
async def get_products_admin():
  with engine.connect() as connection:
    result = connection.execute(select(products))

    return result.mappings().all()



@product_router.get("/admin/products/get/{product_name}", tags=["Admin"], dependencies=[Depends(get_current_admin)])
async def get_product_by_name_admin(product_name: str):
  with engine.connect() as connection:
    product = select(products).where(products.c.ProductName.ilike(f"%{product_name}%"))

    result = connection.execute(product)

    return result.mappings().all()





@product_router.get("/user/products/get", response_model=list[ProductUserResponse], tags=["User"])
async def get_products_user():
  with engine.connect() as connection:
    result = connection.execute(select(products))

    return result.mappings().all()



@product_router.get("/user/products/get/{product_name}", response_model=list[ProductUserResponse], tags=["User"])
async def get_product_by_name_user(product_name: str):
  with engine.connect() as connection:
    product = select(products).where(products.c.ProductName.ilike(f"%{product_name}%"))

    result = connection.execute(product)

    return result.mappings().all()