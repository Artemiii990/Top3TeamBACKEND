from pydantic import BaseModel



class UpdateProduct(BaseModel):
  ProductName: str | None = None
  Description: str | None = None

  ColorsAmount: int | None = None
  ColorNames: str | None = None

  BatteryHours: int | None = None
  BatteryDetails: str | None = None

  DisplayName: str | None = None
  DisplayInches: float | None = None
  DisplayBrightness: int | None = None
  DisplayDetails: str | None = None

  ExternalDisplaysDetails: str | None = None

  RAM: int | None = None
  RAMDetails: str | None = None

  Storage: int | None = None
  StorageDetails: str | None = None

  PixelsAmount: int | None = None
  ColorsSupported: int | None = None

  MaterialsDetails: str | None = None
  MaterialsNames: str | None = None

  Chip: str | None = None
  ChipDetails: str | None = None

  CameraResolution: str | None = None
  CameraDetails: str | None = None

  SpeakersAmount: int | None = None

  AudioPlayback: str | None = None
  AudioDetails: str | None = None

  VideoPlayback: str | None = None

  Ports: str | None = None
  PortsAmount: int | None = None

  CablesAmount: int | None = None
  CablesDescription: str | None = None

  DimensionsDetails: str | None = None

  EnviromentalRequirementsDetails: str | None = None

  KeyboardAndTrackpadDetails: str | None = None

  WirelessCommunicationDetails: str | None = None

  AppleIntelligence: bool | None = None
  AppleIntelligenceDetails: str | None = None

  DownloadedApps: str | None = None
  OperatingSystem: str | None = None

  DolbyAtmos: bool | None = None
  Handoff: bool | None = None
  InstantHotspot: bool | None = None
  TouchID: bool | None = None

  AvailabilityDetails: str | None = None
  KitComponents: str | None = None