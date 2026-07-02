from fastapi import FastAPI, HTTPException, status
import httpx





app = FastAPI(title="User Service")


AUTHENTICATION_SERVICE_URL = "http://authentication-service:8000"




@app.get("/user-service/admin/users")
async def get_users():
  async with httpx.AsyncClient() as client:
    try:
      response = await client.get(f"{AUTHENTICATION_SERVICE_URL}/authentication-service/users")
    except httpx.ConnectError:
      raise HTTPException(status_code=status.HTTP_503_SERVICE_UNAVAILABLE, detail="Authentication| service unavailable")


  if response.status_code != status.HTTP_200_OK:
    raise HTTPException(response.status_code, response.text)


  return response.json()



@app.get("/user-service/admin/users/{username}")
async def get_user(username: str):
  async with httpx.AsyncClient() as client:
    response = await client.get(f"{AUTHENTICATION_SERVICE_URL}/authentication-service/users/{username}")


  if response.status_code == status.HTTP_404_NOT_FOUND:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")

  if response.status_code != status.HTTP_200_OK:
    raise HTTPException(status_code=status.HTTP_200_OK, detail="Auth service error")


  return response.json()