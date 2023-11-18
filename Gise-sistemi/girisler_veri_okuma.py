import sqlite3

connection = sqlite3.connect('../new_database.db')

cursor = connection.cursor()

cursor.execute("SELECT * FROM girisler")
girisler = cursor.fetchall()

print("{:<5} {:<15} {:<15}".format("ID", "calisan_idsi", "tarih"))

# Ayırıcı satır
print("="*36)

for veri in girisler:
    cursor.execute("SELECT * FROM calisanlar")
    birinci_index_isim = cursor.fetchall()
    veri[1] = 
    print("{:<5} {:<15} {:<15}".format(veri[0], veri[1], veri[2],))


connection.close()