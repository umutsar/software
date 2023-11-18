import serial
import sqlite3

# Veritabanına bağlan
with sqlite3.connect('../new_database.db') as conn:
    cursor = conn.cursor()


    # Seri iletişim portu ayarları
    ser = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1)

    try:
        while True:
            data = ser.readline().decode().strip()
            if data:
                print("Sensörden Gelen Veri:", data)
                query = "SELECT * FROM calisanlar WHERE anahtar = ?"
                cursor.execute(query, (data,))
                 # Sonucu al
                calisan = cursor.fetchone()
                # Sonucu değerlendir
                if calisan:
                    query_two = "SELECT * FROM girisler 
                    print(calisan)
                    print("Var")
                else:
                    print("Yok")
    except KeyboardInterrupt:
        ser.close()
        conn.close()
        print("Program sonlandırıldı.")