import sqlite3

connection = sqlite3.connect("ecomind.db")

connection.execute("""
    UPDATE knowledge
    SET subject = ?,
        unit = ?,
        topic = ?
    WHERE title = ?
""", (
    "Operating Systems",
    "Unit II",
    "Deadlocks",
    "Deadlock Common Mistake"
))

connection.commit()

print("Deadlock record fixed successfully!")

connection.close()