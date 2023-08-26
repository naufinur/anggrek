import RPi.GPIO as GPIO
from time import sleep
import requests

# Konfigurasi Ubidots
TOKEN = "BBFF-09pr4oprzQAEerOierTAmyX8FngsYW"
DEVICE_LABEL = "smart-bengkel"
VARIABLE_LABEL = "tombol"

# URL Ubidots untuk mengirim data
url = "http://industrial.api.ubidots.com/api/v1.6/devices/{device_label}/{variable_label}/values".format(
    device_label=DEVICE_LABEL,
    variable_label=VARIABLE_LABEL
)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

for i in range(5):
  GPIO.output(17,GPIO.HIGH)
  GPIO.output(22,GPIO.HIGH)
  GPIO.output(23,GPIO.HIGH)
  GPIO.output(24,GPIO.HIGH)
  print ("Relay menyala")
  sleep(2)
  GPIO.output(17,GPIO.LOW)
  GPIO.output(22,GPIO.LOW)
  GPIO.output(23,GPIO.LOW)
  GPIO.output(24,GPIO.LOW)
  print ("Relay mati")
  sleep(2)



GPIO.cleanup()
