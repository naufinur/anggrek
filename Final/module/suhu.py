
import adafruit_dht
import time
import board

# Set up the DHT11 sensor
dht_pin = 18
dht_sensor = adafruit_dht.DHT11(board.D18)

# import psutil

# # We first check if a libgpiod process is running. If yes, we kill it!
# for proc in psutil.process_iter():
#     if proc.name() == 'libgpiod_pulsein' or proc.name() == 'libgpiod_pulsei':
#         proc.kill()

def sensordht11():
    temperature = dht_sensor.temperature
    humidity = dht_sensor.humidity
    if temperature is not None and humidity is not None:
        print('Temperature: {:.1f}°C, Humidity: {:.1f}%'.format(temperature, humidity))
        return temperature, humidity
    else:
        return None, None

#testing
# while True:
#      temperature, humidity = sensordht11()
#      time.sleep(1)

            
    

