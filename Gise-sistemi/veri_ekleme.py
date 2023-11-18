import sqlite3

def yeni_calisan_ekle(ad, soyad, dogum_tarihi, cinsiyet):
    connection = sqlite3.connect('../new_database.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO calisanlar (ad, soyad, dogum_tarihi, cinsiyet) VALUES (?, ?, ?, ?)", (ad, soyad, dogum_tarihi, cinsiyet))
    connection.commit()

    connection.close()

ad_bilgisi = input("Ad bilgisini girin: ")
soyad_bilgisi = input("Soyad bilgisini girin: ")
dogum_tarihi = input("Doğum tarihi (yyyy-aa-gg): ")
cinsiyet = input("Cinsiyeti Giriniz(Erkek ise 1, Kadın ise 0 giriniz): ")
yeni_calisan_ekle(ad_bilgisi, soyad_bilgisi, dogum_tarihi, cinsiyet)