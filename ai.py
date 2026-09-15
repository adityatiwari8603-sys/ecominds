from ollama import chat
import json
import re


# ============================================================
# ECHOMIND SYLLABUS TOPIC RULES
# ============================================================

TOPIC_RULES = {

    "Operating Systems": {

        "Unit I": [
            "Operating System Basics",
            "Process Management",
            "FCFS Scheduling",
            "SJF Scheduling",
            "SRTF Scheduling",
            "Round Robin Scheduling"
        ],

        "Unit II": [
            "Inter Process Communication",
            "Critical Section",
            "Race Conditions",
            "Semaphores",
            "Producer Consumer",
            "Reader Writer",
            "Dining Philosophers",
            "Deadlocks",
            "Deadlock",
            "Starvation"
        ],

        "Unit III": [
            "Memory Management",
            "Memory Fragmentation",
            "Paging",
            "Virtual Memory",
            "Page Replacement"
        ],

        "Unit IV": [
            "File Management",
            "File Allocation",
            "Disk Scheduling"
        ]
    },


    "Data Structures": {

        "Unit I": [
            "Data Structures Basics",
            "Linear Search",
            "Binary Search"
        ],

        "Unit II": [
            "Stack",
            "Queue"
        ],

        "Unit III": [
            "Linked List",
            "Trees"
        ],

        "Unit IV": [
            "Sorting",
            "Hashing"
        ]
    },


    "Python Programming": {

        "Unit I": [
            "Python Basics",
            "Python Indentation",
            "Python Strings",
            "Python File Handling"
        ],

        "Unit II": [
            "Python Lists",
            "Python Dictionaries",
            "Python Functions"
        ],

        "Unit III": [
            "Turtle Graphics",
            "Python Image Processing",
            "Python GUI"
        ],

        "Unit IV": [
            "Python OOP",
            "Inheritance and Polymorphism",
            "Exception Handling",
            "Multithreading and Networks"
        ]
    },


    "Software Engineering": {

        "Unit I": [
            "Software Engineering Basics",
            "SDLC",
            "SDLC Models",
            "Software Metrics and Risk"
        ],

        "Unit II": [
            "Requirement Engineering",
            "SRS",
            "Software Design"
        ],

        "Unit III": [
            "Software Testing",
            "Testing Strategies",
            "Debugging"
        ],

        "Unit IV": [
            "Software Maintenance",
            "Software Quality",
            "Reengineering"
        ]
    },


    "Digital Electronics": {

        "Unit I": [
            "Number Systems",
            "Boolean Simplification",
            "Logic Gates"
        ],

        "Unit II": [
            "Combinational Circuits",
            "Multiplexers",
            "Demultiplexers",
            "Encoders",
            "Decoders"
        ],

        "Unit III": [
            "Flip Flops",
            "Sequential Circuits"
        ],

        "Unit IV": [
            "Counters",
            "Registers",
            "Memory",
            "Programmable Logic"
        ]
    },


    "Mathematics": {

        "Unit I": [
            "Fourier Series",
            "Sequences and Series"
        ],

        "Unit II": [
            "Partial Derivatives",
            "Maxima and Minima",
            "Vector Calculus"
        ],

        "Unit III": [
            "Multiple Integrals",
            "Vector Integral Theorems"
        ],

        "Unit IV": [
            "Differential Equations"
        ]
    }
}


# ============================================================
# FIND SUBJECT + UNIT + TOPIC
# ============================================================

def find_topic(content):

    text = content.lower()

    # --------------------------------------------------------
    # SPECIAL FOURIER DETECTION
    # --------------------------------------------------------

    if "fourier" in text:

        return {
            "subject": "Mathematics",
            "unit": "Unit I",
            "topic": "Fourier Series"
        }


    # --------------------------------------------------------
    # SPECIAL FCFS DETECTION
    # --------------------------------------------------------

    if (
        "fcfs" in text
        or "first come first served" in text
        or "first-come-first-served" in text
    ):

        return {
            "subject": "Operating Systems",
            "unit": "Unit I",
            "topic": "FCFS Scheduling"
        }


    # --------------------------------------------------------
    # SPECIAL SJF DETECTION
    # --------------------------------------------------------

    if (
        "sjf" in text
        or "shortest job first" in text
        or "shortest-job-first" in text
    ):

        return {
            "subject": "Operating Systems",
            "unit": "Unit I",
            "topic": "SJF Scheduling"
        }


    # --------------------------------------------------------
    # SPECIAL SRTF DETECTION
    # --------------------------------------------------------

    if (
        "srtf" in text
        or "shortest remaining time first" in text
    ):

        return {
            "subject": "Operating Systems",
            "unit": "Unit I",
            "topic": "SRTF Scheduling"
        }


    # --------------------------------------------------------
    # SPECIAL ROUND ROBIN DETECTION
    # --------------------------------------------------------

    if (
        "round robin" in text
        or "round-robin" in text
    ):

        return {
            "subject": "Operating Systems",
            "unit": "Unit I",
            "topic": "Round Robin Scheduling"
        }


    # --------------------------------------------------------
    # SPECIAL DEADLOCK DETECTION
    # --------------------------------------------------------

    if (
        "deadlock" in text
        or "deadlocks" in text
    ):

        return {
            "subject": "Operating Systems",
            "unit": "Unit II",
            "topic": "Deadlocks"
        }


    # --------------------------------------------------------
    # SPECIAL STARVATION DETECTION
    # --------------------------------------------------------

    if (
        "starvation" in text
        and (
            "process" in text
            or "resource" in text
            or "scheduling" in text
            or "deadlock" in text
        )
    ):

        return {
            "subject": "Operating Systems",
            "unit": "Unit II",
            "topic": "Starvation"
        }


    # --------------------------------------------------------
    # GENERAL TOPIC MATCHING
    # --------------------------------------------------------

    best_match = None
    best_score = 0


    for subject, units in TOPIC_RULES.items():

        for unit, topics in units.items():

            for topic in topics:

                topic_words = re.findall(
                    r"[a-zA-Z]+",
                    topic.lower()
                )

                score = 0

                for word in topic_words:

                    if len(word) > 2 and word in text:

                        score += 1


                if score > best_score:

                    best_score = score

                    best_match = {
                        "subject": subject,
                        "unit": unit,
                        "topic": topic
                    }


    if best_match and best_score > 0:

        return best_match


    # --------------------------------------------------------
    # FALLBACK
    # --------------------------------------------------------

    return {
        "subject": "Other",
        "unit": "Unclassified",
        "topic": "Other"
    }


# ============================================================
# FALLBACK KEYWORD GENERATOR
# ============================================================

def generate_fallback_keywords(
    content,
    topic,
    subject
):

    keywords = []

    if subject != "Other":
        keywords.append(subject)

    if topic != "Other":
        keywords.append(topic)

    words = re.findall(
        r"[A-Za-z][A-Za-z0-9-]+",
        content
    )

    stop_words = {

        "the",
        "and",
        "for",
        "with",
        "that",
        "this",
        "from",
        "are",
        "was",
        "were",
        "into",
        "about",
        "students",
        "student",
        "often",
        "always",
        "should",
        "remember",
        "when",
        "then",
        "than",
        "have",
        "has",
        "been",
        "being",
        "their",
        "they",
        "you",
        "your",
        "also",
        "important",
        "good",
        "first",
        "next"
    }


    for word in words:

        word = word.strip().lower()

        if (
            len(word) > 3
            and word not in stop_words
        ):

            formatted = word.capitalize()

            if formatted not in keywords:

                keywords.append(formatted)


        if len(keywords) >= 8:

            break


    return ", ".join(keywords[:8])


# ============================================================
# CLEAN AI KEYWORDS
# ============================================================

def clean_keywords(
    keywords,
    content,
    topic,
    subject
):

    if not keywords:

        return generate_fallback_keywords(
            content,
            topic,
            subject
        )


    if isinstance(keywords, list):

        keywords = ", ".join(
            str(x).strip()
            for x in keywords
            if str(x).strip()
        )


    keywords = str(keywords).strip()


    if not keywords:

        return generate_fallback_keywords(
            content,
            topic,
            subject
        )


    return keywords


# ============================================================
# AI ANALYSIS USING OLLAMA
# ============================================================

def analyze_with_ollama(
    content,
    topic,
    subject
):

    prompt = f"""
You are the AI classification system of EchoMind.

EchoMind is a college-specific knowledge platform.

A senior has submitted this knowledge:

{content}

Detected subject:
{subject}

Detected topic:
{topic}

Classify this knowledge.

Return ONLY valid JSON:

{{
    "category": "Study Tip",
    "difficulty": "Easy",
    "keywords": [
        "keyword1",
        "keyword2",
        "keyword3"
    ]
}}

Allowed categories:

- Study Tip
- Common Mistake
- Concept Explanation
- Exam Strategy
- Project Experience
- Lab Experience
- Career Advice

Allowed difficulty:

- Easy
- Medium
- Hard

Rules:

1. Choose the most appropriate category.

2. Choose Easy, Medium, or Hard.

3. Generate 3 to 8 useful keywords.

4. Keywords should be directly related to the knowledge.

5. Do not invent information.

6. Return ONLY JSON.
"""


    try:

        response = chat(

            model="llama3.2:3b",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )


        result = response.message.content.strip()


        # Remove markdown code fences

        result = result.replace(
            "```json",
            ""
        )

        result = result.replace(
            "```",
            ""
        )

        result = result.strip()


        data = json.loads(result)


        category = data.get(
            "category",
            "Concept Explanation"
        )

        difficulty = data.get(
            "difficulty",
            "Medium"
        )

        keywords = data.get(
            "keywords",
            []
        )


        return {

            "category": category,

            "difficulty": difficulty,

            "keywords": keywords

        }


    except Exception as error:

        print(
            "Ollama analysis error:",
            error
        )


        return {

            "category": "Concept Explanation",

            "difficulty": "Medium",

            "keywords": generate_fallback_keywords(
                content,
                topic,
                subject
            )

        }


# ============================================================
# MAIN KNOWLEDGE ANALYSIS
# ============================================================

def analyze_knowledge(content):

    # --------------------------------------------------------
    # Step 1: Detect syllabus topic
    # --------------------------------------------------------

    syllabus_result = find_topic(content)


    subject = syllabus_result["subject"]

    unit = syllabus_result["unit"]

    topic = syllabus_result["topic"]


    # --------------------------------------------------------
    # Step 2: AI analysis
    # --------------------------------------------------------

    ai_result = analyze_with_ollama(

        content,

        topic,

        subject

    )


    # --------------------------------------------------------
    # Step 3: Clean keywords
    # --------------------------------------------------------

    keywords = clean_keywords(

        ai_result["keywords"],

        content,

        topic,

        subject

    )


    # --------------------------------------------------------
    # Step 4: Final result
    # --------------------------------------------------------

    return {

        "subject": subject,

        "unit": unit,

        "topic": topic,

        "category": ai_result["category"],

        "difficulty": ai_result["difficulty"],

        "keywords": keywords

    }