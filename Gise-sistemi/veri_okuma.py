import sqlite3

connection = sqlite3.connect('../new_database.db')

cursor = connection.cursor()

cursor.execute("SELECT * FROM calisanlar")
calisanlar = cursor.fetchall()

print("{:<5} {:<15} {:<15} {:<15} {:<10} {:<10}".format("ID", "Ad", "Soyad", "Doğum Tarihi", "Cinsiyet", "anahtar"))

# Ayırıcı satır
print("="*72)

for calisan in calisanlar:
    if calisan[4] == 1:
        cinsiyet = "Erkek"
    else:
        cinsiyet = "Kadın"
    print("{:<5} {:<15} {:<15} {:<15} {:<10} {:<10}".format(calisan[0], calisan[1], calisan[2], calisan[3], cinsiyet, calisan[5]))


connection.close()