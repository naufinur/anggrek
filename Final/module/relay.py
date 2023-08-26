import RPi.GPIO as GPIO
import time

#bikin module 4 kipas masing2 kipas bisa dimatikan dan dinyalakan secara independen

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

kipas_pin = [17, 22, 23, 24]

for pin in kipas_pin:
   GPIO.setup(pin,GPIO.OUT)

#control 4 kipas 
def kipas(kipas_id, state):
    '''
    jika state = 1 kipas nyala, jika state = 0 kipas mati.
    '''
    pin = kipas_id-1
    #membalikan nilai
    if state == 0:
        nyala = 1
    elif state == 1:
        nyala = 0 
    GPIO.output(kipas_pin[pin], nyala) 
    print(f"kipas {kipas_id} = {state}")
    
# testing 
# while True:
#     kipas(1, 1)
#     kipas(2, 1)
#     kipas(3, 1)
#     kipas(4, 1)
#     time.sleep(1)