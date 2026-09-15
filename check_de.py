import sqlite3

connection = sqlite3.connect("ecomind.db")

result = connection.execute(
    "SELECT COUNT(*) FROM knowledge WHERE subject = ?",
    ("Digital Electronics",)
).fetchone()

print("Digital Electronics entries:", result[0])

connection.close()