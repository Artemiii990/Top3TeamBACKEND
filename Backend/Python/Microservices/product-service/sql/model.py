from sqlalchemy import *
from sql.database import Base





class Product(Base):
    __tablename__ = "Products"

    Id = Column(Integer, primary_key=True, autoincrement=True)

    ProductName = Column(String(100), unique=True, nullable=False)
    Description = Column(Text)

    ColorsAmount = Column(Integer)
    ColorNames = Column(String(200))

    BatteryHours = Column(Integer)
    BatteryDetails = Column(Text)

    DisplayName = Column(String(50))
    DisplayInches = Column(Float)
    DisplayBrightness = Column(Integer)
    DisplayDetails = Column(Text)

    ExternalDisplaysDetails = Column(Text)

    RAM = Column(Integer)
    RAMDetails = Column(Text)

    Storage = Column(Integer)
    StorageDetails = Column(Text)

    PixelsAmount = Column(Integer)
    ColorsSupported = Column(Integer)

    MaterialsDetails = Column(Text)
    MaterialsNames = Column(Text)

    Chip = Column(String(50))
    ChipDetails = Column(Text)

    CameraResolution = Column(String(50))
    CameraDetails = Column(Text)

    SpeakersAmount = Column(Integer)

    AudioPlayback = Column(Text)
    AudioDetails = Column(Text)

    VideoPlayback = Column(Text)

    Ports = Column(String(100))
    PortsAmount = Column(Integer)

    CablesAmount = Column(Integer)
    CablesDescription = Column(Text)

    DimensionsDetails = Column(Text)

    EnviromentalRequirementsDetails = Column(Text)

    KeyboardAndTrackpadDetails = Column(Text)

    WirelessCommunicationDetails = Column(Text)

    AppleIntelligence = Column(Boolean)

    AppleIntelligenceDetails = Column(Text)

    DownloadedApps = Column(Text)

    OperatingSystem = Column(String(20))

    DolbyAtmos = Column(Boolean)

    Handoff = Column(Boolean)

    InstantHotspot = Column(Boolean)

    TouchID = Column(Boolean)

    AvailabilityDetails = Column(Text)

    KitComponents = Column(Text)