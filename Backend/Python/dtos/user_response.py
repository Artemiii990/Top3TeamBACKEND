from pydantic import BaseModel



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