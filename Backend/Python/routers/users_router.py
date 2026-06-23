from fastapi import Depends, APIRouter

from dtos.products.product_user_response import *
from services.authentication import get_current_admin

from sqlalchemy import select

from sql.database import engine
from sql.tables import users





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