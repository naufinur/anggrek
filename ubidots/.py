import RPi.GPIO as GPIO
import time
import requests

# Mengatur mode GPIO
GPIO.setmode(GPIO.BOARD)

# Definisikan pin trig dan echo
TRIG_PIN = 13
ECHO_PIN = 11

# Mengatur pin sebagai output dan input
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

# Konfigurasi Ubidots
TOKEN = "BBFF-a88d181b90a79a2b9c708fa9a1c88b4a29b"
DEVICE_LABEL = "demo"
VARIABLE_LABEL = "Demo"

# URL Ubidots untuk mengirim data
url = "http://industrial.api.ubidots.com/api/v1.6/devices/{device_label}/{variable_label}/values".format(
    device_label=DEVICE_LABEL,
    variable_label=VARIABLE_LABEL
)

def measure_distance():
    # Mengirimkan sinyal ultrasonik
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.0001)
    GPIO.output(TRIG_PIN, False)

    # Menunggu hingga pin echo menjadi HIGH
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()

    # Menunggu hingga pin echo menjadi LOW
    while GPIO.input(ECHO_PIN) == 1:
        pulse_end = time.time()

    # Menghitung durasi pulsa
    pulse_duration = pulse_end - pulse_start

    # Menghitung jarak berdasarkan kecepatan suara
    speed_of_sound = 34300  # Kecepatan suara dalam cm/s
    distance = pulse_duration * speed_of_sound / 2

    return distance

try:
    while True:
        # Mengukur jarak
        distance = measure_distance()

        # Menampilkan hasil
        print("Jarak: %.2f cm" % distance)

        # Membuat payload data
        payload = {
            "value": distance
        }

        # Mengirim data ke Ubidots
        headers = {"Content-Type": "application/json", "X-Auth-Token": TOKEN}
        response = requests.post(url, headers=headers, json=payload)

        # Memeriksa status respon
        if response.status_code == 201:
            print("Data berhasil dikirim ke Ubidots")
        else:
            print("Terjadi kesalahan saat mengirim data ke Ubidots")

        # Delay sebelum pengukuran berikutnya
        time.sleep(0.1)

except KeyboardInterrupt:
    # Mematikan GPIO
    GPIO.cleanup()