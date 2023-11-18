import sqlite3
import pickle  # Python nesnelerini binary veriye dönüştürmek için kullanılyor

def parmak_izi_ekle(calisan_id, parmak_izi_verisi):
    connection = sqlite3.connect('../new_database.db')
    cursor = connection.cursor()

    # Parmak izi verisini binary formata dönüştrme
    parmak_izi_binary = pickle.dumps(parmak_izi_verisi)

    cursor.execute("UPDATE calisanlar SET anahtar = ? WHERE id = ?", (parmak_izi_binary, calisan_id))
    connection.commit()

    connection.close()

parmak_izi_verisi = '1323456797545'

# Calisan ID'sini belirleyin ve parmak izi verisini eklemek için fonksiyonu çağırın
calisan_id = input("Kişinin id değeri: ")  # Örnek olarak 1. çalışanın ID'sini kullanıyoruz
parmak_izi_ekle(calisan_id, parmak_izi_verisi)
