import sqlite3


DATABASE_NAME = "ecomind.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)

    connection.row_factory = sqlite3.Row

    return connection


def init_database():

    connection = get_connection()


    # =====================================================
    # KNOWLEDGE TABLE
    # =====================================================

    connection.execute("""
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            subject TEXT,
            unit TEXT,
            topic TEXT,
            category TEXT,
            difficulty TEXT,
            keywords TEXT,
            author TEXT,
            helpful INTEGER DEFAULT 0,
            not_helpful INTEGER DEFAULT 0
        )
    """)


    # =====================================================
    # USERS TABLE
    # =====================================================

    connection.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password_hash TEXT NOT NULL,
            role TEXT NOT NULL DEFAULT 'student',
            semester TEXT,
            branch TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)


    # =====================================================
    # SESSIONS TABLE
    # =====================================================

    connection.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token TEXT UNIQUE NOT NULL,
            user_id INTEGER NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
    """)


    connection.commit()

    connection.close()


if __name__ == "__main__":

    init_database()

    print("EchoMind database initialized successfully.")