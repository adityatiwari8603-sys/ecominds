from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

import hashlib
import hmac
import secrets

from database import get_connection
from ai import analyze_knowledge
from qa import generate_answer


app = FastAPI(
    title="EchoMind",
    description="The Knowledge That Never Graduates",
    version="1.0"
)


# =========================================================
# STATIC FILES
# =========================================================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)


# =========================================================
# SCHEMAS
# =========================================================

class KnowledgeCreate(BaseModel):
    title: str
    content: str
    subject: str = ""
    unit: str = ""
    topic: str = ""
    category: str = ""
    difficulty: str = ""
    keywords: str = ""
    author: str


class QuestionRequest(BaseModel):
    question: str


class RegisterRequest(BaseModel):
    name: str
    email: str
    password: str
    role: str = "student"
    semester: str = ""
    branch: str = ""


class LoginRequest(BaseModel):
    email: str
    password: str


def hash_password(password: str) -> str:
    salt = secrets.token_bytes(16)

    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        100000
    )

    return salt.hex() + ":" + password_hash.hex()


def verify_password(password: str, stored_hash: str) -> bool:
    try:
        salt_hex, hash_hex = stored_hash.split(":")

        salt = bytes.fromhex(salt_hex)

        password_hash = hashlib.pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            100000
        )

        return hmac.compare_digest(
            password_hash.hex(),
            hash_hex
        )

    except Exception:
        return False


# =========================================================
# REGISTER
# =========================================================

@app.post("/register")
def register_user(user: RegisterRequest):

    name = user.name.strip()
    email = user.email.strip().lower()
    password = user.password

    if not name:
        raise HTTPException(
            status_code=400,
            detail="Name cannot be empty."
        )

    if not email:
        raise HTTPException(
            status_code=400,
            detail="Email cannot be empty."
        )

    if len(password) < 6:
        raise HTTPException(
            status_code=400,
            detail="Password must contain at least 6 characters."
        )

    connection = get_connection()

    try:

        existing_user = connection.execute(
            """
            SELECT id
            FROM users
            WHERE LOWER(email) = LOWER(?)
            """,
            (email,)
        ).fetchone()

        if existing_user:
            raise HTTPException(
                status_code=409,
                detail="Email already registered."
            )

        password_hash = hash_password(password)

        cursor = connection.execute(
            """
            INSERT INTO users
            (
                name,
                email,
                password_hash,
                role,
                semester,
                branch
            )
            VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                name,
                email,
                password_hash,
                user.role,
                user.semester,
                user.branch
            )
        )

        connection.commit()

        return {
            "success": True,
            "message": "Registration successful.",
            "user_id": cursor.lastrowid,
            "name": name,
            "email": email,
            "role": user.role
        }

    except HTTPException:
        connection.rollback()
        raise

    except Exception as error:

        connection.rollback()

        print(
            "REGISTER ERROR:",
            error
        )

        raise HTTPException(
            status_code=500,
            detail="Registration failed."
        )

    finally:
        connection.close()
        # =========================================================
# LOGIN
# =========================================================
@app.post("/login")
def login_user(
    user: LoginRequest,
    response: Response
):

    email = user.email.strip().lower()
    password = user.password

    if not email:
        raise HTTPException(
            status_code=400,
            detail="Email cannot be empty."
        )

    if not password:
        raise HTTPException(
            status_code=400,
            detail="Password cannot be empty."
        )

    connection = get_connection()

    try:

        existing_user = connection.execute(
            """
            SELECT
                id,
                name,
                email,
                password_hash,
                role,
                semester,
                branch
            FROM users
            WHERE LOWER(email) = LOWER(?)
            """,
            (email,)
        ).fetchone()

        if not existing_user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password."
            )

        if not verify_password(
            password,
            existing_user["password_hash"]
        ):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password."
            )

        # Create a secure session token
        session_token = secrets.token_urlsafe(32)

        # Save session in database
        connection.execute(
            """
            INSERT INTO sessions
            (
                token,
                user_id
            )
            VALUES (?, ?)
            """,
            (
                session_token,
                existing_user["id"]
            )
        )

        connection.commit()

        # Send token to browser as HTTP-only cookie
        response.set_cookie(
            key="echomind_session",
            value=session_token,
            httponly=True,
            samesite="lax",
            max_age=60 * 60 * 24 * 7
        )

        return {
            "success": True,
            "message": "Login successful.",
            "user": {
                "id": existing_user["id"],
                "name": existing_user["name"],
                "email": existing_user["email"],
                "role": existing_user["role"],
                "semester": existing_user["semester"],
                "branch": existing_user["branch"]
            }
        }

    except HTTPException:
        connection.rollback()
        raise

    except Exception as error:

        connection.rollback()

        print(
            "LOGIN ERROR:",
            error
        )

        raise HTTPException(
            status_code=500,
            detail="Login failed."
        )

    finally:
        connection.close()
        # =========================================================
# CURRENT USER
# =========================================================

@app.get("/me")
def get_current_user(request: Request):

    session_token = request.cookies.get(
        "echomind_session"
    )

    if not session_token:
        raise HTTPException(
            status_code=401,
            detail="Not logged in."
        )

    connection = get_connection()

    try:

        user = connection.execute(
            """
            SELECT
                users.id,
                users.name,
                users.email,
                users.role,
                users.semester,
                users.branch
            FROM sessions
            JOIN users
                ON users.id = sessions.user_id
            WHERE sessions.token = ?
            """,
            (session_token,)
        ).fetchone()

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Session expired or invalid."
            )

        return {
            "logged_in": True,
            "user": {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "role": user["role"],
                "semester": user["semester"],
                "branch": user["branch"]
            }
        }

    finally:
            connection.close()
def get_current_user(request: Request):

    session_token = request.cookies.get(
        "echomind_session"
    )

    if not session_token:
        raise HTTPException(
            status_code=401,
            detail="Not logged in."
        )

    connection = get_connection()

    try:

        user = connection.execute(
            """
            SELECT
                users.id,
                users.name,
                users.email,
                users.role,
                users.semester,
                users.branch
            FROM sessions
            JOIN users
                ON users.id = sessions.user_id
            WHERE sessions.token = ?
            """,
            (session_token,)
        ).fetchone()

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Session expired or invalid."
            )

        return {
            "logged_in": True,
            "user": {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "role": user["role"],
                "semester": user["semester"],
                "branch": user["branch"]
            }
        }

    finally:
        connection.close()


# =========================================================
# CURRENT USER
# =========================================================

@app.get("/me")
def get_current_user(request: Request):

    session_token = request.cookies.get(
        "echomind_session"
    )

    if not session_token:
        raise HTTPException(
            status_code=401,
            detail="Not logged in."
        )

    connection = get_connection()

    try:

        user = connection.execute(
            """
            SELECT
                users.id,
                users.name,
                users.email,
                users.role,
                users.semester,
                users.branch
            FROM sessions
            JOIN users
                ON users.id = sessions.user_id
            WHERE sessions.token = ?
            """,
            (session_token,)
        ).fetchone()

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Session expired or invalid."
            )

        return {
            "logged_in": True,
            "user": {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "role": user["role"],
                "semester": user["semester"],
                "branch": user["branch"]
            }
        }

    finally:
        connection.close()

    session_token = request.cookies.get(
        "echomind_session"
    )

    if not session_token:
        raise HTTPException(
            status_code=401,
            detail="Not logged in."
        )

    connection = get_connection()

    try:

        user = connection.execute(
            """
            SELECT
                users.id,
                users.name,
                users.email,
                users.role,
                users.semester,
                users.branch
            FROM sessions
            JOIN users
                ON users.id = sessions.user_id
            WHERE sessions.token = ?
            """,
            (session_token,)
        ).fetchone()

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Session expired or invalid."
            )

        return {
            "logged_in": True,
            "user": {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "role": user["role"],
                "semester": user["semester"],
                "branch": user["branch"]
            }
        }
    finally:
        connection.close()


# =========================================================
# CURRENT USER
# =========================================================


    session_token = request.cookies.get(
        "echomind_session"
    )

    if not session_token:
        raise HTTPException(
            status_code=401,
            detail="Not logged in."
        )

    connection = get_connection()

    try:

        user = connection.execute(
            """
            SELECT
                users.id,
                users.name,
                users.email,
                users.role,
                users.semester,
                users.branch
            FROM sessions
            JOIN users
                ON users.id = sessions.user_id
            WHERE sessions.token = ?
            """,
            (session_token,)
        ).fetchone()

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Session expired or invalid."
            )

        return {
            "logged_in": True,
            "user": {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "role": user["role"],
                "semester": user["semester"],
                "branch": user["branch"]
            }
        }

    finally:
        connection.close()


# =========================================================
# HOME PAGE
# =========================================================

@app.get("/")
def home():
    return FileResponse(
        "static/index.html"
    )


# =========================================================
# ASK ECHOMIND
# =========================================================

@app.post("/ask")
def ask_question(request: QuestionRequest):

    question = request.question.strip()

    if not question:
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    try:

        result = generate_answer(
            question
        )

        return result

    except Exception as error:

        print(
            "ASK ERROR:",
            error
        )

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


# =========================================================
# GET ALL KNOWLEDGE
# =========================================================

@app.get("/knowledge")
def get_knowledge():

    connection = get_connection()

    rows = connection.execute(
        """
               SELECT
            id,
            title,
            content,
            subject,
            unit,
            topic,
            category,
            difficulty,
            keywords,
            author,
            helpful,
            not_helpful
        FROM knowledge
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    result = []

    for row in rows:

        result.append(
    {
        "id": row["id"],
        "title": row["title"],
        "content": row["content"],
        "subject": row["subject"],
        "unit": row["unit"],
        "topic": row["topic"],
        "category": row["category"],
        "difficulty": row["difficulty"],
        "keywords": row["keywords"],
        "author": row["author"],
        "helpful": row["helpful"] or 0,
        "not_helpful": row["not_helpful"] or 0
    }
)

    return result


# =========================================================
# ADD KNOWLEDGE
# =========================================================

@app.post("/knowledge")
@app.post("/knowledge")
def add_knowledge(
    knowledge: KnowledgeCreate
):

    # -----------------------------------------------------
    # VALIDATION
    # -----------------------------------------------------

    title = knowledge.title.strip()
    content = knowledge.content.strip()
    author = knowledge.author.strip()

    if not title:
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty."
        )

    if not content:
        raise HTTPException(
            status_code=400,
            detail="Knowledge content cannot be empty."
        )

    if not author:
        raise HTTPException(
            status_code=400,
            detail="Author cannot be empty."
        )

    # -----------------------------------------------------
    # DATABASE CONNECTION
    # -----------------------------------------------------

    connection = get_connection()

    try:

        # -------------------------------------------------
        # DUPLICATE CHECK
        # -------------------------------------------------

        duplicate = connection.execute(
            """
            SELECT id, title
            FROM knowledge
            WHERE LOWER(TRIM(title)) = LOWER(TRIM(?))
               OR LOWER(TRIM(content)) = LOWER(TRIM(?))
            LIMIT 1
            """,
            (title, content)
        ).fetchone()

        if duplicate:

            raise HTTPException(
                status_code=409,
                detail="Similar knowledge already exists."
            )

        # -------------------------------------------------
        # AI ANALYSIS
        # -------------------------------------------------

        try:

            ai_result = analyze_knowledge(
                content
            )

        except Exception as error:

            print(
                "AI ANALYSIS ERROR:",
                error
            )

            ai_result = {}

        # -------------------------------------------------
        # KEEP USER-SUBMITTED VALUES
        # -------------------------------------------------

        subject = (
            getattr(knowledge, "subject", None)
            or ai_result.get("subject")
            or "General"
        )

        unit = (
            getattr(knowledge, "unit", None)
            or ai_result.get("unit")
            or "General"
        )

        topic = (
            getattr(knowledge, "topic", None)
            or ai_result.get("topic")
            or "General"
        )

        category = (
            getattr(knowledge, "category", None)
            or ai_result.get("category")
            or "Concept Explanation"
        )

        difficulty = (
            getattr(knowledge, "difficulty", None)
            or ai_result.get("difficulty")
            or "Medium"
        )

        keywords = (
            getattr(knowledge, "keywords", None)
            or ai_result.get("keywords")
            or ""
        )

        # -------------------------------------------------
        # INSERT KNOWLEDGE
        # -------------------------------------------------

        cursor = connection.execute(
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
            VALUES
            (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
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
        )

        connection.commit()

        knowledge_id = cursor.lastrowid

        # -------------------------------------------------
        # RESPONSE
        # -------------------------------------------------

        return {
            "success": True,
            "message": "Knowledge shared successfully.",
            "id": knowledge_id,
            "knowledge": {
                "title": title,
                "subject": subject,
                "unit": unit,
                "topic": topic,
                "category": category,
                "difficulty": difficulty,
                "keywords": keywords,
                "author": author
            }
        }

    except HTTPException:
        connection.rollback()
        raise

    except Exception as error:

        connection.rollback()

        print(
            "DATABASE ERROR:",
            error
        )

        raise HTTPException(
            status_code=500,
            detail="Failed to save knowledge."
        )

    finally:

        connection.close()

    if not knowledge.title.strip():

        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty."
        )


    if not knowledge.content.strip():

        raise HTTPException(
            status_code=400,
            detail="Knowledge content cannot be empty."
        )


    if not knowledge.author.strip():

        raise HTTPException(
            status_code=400,
            detail="Author cannot be empty."
        )


    # -----------------------------------------------------
    # AI ANALYSIS
    # -----------------------------------------------------

    try:

        ai_result = analyze_knowledge(
            knowledge.content
        )

    except Exception as error:

        print(
            "AI ANALYSIS ERROR:",
            error
        )

        # Safe fallback
        ai_result = {
            "subject": "General",
            "unit": "General",
            "topic": "General",
            "category": "Concept Explanation",
            "difficulty": "Medium",
            "keywords": ""
        }


    # -----------------------------------------------------
    # DATABASE
    # -----------------------------------------------------

    connection = get_connection()


    cursor = connection.execute(
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
            knowledge.title,
            knowledge.content,
            ai_result.get(
                "subject",
                ""
            ),
            ai_result.get(
                "unit",
                ""
            ),
            ai_result.get(
                "topic",
                ""
            ),
            ai_result.get(
                "category",
                ""
            ),
            ai_result.get(
                "difficulty",
                ""
            ),
            ai_result.get(
                "keywords",
                ""
            ),
            knowledge.author
        )
    )


    connection.commit()


    knowledge_id = cursor.lastrowid


    connection.close()


    return {
        "message":
            "Knowledge added successfully!",

        "knowledge_id":
            knowledge_id,

        "ai_analysis":
            ai_result
    }


# =========================================================
# SEARCH KNOWLEDGE
# =========================================================

@app.get("/search")
def search_knowledge(q: str = ""):

    query = q.strip()


    if not query:

        return []


    search_pattern = (
        "%" +
        query +
        "%"
    )


    connection = get_connection()


    rows = connection.execute(
        """
        SELECT
            id,
            title,
            content,
            subject,
            unit,
            topic,
            category,
            difficulty,
            keywords,
            author
        FROM knowledge

        WHERE
            title LIKE ?
            OR content LIKE ?
            OR subject LIKE ?
            OR unit LIKE ?
            OR topic LIKE ?
            OR category LIKE ?
            OR keywords LIKE ?

        ORDER BY id DESC
        """,
        (
            search_pattern,
            search_pattern,
            search_pattern,
            search_pattern,
            search_pattern,
            search_pattern,
            search_pattern
        )
    ).fetchall()


    connection.close()


    result = []


    for row in rows:

        result.append(
            {
                "id": row["id"],
                "title": row["title"],
                "content": row["content"],
                "subject": row["subject"],
                "unit": row["unit"],
                "topic": row["topic"],
                "category": row["category"],
                "difficulty": row["difficulty"],
                "keywords": row["keywords"],
                "author": row["author"]
            }
        )


    return result


# =========================================================
# HELPFUL FEEDBACK
# =========================================================
@app.post(
    "/knowledge/{knowledge_id}/helpful"
)
def helpful_feedback(
    knowledge_id: int
):
    connection = get_connection()

    row = connection.execute(
        """
        SELECT id
        FROM knowledge
        WHERE id = ?
        """,
        (knowledge_id,)
    ).fetchone()

    if not row:
        connection.close()
        raise HTTPException(
            status_code=404,
            detail="Knowledge not found."
        )

    connection.execute(
        """
        UPDATE knowledge
        SET helpful =
            COALESCE(helpful, 0) + 1
        WHERE id = ?
        """,
        (knowledge_id,)
    )

    connection.commit()
    connection.close()

    return {
        "message":
            "Thank you for your feedback!"
    }
# =========================================================
# NOT HELPFUL FEEDBACK
# =========================================================

@app.post(
    "/knowledge/{knowledge_id}/not-helpful"
)
def not_helpful_feedback(
    knowledge_id: int
):

    connection = get_connection()


    row = connection.execute(
        """
        SELECT id
        FROM knowledge
        WHERE id = ?
        """,
        (knowledge_id,)
    ).fetchone()


    if not row:

        connection.close()

        raise HTTPException(
            status_code=404,
            detail="Knowledge not found."
        )


    connection.execute(
        """
        UPDATE knowledge
        SET not_helpful =
            COALESCE(not_helpful, 0) + 1
        WHERE id = ?
        """,
        (knowledge_id,)
    )


    connection.commit()

    connection.close()


    return {
        "message":
            "Thank you for your feedback!"
    }


# =========================================================
# DASHBOARD
# =========================================================

@app.get("/dashboard")
def dashboard():

    connection = get_connection()


    # -----------------------------------------------------
    # TOTAL KNOWLEDGE
    # -----------------------------------------------------

    total_knowledge = connection.execute(
        """
        SELECT COUNT(*) AS count
        FROM knowledge
        """
    ).fetchone()["count"]


    # -----------------------------------------------------
    # TOTAL SUBJECTS
    # -----------------------------------------------------

    total_subjects = connection.execute(
        """
        SELECT COUNT(
            DISTINCT subject
        ) AS count

        FROM knowledge

        WHERE subject IS NOT NULL
        AND subject != ''
        """
    ).fetchone()["count"]


    # -----------------------------------------------------
    # TOTAL TOPICS
    # -----------------------------------------------------

    total_topics = connection.execute(
        """
        SELECT COUNT(
            DISTINCT topic
        ) AS count

        FROM knowledge

        WHERE topic IS NOT NULL
        AND topic != ''
        """
    ).fetchone()["count"]


    # -----------------------------------------------------
    # TOTAL HELPFUL
    # -----------------------------------------------------

    total_helpful = connection.execute(
        """
        SELECT
            COALESCE(
                SUM(helpful),
                0
            ) AS count

        FROM knowledge
        """
    ).fetchone()["count"]


    # -----------------------------------------------------
    # TOTAL NOT HELPFUL
    # -----------------------------------------------------

    total_not_helpful = connection.execute(
        """
        SELECT
            COALESCE(
                SUM(not_helpful),
                0
            ) AS count

        FROM knowledge
        """
    ).fetchone()["count"]


    # -----------------------------------------------------
    # SUBJECT STATISTICS
    # -----------------------------------------------------

    subject_rows = connection.execute(
        """
        SELECT
            subject,
            COUNT(*) AS count

        FROM knowledge

        WHERE
            subject IS NOT NULL
            AND subject != ''

        GROUP BY subject

        ORDER BY count DESC
        """
    ).fetchall()


    subjects = []


    for row in subject_rows:

        subjects.append(
            {
                "subject":
                    row["subject"],

                "count":
                    row["count"]
            }
        )


    # -----------------------------------------------------
    # TOPIC STATISTICS
    # -----------------------------------------------------

    topic_rows = connection.execute(
        """
        SELECT
            topic,
            COUNT(*) AS count

        FROM knowledge

        WHERE
            topic IS NOT NULL
            AND topic != ''

        GROUP BY topic

        ORDER BY count DESC
        """
    ).fetchall()


    topics = []


    for row in topic_rows:

        topics.append(
            {
                "topic":
                    row["topic"],

                "count":
                    row["count"]
            }
        )


    # -----------------------------------------------------
    # CATEGORY STATISTICS
    # -----------------------------------------------------

    category_rows = connection.execute(
        """
        SELECT
            category,
            COUNT(*) AS count

        FROM knowledge

        WHERE
            category IS NOT NULL
            AND category != ''

        GROUP BY category

        ORDER BY count DESC
        """
    ).fetchall()


    categories = []


    for row in category_rows:

        categories.append(
            {
                "category":
                    row["category"],

                "count":
                    row["count"]
            }
        )


    connection.close()


    # -----------------------------------------------------
    # FINAL DASHBOARD RESPONSE
    # -----------------------------------------------------

    return {

        "total_knowledge":
            total_knowledge,

        "total_subjects":
            total_subjects,

        "total_topics":
            total_topics,

        "total_helpful":
            total_helpful,

        "total_not_helpful":
            total_not_helpful,

        "subjects":
            subjects,

        "topics":
            topics,

        "categories":
            categories
    }
