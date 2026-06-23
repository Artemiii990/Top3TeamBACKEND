from fastapi import Depends, APIRouter, HTTPException, status

from dtos.products.product_user_response import *
from services.authentication import get_current_admin

from sqlalchemy import select, update

from sql.database import engine
from sql.tables import products

from models.product import UpdateProduct





product_router = APIRouter()





# ========== Admin =========

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



@product_router.patch("/admin/products/update/{product_name}", tags=["Admin"], dependencies=[Depends(get_current_admin)])
async def update_product_by_name(product_name: str, update_data: UpdateProduct):
  with engine.connect() as connection:
    product = connection.execute(
      select(products).where(products.c.ProductName == product_name)
    ).mappings().first()


    if product is None:
      raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product {product_name} does not exist",
      )
    

    fields_to_update = update_data.model_dump(exclude_unset=True)

    if not fields_to_update:
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail="No fields provided for update",
      )
    

    connection.execute(
      update(products)
      .where(products.c.ProductName == product_name)
      .values(**fields_to_update)
    )

    connection.commit()

    return {"message": f"Product {product_name} updated successfully"}





# ========== User ==========

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