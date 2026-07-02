from fastapi import Depends, APIRouter

from Backend.Python.Monolith.dtos.products.product_user_response import *
from Backend.Python.Monolith.services.authentication import get_current_admin

from sqlalchemy import select

from Backend.Python.Monolith.sql.database import engine
from Backend.Python.Monolith.sql.tables import users





users_router = APIRouter()





@users_router.get("/admin/users/get", tags=["Admin"], dependencies=[Depends(get_current_admin)])
async def get_admins():
  with engine.connect() as connection:
    result = connection.execute(select(users))

    return result.mappings().all()



@users_router.get("/admin/users/{user_name}", tags=["Admin"], dependencies=[Depends(get_current_admin)])
async def get_admin_by_name(user_name):
  with engine.connect() as connection:
    user = connection.execute(select(users).where(users.c.Username == user_name)).mappings().first()

    return user