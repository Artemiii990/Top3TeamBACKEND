from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from Backend.Python.Monolith.routers.authentication_router import authentication_router
from Backend.Python.Monolith.routers.product_router import product_router





app = FastAPI(
  title="Apple UA Backend",
  description="API for Apple products",
  version="Alpha: 1.0.0"
)

app.include_router(authentication_router)
app.include_router(product_router)


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