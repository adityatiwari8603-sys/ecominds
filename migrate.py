from database import get_connection
from ai import find_topic


def migrate_knowledge():

    connection = get_connection()

    rows = connection.execute(
        "SELECT id, content FROM knowledge"
    ).fetchall()

    print(f"Found {len(rows)} knowledge records.")

    for row in rows:

        result = find_topic(row["content"])

        if result:

            subject = result["subject"]
            unit = result["unit"]
            topic = result["topic"]

            connection.execute(
                """
                UPDATE knowledge
                SET subject = ?,
                    unit = ?,
                    topic = ?
                WHERE id = ?
                """,
                (
                    subject,
                    unit,
                    topic,
                    row["id"]
                )
            )

            print(
                f"Updated ID {row['id']} → "
                f"{subject} | {unit} | {topic}"
            )

        else:

            print(
                f"ID {row['id']} → No syllabus match"
            )

    connection.commit()
    connection.close()

    print("\nMigration completed successfully!")


if __name__ == "__main__":
    migrate_knowledge()