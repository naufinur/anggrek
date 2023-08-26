import requests

# Ubidots API URL dan Token
UBIDOTS_URL = "https://industrial.api.ubidots.com/api/v1.6/devices/smart-bengkel/{variable_label}"
TOKEN = "BBFF-09pr4oprzQAEerOierTAmyX8FngsYW"
DEVICE_LABEL = "smart-bengkel"    # Replace with your device label

#menerima data toogle kipas
def menerima_data(kipas_label): #seharusnya sudah benar 
    headers = {"X-Auth-Token":TOKEN, "Content-Type": "application/json"}
    url = UBIDOTS_URL.format(variable_label=kipas_label)
    response = requests.get(url, headers=headers)
    data = response.json()
    last_value = data.get("last_value", None)
    if last_value and "value" in last_value:
        value = last_value["value"]
        return value
    else:
        print("Data tidak lengkap atau tidak ada nilai (value) yang diterima.")
        return None

def send_data_to_ubidots(variable_label, value):
    url = f"https://industrial.api.ubidots.com/api/v1.6/devices/{DEVICE_LABEL}"
    headers = {"Content-Type": "application/json", "X-Auth-Token": TOKEN}
    payload = {
        variable_label: value
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 201:
        print(f"Failed to send data {variable_label} to Ubidots")
    else:
        print(f"Data {variable_label} sent to Ubidots successfully!")


# import time
# while True:
    # kipas1 = menerima_data("tombol1")
    # print('kipas1: ', kipas1)
    # kipas2 = menerima_data("tombol2")
    # print('kipas2: ', kipas2)
    # kipas3 = menerima_data("tombol3")
    # print('kipas3: ', kipas3)
    # kipas4 = menerima_data("tombol4")
    # print('kipas4: ', kipas4)
    # otomatis = menerima_data("tombol_otomatis")
    # print('otomatis: ', otomatis)
    # print('-----------')

#     time.sleep(1)