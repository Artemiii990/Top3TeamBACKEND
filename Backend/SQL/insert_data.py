import json
import os, sys
import re

BACKEND = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BACKEND)

from Python.sql.database import engine
from Python.sql.tables import products

from sqlalchemy import select





# functions
def load_json(path: str) -> dict:
  with open(path, encoding="utf-8") as file:
    return json.load(file)
  
def json_to_str(data) -> str:
  return json.dumps(data, ensure_ascii=False)

def extract_int(text: str) -> int | None:
  match = re.search(r"\d+", str(text).replace("\xa0", "").replace("\u202f", ""))
  return int(match.group()) if match else None

def extract_inches(text: str) -> float | None:
  match = re.search(r"(\d+[,.]\d+)\s*дюйм", text)
  return float(match.group(1).replace(",", ".")) if match else None

def extract_pixels(text: str) -> int:
  match = re.search(r"(\d{3,})[×xх](\d{3,})", text)
  return int(match.group(1)) * int(match.group(2)) if match else 0



# path
base_dir = os.path.dirname(os.path.abspath(__file__))

hardware = os.path.join(base_dir, "ProductDetails", "HardwareDetails")
hardware_battery = os.path.join(hardware, "Battery")
hardware_display = os.path.join(hardware, "Display")
hardware_memory = os.path.join(hardware, "Memory")
hardware_playback = os.path.join(hardware, "Playback")

software = os.path.join(base_dir, "ProductDetails", "SoftwareDetails")

general = os.path.join(base_dir, "ProductDetails", "GeneralDetails")



# files
chip_data = load_json(os.path.join(hardware, "ChipDetails.json"))
display_data = load_json(os.path.join(hardware_display, "DisplayDetails.json"))
ram_data = load_json(os.path.join(hardware_memory, "RAMDetails.json"))
storage_data = load_json(os.path.join(hardware_memory, "StorageDetails.json"))

audio_data = load_json(os.path.join(hardware, "AudioDetails.json"))
ports_data = load_json(os.path.join(hardware_battery, "ChargingAndConnection.json"))
keyboard_data = load_json(os.path.join(hardware, "KeyboardAndTrackpadDetails.json"))
wireless_data = load_json(os.path.join(hardware, "WirelessCommunicationDetails.json"))
external_displays_data = load_json(os.path.join(hardware_display, "ExternalDisplaysDetails.json"))

battery_data = load_json(os.path.join(hardware_battery, "BatteryDetails.json"))
dimensions_data = load_json(os.path.join(general, "DimensionsAndWeightDetails.json"))
enviromental_data = load_json(os.path.join(general, "EnviromentalRequirementsDetails.json"))
functions_data = load_json(os.path.join(software, "FunctionsDetails.json"))
description_data = load_json(os.path.join(general, "Description.json"))
availability_data = load_json(os.path.join(general, "AvailabilityDetails.json"))
kit_data = load_json(os.path.join(general, "KitComponentsDetails.json"))
color_data = load_json(os.path.join(general, "ColorsDetails.json"))
materials_data = load_json(os.path.join(general, "MaterialDetails.json"))
camera_data = load_json(os.path.join(hardware, "CameraDetails.json"))

audio_playback_data = load_json(os.path.join(hardware_playback, "AudioPlayback.json"))
video_playback_data = load_json(os.path.join(hardware_playback, "VideoPlayback.json"))
ai_data = load_json(os.path.join(software, "AppleIntelligenceDetails.json"))
apps_data = load_json(os.path.join(software, "DownloadedAppsDetails.json"))
os_data = load_json(os.path.join(software, "OperatingSystemDetails.json"))

images_data = load_json(os.path.join(base_dir, "ProductDetails", "Images.json"))
product_configs = load_json(os.path.join(base_dir, "ProductDetails", "ProductConfig.json"))



def seed_product(product_key: str):
  config = product_configs[product_key]
  images = json_to_str(images_data[product_key])


  # chip
  chip_name = config["chip"]
  chip_info = chip_data[chip_name]
  chip_details = json_to_str(chip_info)


  # battery
  battery_info = battery_data[product_key]
  battery_hours = extract_int(battery_info["broadcastingTime"])
  battery_details = json_to_str(battery_info)
  cables_amount = 1
  cables_description = battery_info.get("chargingCable", "")


  # display
  display_name = config["display"]
  display_info = display_data[display_name]
  display_details = json_to_str(display_info)
  display_inches = extract_inches(display_info["diagonal"])
  display_brightness = extract_int(display_info["brightness"])
  pixels_amount = extract_pixels(display_info["diagonal"])

  colors_supported = 1_000_000_000

  external_displays_details = json_to_str(external_displays_data)


  # memory
  ram_key = config["ram"]
  ram = extract_int(ram_key)
  ram_details = json_to_str(ram_data[ram_key])

  storage_key = config["storage"]
  storage = extract_int(storage_key)
  storage_details = json_to_str(storage_data[storage_key])


  # camera
  camera_resolution = config["cameraResolution"]
  camera_details = json_to_str(camera_data[product_key])


  # audio
  product_audio = audio_data[product_key]
  speakers_key = next(s for s in product_audio if re.match(r'^\d+\s', s))
  speakers_amount = extract_int(speakers_key)
  audio_details = json_to_str(product_audio)
  audio_playback = json_to_str(audio_playback_data)
  dolby_atmos = "Dolby Atmos" in product_audio


  # video
  video_playback = json_to_str(video_playback_data)


  # ports
  product_ports = ports_data[product_key]
  ports_amount = len(product_ports)
  ports = ", ".join(product_ports.keys())


  # dimentions & enviroment
  dimensions_details = json_to_str(dimensions_data[product_key])
  enviroment_details = json_to_str(enviromental_data[product_key])


  # keyboard & trackpad
  product_keyboard = keyboard_data[product_key]
  keyboard_details = json_to_str(product_keyboard)

  touch_id = any(
    keyboard.get("touchId")
    for keyboard in keyboard_data.values()
    if isinstance(keyboard, dict)
  )


  # wireless
  wireless_details = json_to_str(wireless_data[product_key])


  # availability & kit
  availability_details = json_to_str(availability_data[product_key])
  kit_components = json_to_str(kit_data[product_key])


  # apps & OS
  downloaded_apps = ", ".join(apps_data["default"])
  operating_system = next(iter(os_data.keys()))


  # apple intelligence
  ai_key, ai_description = next(iter(ai_data.items()))
  apple_intelligence = 1
  apple_intelligence_details = ai_description


  # colors & materials & description
  colors_amount = len(color_data[product_key])
  colors_names = ", ".join(color_data[product_key])
  materials_details = json_to_str(materials_data[product_key])
  materials_names = json_to_str(materials_data[product_key]["names"])
  description = description_data[product_key]


  # functions (продукт-кейед)
  func = functions_data[product_key]
  handoff = bool(func.get("handoff"))
  instant_hotspot = bool(func.get("instantHotspot"))



  # insert
  with engine.begin() as connection:
    exists = connection.execute(
      select(products.c.ProductName)
      .where(products.c.ProductName == product_key)
    ).first()
  

    if exists:
      print(f"Product '{product_key}' already exists")
      return
    
    
    connection.execute(
      products.insert().values(
        ProductName = product_key,
        Description = description,

        ColorsAmount = colors_amount,
        ColorNames = colors_names,

        BatteryHours = battery_hours,
        BatteryDetails = battery_details,

        DisplayName = display_name,
        DisplayInches = display_inches,
        DisplayBrightness = display_brightness,
        DisplayDetails = display_details,
        ExternalDisplaysDetails = external_displays_details,

        RAM = ram,
        RAMDetails = ram_details,

        Storage = storage,
        StorageDetails = storage_details,

        PixelsAmount = pixels_amount,
        ColorsSupported = colors_supported,

        MaterialsDetails = materials_details,
        MaterialsNames = materials_names,

        Chip = chip_name,
        ChipDetails = chip_details,

        CameraResolution = camera_resolution,
        CameraDetails = camera_details,

        SpeakersAmount = speakers_amount,

        AudioPlayback = audio_playback,
        AudioDetails = audio_details,

        VideoPlayback = video_playback,

        Ports = ports,
        PortsAmount = ports_amount,

        CablesAmount = cables_amount,
        CablesDescription = cables_description,

        DimensionsDetails = dimensions_details,
        EnviromentalRequirementsDetails = enviroment_details,

        KeyboardAndTrackpadDetails = keyboard_details,

        WirelessCommunicationDetails = wireless_details,

        AppleIntelligence = apple_intelligence,
        AppleIntelligenceDetails = apple_intelligence_details,

        DownloadedApps = downloaded_apps,
        OperatingSystem = operating_system,

        DolbyAtmos = 1 if dolby_atmos else 0,
        Handoff = handoff,
        InstantHotspot = instant_hotspot,
        TouchID = touch_id,
        
        AvailabilityDetails = availability_details,
        KitComponents = kit_components,

        Images = images
      )
    )
    
    print(f"Product '{product_key}' successfully added to the database")



# execute
for product_key in product_configs:
  seed_product(product_key)