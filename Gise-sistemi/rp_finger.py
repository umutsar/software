import serial
import sqlite3
# Veritabanı kodlarım
connection = sqlite3.connect('../new_database')
cursor = connection.cursor()

# Seri iletişim portu ayarları
ser = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1)

try:
    while True:
        data = ser.readline().decode().strip()
        if data:
            print("Sensörden Gelen Veri:", data)
        
except KeyboardInterrupt:
    ser.close()
    print("Program sonlandırıldı.")