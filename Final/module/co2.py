import serial
from struct import unpack
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 9600)  # Ganti dengan port serial yang sesuai

def sensorco2():
  dataRaw = ser.read(4)  # Ubah ukuran data yang dibaca sesuai format data sensor
  receivedCO2, receivedTVOC = unpack("hh", dataRaw)  # Menggunakan format "hh" untuk dua nilai short
  
  print(f"Received CO2 Data: {receivedCO2} ppm")
  print(f"Received TVOC Data: {receivedTVOC} ppb")
  print("==============================================")
  return receivedCO2, receivedTVOC

# testing
# while True:
#     sensorco2()
#     sleep(1)


