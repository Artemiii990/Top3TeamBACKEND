# pip install pyodbc
import pyodbc

import json
import os
import re



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



# connection
connection = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS;DATABASE=AppleUADB;Trusted_Connection=YES;")
cursor = connection.cursor()



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
battery_data = load_json(os.path.join(hardware_battery, "BatteryDetails.json"))
display_data = load_json(os.path.join(hardware_display, "DisplayDetails.json"))
external_displays_data = load_json(os.path.join(hardware_display, "ExternalDisplaysDetails.json"))
ram_data = load_json(os.path.join(hardware_memory, "RAMDetails.json"))
storage_data = load_json(os.path.join(hardware_memory, "StorageDetails.json"))
audio_playback_data = load_json(os.path.join(hardware_playback, "AudioPlayback.json"))
video_playback_data = load_json(os.path.join(hardware_playback, "VideoPlayback.json"))
audio_data = load_json(os.path.join(hardware, "AudioDetails.json"))
camera_data = load_json(os.path.join(hardware, "CameraDetails.json"))
ports_data = load_json(os.path.join(hardware_battery, "ChargingAndConnection.json"))
dimensions_data = load_json(os.path.join(hardware, "DimensionsAndWeightDetails.json"))
enviromental_data = load_json(os.path.join(hardware, "EnviromentalRequirementsDetails.json"))
keyboard_data = load_json(os.path.join(hardware, "KeyboardAndTrackpadDetails.json"))
wireless_data = load_json(os.path.join(hardware, "WirelessCommunicationDetails.json"))

ai_data   = load_json(os.path.join(software, "AppleIntelligenceDetails.json"))
apps_data = load_json(os.path.join(software, "DownloadedAppsDetails.json"))
os_data   = load_json(os.path.join(software, "OperatingSystemDetails.json"))
functions_data = load_json(os.path.join(software, "FunctionsDetails.json"))

description_data = load_json(os.path.join(general, "Description.json"))
availability_data = load_json(os.path.join(general, "AvailabilityDetails.json"))
kit_data = load_json(os.path.join(general, "KitComponentsDetails.json"))
color_data = load_json(os.path.join(general, "ColorsDetails.json"))
materials_data = load_json(os.path.join(general, "MaterialDetails.json"))


product_key = "MacBook Neo"



# chip
chip_name, chip_info = next(iter(chip_data.items()))
chip_details = json_to_str(chip_info)


# battery
battery_info = battery_data[product_key]
battery_hours = extract_int(battery_info["broadcastingTime"])
battery_details = json_to_str(battery_info)
cables_amount = 1
cables_description = battery_info.get("chargingCable", "")


# display
display_key, display_info = next(iter(display_data.items()))
 
display_name = display_key
display_details = json_to_str(display_info)
display_inches = extract_inches(display_info["diagonal"])
display_brightness = extract_int(display_info["brightness"])
 
pixels_amount = extract_pixels(display_info["diagonal"])
colors_supported   = 1_000_000_000
 
external_displays_details = json_to_str(external_displays_data)


# memory
ram_key, ram_info = next(iter(ram_data.items()))
ram = extract_int(ram_key)
ram_details = json_to_str(ram_info)

storage_key = next(iter(storage_data.keys()))
storage = extract_int(storage_key)
storage_details = json_to_str(storage_data)


# camera
camera_resolution = next(iter(camera_data.keys()))
camera_details = json_to_str(camera_data)


# audio
speakers_key = next(s for s in audio_data if re.match(r'^\d+\s', s))
speakers_amount = extract_int(speakers_key)
audio_details = json_to_str(audio_data)
audio_playback = json_to_str(audio_playback_data)
dolby_atmos = "Dolby Atmos" in audio_data


# video
video_playback = json_to_str(video_playback_data)


# ports
ports_amount = len(ports_data)
ports = ", ".join(ports_data.keys())


# dimentions & enviroment
dimensions_details = json_to_str(dimensions_data[product_key])
enviroment_details = json_to_str(enviromental_data[product_key])


# keyboard & trackpad
keyboard_details = json_to_str(keyboard_data)

touch_id = any(
  keyboard.get("touchId")
  for keyboard in keyboard_data.values()
  if isinstance(keyboard, dict)
)


# wireless
wireless_details = json_to_str(wireless_data)


# software
availability_details = json_to_str(availability_data[product_key])
kit_components = json_to_str(kit_data[product_key])


# apple intelligence
ai_key, ai_description = next(iter(ai_data.items()))
apple_intelligence = 1
apple_intelligence_details = ai_description


# downloaded apps
downloaded_apps = ", ".join(apps_data["default"])


# operating system
operating_system = next(iter(os_data.keys()))


# colors
colors_amount = len(color_data.get(product_key))
colors_names = " ".join(color_data.get(product_key))


# materials
materials_details = json_to_str(materials_data.get(product_key))
materials_names = json_to_str(materials_data[product_key]["names"])


# description
description = description_data.get(product_key)


# function
handoff = any(
  func.get("handoff")
  for func in functions_data.values()
  if isinstance(func, dict)
)

instant_hotspot = any(
  func.get("instantHotspot")
  for func in functions_data.values()
  if isinstance(func, dict)
)


# product name
product_name = product_key



# insert
cursor.execute("""
    INSERT INTO Products (
        ProductName, Description,
        ColorsAmount, ColorNames,
        BatteryHours, BatteryDetails,
        DisplayName, DisplayInches, DisplayBrightness, DisplayDetails,
        ExternalDisplaysDetails,
        RAM, RAMDetails,
        Storage, StorageDetails,
        PixelsAmount, ColorsSupported,
        MaterialsDetails, MaterialsNames,
        Chip, ChipDetails,
        CameraResolution, CameraDetails,
        SpeakersAmount,
        AudioPlayback, AudioDetails,
        VideoPlayback,
        Ports, PortsAmount,
        CablesAmount, CablesDescription,
        DimensionsDetails,
        EnviromentalRequirementsDetails,
        KeyboardAndTrackpadDetails,
        WirelessCommunicationDetails,
        AppleIntelligence, AppleIntelligenceDetails,
        DownloadedApps, OperatingSystem,
        DolbyAtmos, Handoff, InstantHotspot, TouchID,
        AvailabilityDetails, KitComponents
    ) VALUES (
        ?,?,  ?,?,  ?,?,  ?,?,?,?,  ?,  ?,?,  ?,?,  ?,?,  ?,?,
        ?,?,  ?,?,  ?,  ?,?,  ?,  ?,?,  ?,?,  ?,?,?,?,  ?,?,  ?,?,  ?,?,?,?,  ?,?
    )
""",
    product_name, description,
    colors_amount, colors_names,
    battery_hours, battery_details,
    display_name, display_inches, display_brightness, display_details,
    external_displays_details,
    ram, ram_details,
    storage, storage_details,
    pixels_amount, colors_supported,
    materials_details, materials_names,
    chip_name, chip_details,
    camera_resolution, camera_details,
    speakers_amount,
    audio_playback, audio_details,
    video_playback,
    ports, ports_amount,
    cables_amount, cables_description,
    dimensions_details,
    enviroment_details,
    keyboard_details,
    wireless_details,
    apple_intelligence, apple_intelligence_details,
    downloaded_apps, operating_system,
    1 if dolby_atmos else 0, handoff, instant_hotspot, touch_id,
    availability_details, kit_components
)
 
connection.commit()
connection.close()

print(f"Product '{product_name}' successfully added to the database")