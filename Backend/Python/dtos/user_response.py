from pydantic import BaseModel
from typing import Annotated
from fastapi import Form



class ProductUserResponse(BaseModel):
  ProductName: str
  Description: str

  ColorsAmount: int
  ColorNames: str

  BatteryHours: int

  DisplayInches: float
  DisplayBrightness: int

  RAM: int
  Storage: int

  Chip: str

  TouchID: bool

  AppleIntelligence: bool