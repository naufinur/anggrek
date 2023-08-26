# import semua module dulu
# import module co2
from module.co2 import *

#import module relay
from module.relay import *

#import module suhu
from module.suhu import *

#import module ubidots
from module.ubidots import *

#ambil semua data sensor
# data sensor co2

import time
import threading

'''
1. deteksi sensor co2 mendeteksi co2 dan tvoc --> karena terus mnedapatkan data dari arduino sehingga prosesnya harus dipisah
2. deteksi suhu dan kelembapan
3. mengirim data ke ubidots
4. switch antara manual dan otomatis --> dapat kondisi alat jalan ototmatis atau manual
5. jika otomatis --> ambil level temperature dan co2 --> lalu diambil yang palin tinggi
5. nyalakan / matikan kipas sesuai level
7. menerima data dari ubidots
8. jika berjalan manual --> bisa menyalakan kipas secara manual dari aplikai jika kedua kondisi diatas tidak terpenuhi --> manual

temperature  ---> 1 2 3 4 | 0
co2          ---> 1 2 3 4 | 0
misal ==
temperature = 0
co2         = 4
diambil level yg paling tinggi, jadi nanti dianggap level 4.
kipas nyala semua


'''
receivedCO2 = 400
receivedTVOC = 0
temperature, humidity = 0, 0

# ambil sensor co2 dengan threading --> https://realpython.com/intro-to-python-threading/
def ambil_sensor_co2(_):
  global receivedCO2, receivedTVOC
  while True:
    receivedCO2, receivedTVOC = sensorco2()
    time.sleep(1)

def ambil_sensor_suhu(_):
  global temperature, humidity
  while True:
    temperature, humidity = sensordht11() # mendapatkan data sensor suhu dan kelembapan
    time.sleep(1)

# bikin def main --> program utama
def main(): # program utama, semua program berjalan disini
    global receivedCO2, receivedTVOC, temperature, humidity
    
    # 1. deteksi sensor co2 mendeteksi co2 dan tvoc --> diluar proses ini

    # 2. deteksi suhu dan kelembapan
    # temperature, humidity = sensordht11() # mendapatkan data sensor suhu dan kelembapan

    # 3. mengirim data ke ubidots
    # mengirim data suhu
    send_data_to_ubidots("Temperature", temperature)
    send_data_to_ubidots("Humidity", humidity)
    send_data_to_ubidots("dataco2", receivedCO2)
    send_data_to_ubidots("datatvoc", receivedTVOC)

    # ambil data tombol_otomatis
    otomatis = menerima_data("tombol_otomatis")
    
    # jika otomatis
    if otomatis:
      print("mode otomatis")
      # 3. kalau suhu terlalu panas kipas nyala --> otomatis
      level_temperature = 0
      level_co2 = 0
      if ( temperature > 30 ): # nyalain 1 kipas
        level_temperature = 1
        
      elif ( temperature > 31 ): # nyalain 2 kipas
        level_temperature = 2

      elif ( temperature > 32 ): # nyalain 3 kipas
        level_temperature = 3

      elif ( temperature > 33 ): # nyalain 4 kipas
        level_temperature = 4
        
      else:
        level_temperature = 0

      # 4. kalau kadar co2 terlalu tinggi kipas nyala --> otomatis 
      if ( receivedCO2 > 500 ): # nyalain 1 kipas
        level_co2 = 1
        
      elif ( receivedCO2 > 600 ): # nyalain 2 kipas
        level_co2 = 2

      elif ( receivedCO2 > 700 ): # nyalain 3 kipas
        level_co2 = 3

      elif ( receivedCO2 > 800 ): # nyalain 4 kipas
        level_co2 = 4
        
      else: 
        level_co2 = 0


        
      
      # mengambil level yang paling tinggi
      # jika level temperature > level co2 maka level = level temperature
      # jika level co2 > level temperature maka level = level co2
      level = 0 # hanya inisiasi saja
      if (level_temperature > level_co2):
        level = level_temperature

      else:
        level = level_co2

      print(f"level: {level}")
      if level == 0: # kipas mati semua
        kipas(1, 0)
        kipas(2, 0)
        kipas(3, 0)
        kipas(4, 0)
      
      elif level ==1:# kipas nyala 1
        kipas(1, 1)
        kipas(2, 0)
        kipas(3, 0)
        kipas(4, 0)

      elif level ==2:# kipas nyala 2
        kipas(1, 1)
        kipas(2, 1)
        kipas(3, 0)
        kipas(4, 0)

      elif level ==3:# kipas nyala 3
        kipas(1, 1)
        kipas(2, 1)
        kipas(3, 1)
        kipas(4, 0)
        
      elif level ==4:# kipas nyala 4
        kipas(1, 1)
        kipas(2, 1)
        kipas(3, 1)
        kipas(4, 1)

    else: # manual
      print ("mode manual")
      # menerima data dari ubidots lampu 1-4
      kipas1_state = menerima_data("tombol1")
      kipas2_state = menerima_data("tombol2")
      kipas3_state = menerima_data("tombol3")
      kipas4_state = menerima_data("tombol4")

      # menyalakan atau mematikan lampu 1-4
      kipas(1, int(kipas1_state))
      kipas(2, int(kipas2_state))
      kipas(3, int(kipas3_state))
      kipas(4, int(kipas4_state))

# jalankan program
# bukun thread untuk membaca sensor co2
co2_thread = threading.Thread(target=ambil_sensor_co2, args=(1,))
co2_thread.start()
suhu_thread = threading.Thread(target=ambil_sensor_suhu, args=(1,))
suhu_thread.start()

while True:
  main()