import sqlite3

connection = sqlite3.connect('../new_database') 
cursor = connection.cursor()

def calisan_sil(calisan_id):
    cursor.execute("DELETE FROM calisanlar WHERE id = ?", (calisan_id,))
    connection.commit()

def calisan_oku(calisan_id):
    cursor.execute("SELECT * FROM calisanlar WHERE id = ?", (calisan_id,))
    calisan = cursor.fetchone()

    if calisan:
        print("Aşağıdaki satır silindi.")
        print("ID:", calisan[0])
        print("Ad:", calisan[1])
        print("Soyad:", calisan[2])
        print("Doğum Tarihi:", calisan[3])
    else:
        print("Belirtilen ID'ye sahip çalışan bulunamadı.")

silinecek_id = input("Silmek istediğiniz id giriniz: ")
calisan_oku(silinecek_id)

calisan_sil(silinecek_id)

connection.close()