from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import httpx





app = FastAPI(title="Product Service")

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



@app.get("/product-service/products")
async def get_products(username: str = Depends(get_current_admin)):
  # to-do
  #
  #
  return {"message": f"products for {username}"}