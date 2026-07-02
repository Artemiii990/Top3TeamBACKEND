from fastapi import FastAPI, Request
import httpx





app = FastAPI(title="API Gateway")


SERVICES = {
  "authentication-service": "http://localhost:8001",
  "product-service": "http://localhost:8002",
  "user-service": "http://localhost:8003"
}



@app.post("/gateway/login")
async def login(request: Request):
  body = await request.json()

  async with httpx.AsyncClient() as client:
    return await client.post(f"{SERVICES['authentication-service']}/authentication-service/login")



@app.get("/products")
async def products(request:Request):
  # to-do
  #
  #