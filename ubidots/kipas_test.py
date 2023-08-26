import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

relay_pin1 = 17
relay_pin2 = 22
relay_pin3 = 23
relay_pin4 = 24

GPIO.setup(relay_pin1,GPIO.OUT)
GPIO.setup(relay_pin2,GPIO.OUT)
GPIO.setup(relay_pin3,GPIO.OUT)
GPIO.setup(relay_pin4,GPIO.OUT)

for i in range(1):
    GPIO.output(relay_pin1, GPIO.LOW)
    print("Kipas 1 lagi nyala")
    time.sleep(1)
    GPIO.output(relay_pin1, GPIO.HIGH)
    print("Kipas 1 sedang mati")
    print("===============================")
    time.sleep(5)
    
    GPIO.output(relay_pin2, GPIO.LOW)
    print("Kipas 2 lagi nyala")
    time.sleep(5)
    GPIO.output(relay_pin2, GPIO.HIGH)
    print("Kipas 2 sedang mati")
    print("===============================")
    time.sleep(5)

    GPIO.output(relay_pin3, GPIO.LOW)
    print("Kipas 3 lagi nyala")
    time.sleep(2)
    GPIO.output(relay_pin3, GPIO.HIGH)
    print("Kipas 3 sedang mati")
    print("===============================")
    time.sleep(2)
    
    GPIO.output(relay_pin4, GPIO.LOW)
    print("Kipas 4 lagi nyala")
    time.sleep(2)
    GPIO.output(relay_pin4, GPIO.HIGH)
    print("Kipas 4 sedang mati")
    print("===============================")
    time.sleep(1)