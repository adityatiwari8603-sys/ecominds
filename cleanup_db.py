import sqlite3

connection = sqlite3.connect("ecomind.db")

connection.execute("""
    UPDATE knowledge
    SET subject = 'Python Programming'
    WHERE lower(subject) = 'python programming'
""")

connection.execute("""
    UPDATE knowledge
    SET category = 'Common Mistake'
    WHERE lower(category) = 'common mistake'
""")

connection.execute("""
    UPDATE knowledge
    SET topic = 'Python Lists'
    WHERE lower(topic) = 'python lists'
""")

connection.execute("""
    UPDATE knowledge
    SET difficulty = 'Beginner'
    WHERE lower(difficulty) = 'begineer'
""")

connection.execute("""
    UPDATE knowledge
    SET unit = 'Unit I'
    WHERE lower(unit) = 'unit 1'
""")

connection.execute("""
    UPDATE knowledge
    SET unit = 'Unit II'
    WHERE lower(unit) = 'unit 2'
""")

connection.commit()
connection.close()

print("Database normalized successfully")