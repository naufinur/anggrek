import Adafruit_DHT

# Tentukan tipe sensor yang digunakan (DHT11)
sensor = Adafruit_DHT.DHT11

# Tentukan nomor pin GPIO yang terhubung dengan sensor
pin = 4  # Ganti dengan nomor pin yang sesuai

# Membaca data dari sensor
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

# Memeriksa apakah pembacaan data berhasil
if humidity is not None and temperature is not None:
    print(f"Suhu: {temperature:.1f}°C")
    print(f"Kelembaban: {humidity:.1f}%")
else:
    print("Gagal membaca data dari sensor DHT11. Pastikan koneksi dan konfigurasi benar.")
