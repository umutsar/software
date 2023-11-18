import sqlite3

connection = sqlite3.connect('../new_database')
cursor = connection.cursor()

def calisan_guncelle(id, ad, soyad, dogum_tarihi):
    cursor.execute("UPDATE calisanlar SET ad = ?, soyad = ?, dogum_tarihi = ? WHERE id = ?",
                   (ad, soyad, dogum_tarihi, id))
    connection.commit()
    print("Çalışan güncellendi.")

calisan_id = input("Güncellenecek çalışanın ID'sini giriniz: ")
yeni_ad = input("Yeni adı giriniz: ")
yeni_soyad = input("Yeni soyadı giriniz: ")
yeni_dogum_tarihi = input("Yeni doğum tarihini (YYYY-MM-DD) giriniz: ")

calisan_guncelle(calisan_id, yeni_ad, yeni_soyad, yeni_dogum_tarihi)

connection.close()