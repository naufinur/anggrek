import board
import adafruit_dht
import time
import requests  # Library for making HTTP requests

# Set up the DHT11 sensor
dht_pin = board.D4
dht_sensor = adafruit_dht.DHT11(dht_pin)

# Ubidots API settings
UBIDOTS_TOKEN = "BBFF-09pr4oprzQAEerOierTAmyX8FngsYW"  # Replace with your Ubidots token
DEVICE_LABEL = "smart-bengkel"    # Replace with your device label

def send_to_ubidots(temperature, humidity):
    url = "http://industrial.api.ubidots.com/api/v1.6/devices/{device_label}"
    url = url.format(device_label=DEVICE_LABEL)
    headers = {"X-Auth-Token": UBIDOTS_TOKEN, "Content-Type": "application/json"}
    payload = {"temperature": temperature, "humidity": humidity}
    
    response = requests.post(url, json=payload, headers=headers)
    print("Ubidots Response:", response.text)
    response.close()

try:
    while True:
        try:
            temperature = dht_sensor.temperature
            humidity = dht_sensor.humidity
            if temperature is not None and humidity is not None:
                print('Temperature: {:.1f}°C, Humidity: {:.1f}%'.format(temperature, humidity))
                send_to_ubidots(temperature, humidity)  # Send data to Ubidots
                print("Data sent to Ubidots.")
            else:
                print('Data not available.')
        except RuntimeError as e:
            print('Error reading from sensor:', e)

        time.sleep(5)  # Send data every 10 seconds

except KeyboardInterrupt:
    pass