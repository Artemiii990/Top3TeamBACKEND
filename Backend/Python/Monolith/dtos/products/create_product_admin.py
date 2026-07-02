from pydantic import BaseModel, Field



class CreateProduct(BaseModel):
  ProductName: str = Field(..., max_length = 100)
  Description: str | None = None

  ColorsAmount: int
  ColorNames: str = Field(..., max_length = 200)

  BatteryHours: int
  BatteryDetails: str

  DisplayName: str | None = Field(None, max_length = 50)
  DisplayInches: float = Field(..., ge = 0, le = 99.9)
  DisplayBrightness: int
  DisplayDetails: str

  ExternalDisplaysDetails: str | None = None

  RAM: int
  RAMDetails: str

  Storage: int
  StorageDetails: str

  PixelsAmount: int
  ColorsSupported: int | None = None

  MaterialsDetails: str
  MaterialsNames: str

  Chip: str = Field(..., max_length = 50)
  ChipDetails: str | None = None

  CameraResolution: str = Field(..., max_length = 50)
  CameraDetails: str

  SpeakersAmount: int

  AudioPlayback: str | None = None
  AudioDetails: str | None = None

  VideoPlayback: str | None = None

  Ports: str = Field(..., max_length = 100)
  PortsAmount: int

  CablesAmount: int | None = None
  CablesDescription: str | None = None

  DimensionsDetails: str | None = None
  EnviromentalRequirementsDetails: str | None = None

  KeyboardAndTrackpadDetails: str | None = None
  WirelessCommunicationDetails: str | None = None

  AppleIntelligence: bool | None = None
  AppleIntelligenceDetails: str | None = None

  DownloadedApps: str
  OperatingSystem: str = Field(..., max_length = 20)

  DolbyAtmos: bool | None = None
  Handoff: bool | None = None
  InstantHotspot: bool | None = None
  TouchID: bool | None = None

  AvailabilityDetails: str | None = None
  KitComponents: str | None = None