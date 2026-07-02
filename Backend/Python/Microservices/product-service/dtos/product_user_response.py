from pydantic import BaseModel, ConfigDict



class ProductUserResponse(BaseModel):
  model_config = ConfigDict(from_attributes=True)

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