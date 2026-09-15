import sqlite3

connection = sqlite3.connect("ecomind.db")

connection.execute(
    """
    UPDATE knowledge
    SET subject = ?,
        unit = ?,
        topic = ?
    WHERE title LIKE ?
       OR content LIKE ?
    """,
    (
        "Mathematics",
        "Unit I",
        "Fourier Series",
        "%Fourier%",
        "%Fourier%"
    )
)

connection.commit()

print("Fourier Series record fixed successfully!")

connection.close()