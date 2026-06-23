from pydantic import BaseModel



class Product(BaseModel):
  Id: int

  ProductName: str
  Description: str

  ColorsAmount: int
  ColorNames: str

  BatteryHours: int
  BatteryDetails: str

  DisplayName: str
  DisplayInches: float
  DisplayBrightness: int
  DisplayDetails: str

  ExternalDisplaysDetails: str

  RAM: int
  RAMDetails: str

  Storage: int
  StorageDetails: str

  PixelsAmount: int
  ColorsSupported: int

  MaterialsDetails: str
  MaterialsNames: str

  Chip: str
  ChipDetails: str

  CameraResolution: str
  CameraDetails: str

  SpeakersAmount: int

  AudioPlayback: str
  AudioDetails: str

  VideoPlayback: str

  Ports: str
  PortsAmount: int

  CablesAmount: int
  CablesDescription: str

  DimensionsDetails: str

  EnviromentalRequirementsDetails: str

  KeyboardAndTrackpadDetails: str

  WirelessCommunicationDetails: str

  AppleIntelligence: bool
  AppleIntelligenceDetails: str

  DownloadedApps: str
  OperatingSystem: str

  DolbyAtmos: bool
  Handoff: bool
  InstantHotspot: bool
  TouchID: bool

  AvailabilityDetails: str
  KitComponents: str