import sqlite3

connection = sqlite3.connect("ecomind.db")

# Delete duplicate FCFS records.
# Keep the oldest FCFS record.
connection.execute("""
    DELETE FROM knowledge
    WHERE subject = 'Operating Systems'
      AND topic = 'FCFS Scheduling'
      AND id NOT IN (
          SELECT MIN(id)
          FROM knowledge
          WHERE subject = 'Operating Systems'
            AND topic = 'FCFS Scheduling'
      )
""")

connection.commit()

remaining = connection.execute("""
    SELECT COUNT(*)
    FROM knowledge
    WHERE topic = 'FCFS Scheduling'
""").fetchone()[0]

print("Duplicate FCFS records removed.")
print("Remaining FCFS records:", remaining)

connection.close()