from database import init_database, get_connection


JUNIOR_KNOWLEDGE = [

    {
        "title": "PPS - Programming Basics",
        "content": "Programming is the process of writing instructions for a computer. Important basics include variables, data types, operators, conditions, loops and functions.",
        "subject": "PPS",
        "unit": "Unit I",
        "topic": "Programming Basics",
        "category": "Study Notes",
        "difficulty": "Easy",
        "keywords": "programming, variables, data types, loops, functions",
    },

    {
        "title": "Physics - Basic Concepts",
        "content": "Physics studies matter, energy, motion and their interactions. Important fundamentals include measurement, units, force, motion, waves and optics.",
        "subject": "Physics",
        "unit": "Unit I",
        "topic": "Basic Physics",
        "category": "Study Notes",
        "difficulty": "Easy",
        "keywords": "physics, units, motion, force, waves, optics",
    },

    {
        "title": "Artificial Intelligence - Introduction",
        "content": "Artificial Intelligence is the field of computing concerned with creating systems that can perform tasks associated with human intelligence, such as learning, reasoning and problem solving.",
        "subject": "Artificial Intelligence",
        "unit": "Unit I",
        "topic": "Introduction to AI",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "AI, artificial intelligence, machine learning",
    },

    {
        "title": "Mathematics-I - Matrices",
        "content": "A matrix is a rectangular arrangement of elements in rows and columns. Important operations include addition, subtraction, scalar multiplication and matrix multiplication.",
        "subject": "Mathematics-I",
        "unit": "Unit I",
        "topic": "Matrices",
        "category": "Study Notes",
        "difficulty": "Medium",
        "keywords": "matrices, matrix, rows, columns",
    },

    {
        "title": "BME - Engineering Materials",
        "content": "Engineering materials include metals, polymers, ceramics and composites. Important properties include strength, hardness, toughness, ductility and conductivity.",
        "subject": "BME",
        "unit": "Unit I",
        "topic": "Engineering Materials",
        "category": "Study Notes",
        "difficulty": "Easy",
        "keywords": "BME, materials, metals, polymers, ceramics",
    },

    {
        "title": "BEEE - KCL",
        "content": "Kirchhoff's Current Law states that the algebraic sum of currents at a node is zero. Current entering a node equals current leaving the node.",
        "subject": "BEEE",
        "unit": "Unit I",
        "topic": "KCL",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "BEEE, KCL, current, node",
    },

    {
        "title": "Chemistry - Corrosion",
        "content": "Corrosion is the gradual deterioration of a material, especially a metal, due to chemical or electrochemical reactions with its environment.",
        "subject": "Chemistry",
        "unit": "Unit I",
        "topic": "Corrosion",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "chemistry, corrosion, rusting",
    },

    {
        "title": "Mathematics-II - Probability",
        "content": "Probability measures the likelihood of an event. Its value ranges from 0 to 1. Important topics include events, sample space and probability distributions.",
        "subject": "Mathematics-II",
        "unit": "Unit I",
        "topic": "Probability",
        "category": "Study Notes",
        "difficulty": "Easy",
        "keywords": "probability, event, sample space",
    },

    {
        "title": "Workshop Technology - Casting",
        "content": "Casting is a manufacturing process in which molten material is poured into a mould and allowed to solidify to produce the required shape.",
        "subject": "Workshop Technology",
        "unit": "Unit I",
        "topic": "Casting",
        "category": "Concept Explanation",
        "difficulty": "Medium",
        "keywords": "workshop, casting, mould, manufacturing",
    },

    {
        "title": "DSA - Data Structures",
        "content": "A data structure is a way of organizing and storing data so that operations can be performed efficiently. Examples include arrays, linked lists, stacks, queues, trees and graphs.",
        "subject": "Data Structures & Algorithms",
        "unit": "Unit I",
        "topic": "Data Structures",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "DSA, data structures, array, stack, queue, tree",
    },

    {
        "title": "OOP - Four Pillars",
        "content": "The four major principles of object oriented programming are encapsulation, abstraction, inheritance and polymorphism.",
        "subject": "OOP",
        "unit": "Unit I",
        "topic": "OOP Concepts",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "OOP, encapsulation, abstraction, inheritance, polymorphism",
    },

    {
        "title": "DBMS - Introduction",
        "content": "A Database Management System is software used to create, store, organize, retrieve and manage data in databases.",
        "subject": "DBMS",
        "unit": "Unit I",
        "topic": "DBMS Introduction",
        "category": "Concept Explanation",
        "difficulty": "Easy",
        "keywords": "DBMS, database, data management, SQL",
    },

    {
        "title": "Computer Networks - OSI Model",
        "content": "The OSI model has seven layers: Physical, Data Link, Network, Transport, Session, Presentation and Application.",
        "subject": "Computer Networks",
        "unit": "Unit I",
        "topic": "OSI Model",
        "category": "Important Question",
        "difficulty": "Medium",
        "keywords": "computer networks, OSI, layers, networking",
    },

    {
        "title": "Computer Fundamentals - CPU",
        "content": "The CPU is the main processing unit of a computer. Its major components include the ALU, Control Unit and registers.",
        "subject": "Computer Fundamentals",
        "unit": "Unit I",
        "topic": "CPU",
        "category": "Viva Question",
        "difficulty": "Easy",
        "keywords": "computer fundamentals, CPU, ALU, control unit",
    },

]


def seed_knowledge():

    init_database()

    connection = get_connection()

    inserted = 0
    skipped = 0

    for item in JUNIOR_KNOWLEDGE:

        existing = connection.execute(
            """
            SELECT id
            FROM knowledge
            WHERE title = ? AND subject = ?
            LIMIT 1
            """,
            (
                item["title"],
                item["subject"]
            )
        ).fetchone()

        if existing:
            skipped += 1
            continue

        connection.execute(
            """
            INSERT INTO knowledge
            (
                title,
                content,
                subject,
                unit,
                topic,
                category,
                difficulty,
                keywords,
                author
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                item["title"],
                item["content"],
                item["subject"],
                item["unit"],
                item["topic"],
                item["category"],
                item["difficulty"],
                item["keywords"],
                "EchoMind"
            )
        )

        inserted += 1

    connection.commit()
    connection.close()

    print("========================================")
    print("Junior Hub Knowledge Added")
    print("========================================")
    print("Inserted:", inserted)
    print("Skipped :", skipped)
    print("Total   :", len(JUNIOR_KNOWLEDGE))
    print("========================================")


if __name__ == "__main__":
    seed_knowledge()