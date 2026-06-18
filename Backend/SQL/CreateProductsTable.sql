CREATE DATABASE AppleUADB;
GO


USE AppleUADB


CREATE TABLE Products
(
    Id INT IDENTITY(1,1) PRIMARY KEY,

    ProductName NVARCHAR(100) NOT NULL,
    Description NVARCHAR(MAX) NULL,

    ColorsAmount INT NOT NULL,
    ColorNames NVARCHAR(200) NOT NULL,

    BatteryHours INT NOT NULL,
    BatteryDetails NVARCHAR(MAX) NOT NULL,

    DisplayName NVARCHAR(50) NULL,
    DisplayInches DECIMAL(3,1) NOT NULL,
    DisplayBrightness INT NOT NULL,
    DisplayDetails NVARCHAR(MAX) NOT NULL,

    ExternalDisplaysDetails NVARCHAR(MAX) NULL,

    RAM INT NOT NULL,
    RAMDetails NVARCHAR(MAX) NOT NULL,

    Storage INT NOT NULL,
    StorageDetails NVARCHAR(MAX) NOT NULL,

    PixelsAmount INT NOT NULL,
    ColorsSupported INT NULL,

    MaterialsDetails NVARCHAR(MAX) NOT NULL,
    MaterialsNames NVARCHAR(MAX) NOT NULL,

    Chip NVARCHAR(50) NOT NULL,
    ChipDetails NVARCHAR(MAX) NULL,

    CameraResolution NVARCHAR(50) NOT NULL,
    CameraDetails NVARCHAR(MAX) NOT NULL,

    SpeakersAmount INT NOT NULL,

    AudioPlayback NVARCHAR(MAX) NULL,
    AudioDetails NVARCHAR(MAX) NULL,

    VideoPlayback NVARCHAR(MAX) NULL,

    Ports NVARCHAR(100) NOT NULL,
    PortsAmount INT NOT NULL,

    CablesAmount INT NULL,
    CablesDescription NVARCHAR(MAX) NULL,

    DimensionsDetails NVARCHAR(MAX) NULL,
    EnviromentalRequirementsDetails NVARCHAR(MAX) NULL,

    KeyboardAndTrackpadDetails NVARCHAR(MAX) NULL,

    WirelessCommunicationDetails NVARCHAR(MAX) NULL,


    AppleIntelligence BIT NULL,
    AppleIntelligenceDetails NVARCHAR(MAX) NULL,

    DownloadedApps NVARCHAR(MAX) NOT NULL,
    OperatingSystem NVARCHAR(20) NOT NULL,

    DolbyAtmos BIT NULL,
    Handoff BIT NULL,
    InstantHotspot BIT NULL,
    TouchID BIT NULL,


    AvailabilityDetails NVARCHAR(MAX) NULL,
    KitComponents NVARCHAR(MAX) NULL
);