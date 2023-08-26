import serial
import requests
from struct import unpack
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 9600)  # Ganti dengan port serial yang sesuai
UBIDOTS_TOKEN = "BBFF-09pr4oprzQAEerOierTAmyX8FngsYW"  # Ganti dengan token Ubidots Anda
CO2_VARIABLE_LABEL = "dataco2"  # Ganti dengan label variabel CO2 di Ubidots                                                                                                                                                                                                                      "  # Ganti dengan label variabel CO2 di Ubidots
TVOC_VARIABLE_LABEL = "datatvoc(sensorco2)"  # Ganti dengan label variabel TVOC di Ubidots
DEVICE_LABEL = "smart-bengkel"

data_received_count = 0

def send_data_to_ubidots(variable_label, value):
    url = f"https://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}"
    headers = {"Content-Type": "application/json", "X-Auth-Token": UBIDOTS_TOKEN}
    payload = {
        variable_label: value
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print(f"Failed to send data {variable_label} to Ubidots")
    else:
        print(f"Data {variable_label} sent to Ubidots successfully!")

while True:
    dataRaw = ser.read(4)  # Ubah ukuran data yang dibaca sesuai format data sensor
    receivedCO2, receivedTVOC = unpack("hh", dataRaw)  # Menggunakan format "hh" untuk dua nilai short
    
    data_received_count += 1
    
    print(f"Received CO2 Data: {receivedCO2} ppm")
    print(f"Received TVOC Data: {receivedTVOC} ppb")
    print(f"Data Received Count: {data_received_count}")
    print("==============================================")

    # Kirim data CO2 dan TVOC ke Ubidots
    send_data_to_ubidots(CO2_VARIABLE_LABEL, receivedCO2)
    send_data_to_ubidots(TVOC_VARIABLE_LABEL, receivedTVOC)

    sleep(1)