import sqlite3

connection = sqlite3.connect('/U/first_database/first_db')

cursor = connection.cursor()

cursor.execute("SELECT * FROM giris_bilgileri")
calisanlar = cursor.fetchall()

print("{:<5} {:<15} {:<15}".format("ID", "Çalışan ID", "Zaman"))

# Ayırıcı satır
print("="*62)

for calisan in calisanlar:
    print("{:<5} {:<15} {:<15}".format(calisan[0], calisan[1], calisan[2]))


connection.close()
