from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import httpx

from dtos.product_user_response import ProductUserResponse
from dtos.create_product_admin import CreateProduct
from dtos.update_product_admin import UpdateProduct

from sql.database import engine, Base
from sql.model import Product

from sqlalchemy import select
from sqlalchemy.orm import Session, sessionmaker





app = FastAPI(title="Product Service")

Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(
  bind=engine,
  autoflush=False
)

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()


AUTHENTICATION_SERVICE_URL = "http://localhost:8001"

bearer_scheme = HTTPBearer()



async def get_current_admin(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)) -> str:
  async with httpx.AsyncClient() as client:
    try:
      response = await client.post(f"{AUTHENTICATION_SERVICE_URL}/authentication-service/verify", json={"token": credentials.credentials})
    
    except httpx.ConnectError:
      raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Authentication service is unavailable")
    except httpx.TimeoutException:
      raise HTTPException(status_code=status.HTTP_504_GATEWAY_TIMEOUT, detail="Authentication service timeout")
    
  if response.status_code != status.HTTP_200_OK:
    raise HTTPException(status_code=response.status_code, detail=response.json().get("detail", "Authentication failed"))
  

  return response.json()["username"]





# ========== User ==========

@app.get("/product-service/user/get", response_model=list[ProductUserResponse], tags=["User"])
async def get_products_user(db: Session = Depends(get_db)):
  return db.scalars(select(Product)).all()



@app.get("/product-service/user/get/{product_name}", response_model=list[ProductUserResponse], tags=["User"])
async def get_products_user(product_name: str, db: Session = Depends(get_db)):
  return db.scalars(
    select(Product).where(Product.ProductName.ilike(f"%{product_name}%"))
    ).all()





# ========== Admin ==========

@app.get("/product-service/admin/get", dependencies=[Depends(get_current_admin)], tags=["Admin"])
async def get_products_admin(db: Session = Depends(get_db)):
  return db.scalars(select(Product)).all()



@app.get("/product-service/admin/get/{product_name}", dependencies=[Depends(get_current_admin)], tags=["Admin"])
async def get_products_admin(product_name: str, db: Session = Depends(get_db)):
  return db.scalars(
    select(Product).where(Product.ProductName.ilike(f"%{product_name}%"))
    ).all()



@app.post("/product-service/admin/product/create", dependencies=[Depends(get_current_admin)], tags=["Admin"])
async def create_product(create_data: CreateProduct, db: Session = Depends(get_db)):
  exists = db.scalar(
    select(Product).where(Product.ProductName == create_data.ProductName)
  )


  if exists: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Product {create_data.ProductName} already exists")
  
  product = Product(**create_data.model_dump())
  db.add(product)
  db.commit()


  return {"message": f"Product {create_data.ProductName} successfully created"}



@app.patch("/product-service/admin/update/{product_name}", dependencies=[Depends(get_current_admin)], tags=["Admin"])
async def update_product_by_name(product_name: str, update_data: UpdateProduct, db: Session = Depends(get_db)):
  product = db.scalar(select(Product).where(Product.ProductName == product_name))

  if product is None: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product {product_name} was not found")


  for key, value in update_data.model_dump(exclude_unset=True).items():
    setattr(product, key, value)
  
  db.commit()

  return {"message": f"Successfully updated {product_name}"}



@app.delete("/product-service/admin/delete/{product_id}", dependencies=[Depends(get_current_admin)], tags=["Admin"])
async def delete_product_by_id(product_id: int, db: Session = Depends(get_db)):
  product = db.scalar(select(Product).where(Product.Id == product_id))

  if product is None: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product was not found")


  db.delete(product)
  db.commit()


  return {"message": "Product deleted successfully"}