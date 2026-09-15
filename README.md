# 🧠 EchoMind

### The Knowledge That Never Graduates

EchoMind is an AI-powered academic knowledge platform designed to help college students **learn, search, share, and interact with academic knowledge** through a centralized knowledge network.

It combines a **FastAPI backend, SQLite database, Ollama-powered AI, and a responsive web interface** to provide college-focused question answering and academic knowledge management.

---

## ✨ Features

### 🤖 AI Academic Assistant

Ask academic questions through the EchoMind AI Query Terminal.

EchoMind generates answers using indexed academic knowledge so that responses remain grounded in the project's knowledge base.

Example:

> Explain FCFS scheduling with a solved example.

---

### 📚 Knowledge Network

Students can contribute academic knowledge to the platform.

Knowledge records can contain:

* Title
* Subject
* Unit
* Topic
* Category
* Difficulty
* Keywords
* Author
* Detailed explanation/content

---

### 🔎 Knowledge Search

Search the academic knowledge base by:

* Subject
* Topic
* Concept
* Category
* Formula
* Keywords

---

### 📊 Academic Dashboard

The dashboard provides an overview of the knowledge network, including:

* Knowledge records
* Subjects
* Topics
* Helpful feedback
* Not-helpful feedback
* Subject matrix
* Topic index
* Category channels

---

### 🎓 Junior Student Hub

EchoMind includes academic sections for students covering areas such as:

**Semester 1**

* PPS
* Physics
* Artificial Intelligence
* Mathematics-I
* BME

**Semester 2**

* BEEE
* Chemistry
* Mathematics-II
* Workshop Technology

**CS Core**

* Data Structures & Algorithms
* OOP
* Operating Systems
* DBMS
* Computer Networks
* Computer Fundamentals

---

### 👤 Authentication

EchoMind includes user authentication functionality with:

* Registration
* Login
* User information
* Student role
* Semester
* Branch
* Password hashing and verification

---

### 👍 Feedback System

Users can provide feedback on AI-generated answers.

This helps identify:

* Helpful answers
* Answers requiring improvement

---

## 🏗️ System Architecture

```text
                    ┌──────────────────────┐
                    │      Web Browser     │
                    │   EchoMind Frontend  │
                    └──────────┬───────────┘
                               │
                               │ HTTP Requests
                               ▼
                    ┌──────────────────────┐
                    │      FastAPI         │
                    │      Backend         │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
       ┌────────────┐   ┌─────────────┐  ┌─────────────┐
       │ SQLite DB  │   │ AI / RAG    │  │ Auth System │
       │            │   │ Pipeline    │  │             │
       └────────────┘   └──────┬──────┘  └─────────────┘
                               │
                               ▼
                       ┌──────────────┐
                       │    Ollama    │
                       │  Local LLM   │
                       └──────────────┘
```

---

## 🛠️ Technology Stack

### Backend

* Python
* FastAPI
* Uvicorn
* Pydantic

### AI / Machine Learning

* Ollama
* Transformers
* PyTorch
* NumPy
* SciPy
* scikit-learn
* SymPy

### Database

* SQLite

### Frontend

* HTML5
* CSS3
* JavaScript

### Development Tools

* Git
* GitHub
* VS Code
* Python Virtual Environment

---

## 📁 Project Structure

```text
ecomind/
│
├── main.py
├── ai.py
├── qa.py
├── database.py
├── schemas.py
│
├── requirements.txt
├── .gitignore
│
├── scheduling_parser.py
├── fcfs.py
├── sjf.py
│
├── seed_knowledge.py
├── seed_python.py
├── seed_math.py
├── seed_os.py
├── seed_se.py
├── seed_de.py
│
├── seed_dsa.py
├── seed_dsa_master.py
├── seed_dsa_arrays_hashing.py
├── seed_dsa_binary_search.py
├── seed_dsa_heap.py
├── seed_dsa_linked_list.py
├── seed_dsa_sliding_window.py
├── seed_dsa_stack.py
├── seed_dsa_two_pointers.py
│
├── seed_software_engineering.py
├── seed_full_junior_knowledge.py
│
├── test_ai.py
├── test_ollama.py
├── test_subjects.py
│
└── static/
    ├── index.html
    └── Start_EchoMind.bat
```

> Local SQLite database files and the Python virtual environment are intentionally excluded from GitHub using `.gitignore`.

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone https://github.com/adityatiwari8603-sys/ecominds.git
```

Move into the project:

```bash
cd ecominds
```

---

## 2. Create a virtual environment

### Windows

```powershell
python -m venv venv
```

Activate it:

```powershell
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can run the project using the virtual-environment Python directly.

---

## 3. Install dependencies

```powershell
pip install -r requirements.txt
```

---

# 🤖 Ollama Setup

EchoMind uses Ollama for local AI model interaction.

Install Ollama on your computer and make sure the Ollama service is running.

Then download/configure the model required by your EchoMind AI configuration.

You can verify that Ollama is available using:

```powershell
ollama list
```

The exact model used by the application should match the model configured in `ai.py`.

---

# ▶️ Run EchoMind

From the project directory:

```powershell
python -m uvicorn main:app --reload
```

If port `8000` is unavailable, use another port:

```powershell
python -m uvicorn main:app --reload --port 8080
```

Then open:

```text
http://127.0.0.1:8080
```

or, if using the default port:

```text
http://127.0.0.1:8000
```

---

# 🔌 Main API Endpoints

| Method | Endpoint     | Purpose                      |
| ------ | ------------ | ---------------------------- |
| POST   | `/register`  | Register a user              |
| POST   | `/login`     | User login                   |
| GET    | `/me`        | Get current user information |
| POST   | `/ask`       | Ask an academic question     |
| GET    | `/knowledge` | Retrieve knowledge           |
| POST   | `/knowledge` | Add academic knowledge       |
| GET    | `/search`    | Search the knowledge base    |
| GET    | `/dashboard` | Dashboard statistics         |

---

# 🧠 How EchoMind Works

A simplified question-answering flow:

```text
Student
   │
   ▼
Ask Academic Question
   │
   ▼
EchoMind Backend
   │
   ▼
Knowledge Retrieval
   │
   ▼
Relevant Academic Knowledge
   │
   ▼
AI Processing
   │
   ▼
Ollama
   │
   ▼
Grounded Answer
   │
   ▼
Student
```

The goal is to reduce unreliable generic answers by using the academic knowledge indexed inside EchoMind.

---

# 🔐 Security

EchoMind includes basic application security features such as:

* Password hashing
* Password verification
* Environment-variable protection through `.gitignore`
* Local database exclusion from Git
* Virtual environment exclusion from Git

Sensitive files such as `.env` files and local databases should not be committed to the repository.

---

# 📸 Screenshots

Screenshots will be added here to demonstrate the EchoMind interface.

### Dashboard

*Add screenshot here.*

### AI Query Terminal

*Add screenshot here.*

### Knowledge Network

*Add screenshot here.*

### Knowledge Search

*Add screenshot here.*

### Knowledge Sharing

*Add screenshot here.*

---

# 🚀 Future Improvements

Planned improvements include:

* Improved AI retrieval and ranking
* Better academic source attribution
* More college/university syllabus support
* Advanced student analytics
* Personalized learning recommendations
* Improved authentication and authorization
* Cloud deployment
* API documentation
* Automated testing
* Docker support
* CI/CD integration
* Better mobile experience

---

# 🎯 Project Goals

EchoMind aims to create a collaborative academic knowledge network where students can:

**Learn → Ask → Search → Share → Improve**

The long-term vision is to create a continuously growing academic knowledge system that becomes more useful as students contribute high-quality educational content.

---

# 👨‍💻 Author

**Aditya Tiwari**

B.Tech Computer Science Engineering Student

GitHub:

https://github.com/adityatiwari8603-sys

---

# 📄 License

This project is currently intended for educational and development purposes.

A formal open-source license can be added in a future version.

---

## ⭐ EchoMind

**The Knowledge That Never Graduates.**
