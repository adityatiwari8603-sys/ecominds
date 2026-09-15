import re

from ollama import chat

from database import get_connection

from sjf import sjf_non_preemptive
from fcfs import fcfs_scheduling
from rr import round_robin_scheduling

from scheduling_parser import (
    parse_sjf_question,
    parse_fcfs_question,
    parse_rr_question,
)


# ============================================================
# 1. SEARCH RELEVANT COLLEGE KNOWLEDGE
# ============================================================

def search_relevant_knowledge(question):
    """Search the college knowledge database and rank relevant entries."""

    conn = get_connection()
    cursor = conn.cursor()

    q = (question or "").lower().strip()

    topic_aliases = {  
        "fcfs": "FCFS Scheduling",
        "first come first serve": "FCFS Scheduling",
        "sjf": "SJF Scheduling",
        "shortest job first": "SJF Scheduling",
        "round robin": "Round Robin Scheduling",
        "rr scheduling": "Round Robin Scheduling",
        "deadlock": "Deadlock",
        "deadlocks": "Deadlock",
        "starvation": "Starvation",
        "binary search": "Binary Search",
        "linear search": "Linear Search",
        "stack": "Stack",
        "queue": "Queue",
        "fourier series": "Fourier Series",
        "fourier": "Fourier Series",
        "srs": "SRS",
        "software requirement specification": "SRS",
        "k-map": "K-Map Simplification",
        "kmap": "K-Map Simplification",
        "boolean simplification": "K-Map Simplification",
        "python indentation": "Python Common Mistake",
        "indentation": "Python Common Mistake",
        "python function": "Python Function Exam Tip",
        "python functions": "Python Function Exam Tip",
    }

    exact_topic = None

    for alias, topic in topic_aliases.items():
        if alias in q:
            exact_topic = topic
            break

    # CPU scheduling intent.
    cpu_scheduling = any(
        phrase in q
        for phrase in [
            "fcfs",
            "first come first serve",
            "sjf",
            "shortest job first",
            "round robin",
            "rr scheduling",
            "cpu scheduling",
            "process scheduling",
            "cpu scheduling algorithm",
        ]
    )

    # Disk scheduling intent.
    disk_scheduling = any(
        phrase in q
        for phrase in [
            "disk scheduling",
            "disk fcfs",
            "disk sjf",
            "disk scheduling algorithm",
            "head movement",
            "disk queue",
            "cylinder",
            "seek time",
            "sstf",
            "scan scheduling",
            "c-scan",
            "look scheduling",
            "c-look",
        ]
    )

    normalized_question = re.sub(
        r"\b(what|is|are|the|a|an|of|in|on|to|for|and|or|how|why|do|does|can|could|explain|define|tell|me|about)\b",
        " ",
        q,
    )

    normalized_question = re.sub(
        r"[^a-z0-9\s]",
        " ",
        normalized_question,
    )

    normalized_question = re.sub(
        r"\s+",
        " ",
        normalized_question,
    ).strip()

    words = re.findall(
        r"[a-zA-Z0-9]+",
        normalized_question,
    )

    stop_words = {
        "what", "is", "are", "the", "a", "an", "of", "in", "on",
        "to", "for", "and", "or", "how", "why", "do", "does",
        "should", "i", "we", "can", "be", "with", "from", "this",
        "that", "common", "mistake", "mistakes", "students", "please",
        "explain", "define", "tell", "me", "about",
    }

    keywords = [
        word
        for word in words
        if word not in stop_words and len(word) > 2
    ]

    conditions = []
    values = []

    searchable_columns = [
        "title",
        "content",
        "subject",
        "unit",
        "topic",
        "category",
        "keywords",
    ]

    for word in keywords:
        word_conditions = []

        for column in searchable_columns:
            word_conditions.append(
                f"LOWER(COALESCE({column}, '')) LIKE ?"
            )
            values.append(f"%{word}%")

        conditions.append(
            "(" + " OR ".join(word_conditions) + ")"
        )

    if exact_topic:
        conditions.append(
            "LOWER(topic) = LOWER(?)"
        )
        values.append(exact_topic)

    if conditions:
        sql = f"""
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
                helpful
            FROM knowledge
            WHERE {" OR ".join(conditions)}
            LIMIT 100
        """

        cursor.execute(sql, values)
        results = cursor.fetchall()
    else:
        results = []

    knowledge = []

    for row in results:
        item = {
            "id": row[0],
            "title": row[1],
            "content": row[2],
            "subject": row[3],
            "unit": row[4],
            "topic": row[5],
            "category": row[6],
            "difficulty": row[7],
            "keywords": row[8],
            "author": row[9],
            "helpful": row[10],
        }

        score = 0

        title = (item["title"] or "").lower()
        content = (item["content"] or "").lower()
        subject = (item["subject"] or "").lower()
        unit = (item["unit"] or "").lower()
        topic = (item["topic"] or "").lower()
        category = (item["category"] or "").lower()
        item_keywords = (item["keywords"] or "").lower()

        searchable_text = " ".join([
            title,
            content,
            subject,
            unit,
            topic,
            category,
            item_keywords,
        ])

        if exact_topic and topic == exact_topic.lower():
            score += 300

        # CPU scheduling protection.
        if cpu_scheduling and not disk_scheduling:
            if (
                "cpu scheduling" in searchable_text
                or "process scheduling" in searchable_text
            ):
                score += 250

            if "fcfs" in q:
                if "fcfs scheduling" in searchable_text:
                    score += 350
                if "disk fcfs" in searchable_text:
                    score -= 500

            if "sjf" in q or "shortest job first" in q:
                if "sjf scheduling" in searchable_text:
                    score += 350
                if "disk sjf" in searchable_text:
                    score -= 500

            if "round robin" in q or "rr scheduling" in q:
                if "round robin scheduling" in searchable_text:
                    score += 350

            for term in [
                "disk scheduling",
                "disk fcfs",
                "disk sjf",
                "head movement",
                "seek time",
                "cylinder",
                "sstf",
                "scan scheduling",
                "c-scan",
                "look scheduling",
                "c-look",
            ]:
                if term in searchable_text:
                    score -= 300

        # Explicit disk scheduling protection.
        if disk_scheduling:
            if "disk scheduling" in searchable_text:
                score += 300
            if "head movement" in searchable_text:
                score += 150
            if "seek time" in searchable_text:
                score += 150
            if "cylinder" in searchable_text:
                score += 150
            if "disk fcfs" in searchable_text and "fcfs" in q:
                score += 400
            if "disk sjf" in searchable_text and "sjf" in q:
                score += 400

        if title == q:
            score += 150

        title_clean = re.sub(
            r"\b(what|is|are|the|a|an|of|in|on|to|for|and|or|how|why|do|does|explain|define)\b",
            " ",
            title,
        )

        title_clean = re.sub(
            r"[^a-z0-9\s]",
            " ",
            title_clean,
        )

        title_clean = re.sub(
            r"\s+",
            " ",
            title_clean,
        ).strip()

        if title_clean and title_clean == normalized_question:
            score += 120

        for word in keywords:
            if word in title:
                score += 15
            if word in topic:
                score += 10
            if word in subject:
                score += 7
            if word in item_keywords:
                score += 6
            if word in unit:
                score += 3
            if word in category:
                score += 3
            if word in content:
                score += 2

        item["score"] = score
        knowledge.append(item)

    knowledge.sort(
        key=lambda x: (
            x["score"],
            x.get("helpful", 0),
            x["id"],
        ),
        reverse=True,
    )

    conn.close()

    return knowledge[:20]


# ============================================================
# 2. AI SOURCE RANKING
# ============================================================
def rank_knowledge(question, knowledge):
    """Rank college knowledge with strong topic protection."""

    if not knowledge:
        return []

    q = (question or "").lower().strip()

    cpu_scheduling = any(
        phrase in q
        for phrase in [
            "fcfs",
            "first come first serve",
            "sjf",
            "shortest job first",
            "round robin",
            "rr scheduling",
            "cpu scheduling",
            "process scheduling",
        ]
    )

    disk_scheduling = any(
        phrase in q
        for phrase in [
            "disk scheduling",
            "disk fcfs",
            "disk sjf",
            "head movement",
            "disk queue",
            "cylinder",
            "seek time",
            "sstf",
            "scan scheduling",
            "c-scan",
            "look scheduling",
            "c-look",
        ]
    )

    topic_phrases = [
        phrase
        for phrase in [
            "deadlock",
            "euler's theorem",
            "euler theorem",
            "homogeneous function",
            "nand gate",
            "binary search",
            "linear search",
            "operating system",
            "software engineering",
            "digital electronics",
            "mathematics iii",
            "data structures",
            "round robin",
            "shortest job first",
            "first come first serve",
            "fcfs",
            "sjf",
        ]
        if phrase in q
    ]

    question_words = set(
        re.findall(
            r"[a-zA-Z0-9']+",
            q,
        )
    )

    stop_words = {
        "what", "is", "are", "the", "a", "an", "of", "in", "on",
        "for", "to", "and", "or", "with", "how", "why", "does",
        "do", "this", "that", "define", "explain", "give", "me",
        "tell", "about", "example", "numerical",
    }

    question_words -= stop_words

    scored_sources = []

    for item in knowledge:

        title = (item.get("title") or "").lower()
        subject = (item.get("subject") or "").lower()
        topic = (item.get("topic") or "").lower()
        category = (item.get("category") or "").lower()
        keywords = (item.get("keywords") or "").lower()
        content = (item.get("content") or "").lower()

        searchable_text = " ".join([
            title,
            subject,
            topic,
            category,
            keywords,
            content,
        ])

        score = item.get("score", 0)

        # ----------------------------------------------------
        # DEADLOCK TOPIC PROTECTION
        # ----------------------------------------------------

        if "deadlock" in q:

            if topic == "deadlock":
                score += 1000

            if "deadlock in operating systems" in title:
                score += 900

            if "mutual exclusion" in searchable_text:
                score += 300

            if "hold and wait" in searchable_text:
                score += 300

            if "no preemption" in searchable_text:
                score += 300

            if "circular wait" in searchable_text:
                score += 300

        # ----------------------------------------------------
        # CPU SCHEDULING
        # ----------------------------------------------------

        if cpu_scheduling and not disk_scheduling:

            if "cpu scheduling" in searchable_text:
                score += 500

            if "process scheduling" in searchable_text:
                score += 500

            if (
                "fcfs" in q
                or "first come first serve" in q
            ):

                if "fcfs scheduling" in searchable_text:
                    score += 700

                if topic == "fcfs scheduling":
                    score += 800

                if "disk fcfs" in searchable_text:
                    score -= 1000

            if (
                "sjf" in q
                or "shortest job first" in q
            ):

                if "sjf scheduling" in searchable_text:
                    score += 700

                if topic == "sjf scheduling":
                    score += 800

                if "disk sjf" in searchable_text:
                    score -= 1000

            if (
                "round robin" in q
                or "rr scheduling" in q
            ):

                if "round robin scheduling" in searchable_text:
                    score += 700

                if topic == "round robin scheduling":
                    score += 800

            disk_terms = [
                "disk scheduling",
                "disk fcfs",
                "disk sjf",
                "head movement",
                "seek time",
                "cylinder",
                "sstf",
                "scan scheduling",
                "c-scan",
                "look scheduling",
                "c-look",
            ]

            for term in disk_terms:

                if term in searchable_text:
                    score -= 700

        # ----------------------------------------------------
        # DISK SCHEDULING
        # ----------------------------------------------------

        if disk_scheduling:

            if "disk scheduling" in searchable_text:
                score += 600

            if "head movement" in searchable_text:
                score += 400

            if "seek time" in searchable_text:
                score += 300

            if "cylinder" in searchable_text:
                score += 300

            if (
                "disk fcfs" in searchable_text
                and "fcfs" in q
            ):
                score += 800

            if (
                "disk sjf" in searchable_text
                and "sjf" in q
            ):
                score += 800

        # ----------------------------------------------------
        # TOPIC PHRASES
        # ----------------------------------------------------

        for phrase in topic_phrases:

            if phrase in title:
                score += 250

            if phrase in topic:
                score += 300

            if phrase in keywords:
                score += 150

            if phrase in content:
                score += 20

        # ----------------------------------------------------
        # GENERAL MATCHING
        # ----------------------------------------------------

        for word in question_words:

            if len(word) >= 3 and word in title:
                score += 40

            if len(word) >= 3 and word in topic:
                score += 30

            if len(word) >= 3 and word in keywords:
                score += 25

            if len(word) >= 4 and word in category:
                score += 10

        content_matches = sum(
            1
            for word in question_words
            if len(word) >= 5 and word in content
        )

        score += min(
            content_matches * 2,
            6,
        )

        item_copy = dict(item)
        item_copy["score"] = score

        scored_sources.append(item_copy)

    scored_sources.sort(
        key=lambda item: (
            item.get("score", 0),
            item.get("helpful", 0),
            item.get("id", 0),
        ),
        reverse=True,
    )

    relevant_sources = [
        item
        for item in scored_sources
        if item.get("score", 0) >= 25
    ]

    return relevant_sources[:5]

# ============================================================
# 3. ACCURACY GUARD
# ============================================================

def accuracy_guard(answer, question):
    """Protect against common scheduling mistakes."""

    q = (question or "").lower()

    if "fcfs" in q or "first come first serve" in q:
        answer = answer.replace(
            "Completion Time (CT) = Turnaround Time (TAT)",
            "Completion Time (CT) is not always equal to Turnaround Time (TAT).",
        )

        answer = answer.replace(
            "CT = TAT",
            "CT is not always equal to TAT.",
        )

    return answer


# ============================================================
# 4. SHARED SCHEDULING TABLE HELPER
# ============================================================

def _format_scheduling_result(results, algorithm_name):

    rows = []

    for item in results:
        process_name = (
            item.get("name")
            or item.get("pid")
            or item.get("process")
            or ""
        )

        arrival_time = (
            item.get("arrival")
            if item.get("arrival") is not None
            else item.get("arrival_time", 0)
        )

        burst_time = (
            item.get("burst")
            if item.get("burst") is not None
            else item.get("burst_time", 0)
        )

        completion_time = (
            item.get("completion")
            if item.get("completion") is not None
            else item.get("completion_time", 0)
        )

        turnaround_time = completion_time - arrival_time
        waiting_time = turnaround_time - burst_time

        rows.append({
            "process": process_name,
            "arrival_time": arrival_time,
            "burst_time": burst_time,
            "completion_time": completion_time,
            "turnaround_time": turnaround_time,
            "waiting_time": waiting_time,
        })

    if not rows:
        return f"Unable to calculate {algorithm_name} scheduling."

    average_waiting_time = (
        sum(row["waiting_time"] for row in rows)
        / len(rows)
    )

    average_turnaround_time = (
        sum(row["turnaround_time"] for row in rows)
        / len(rows)
    )

    table = [
        "| Process | AT | BT | CT | TAT | WT |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    for row in rows:
        table.append(
            f"| {row['process']} | "
            f"{row['arrival_time']} | "
            f"{row['burst_time']} | "
            f"{row['completion_time']} | "
            f"{row['turnaround_time']} | "
            f"{row['waiting_time']} |"
        )

    return (
        f"## {algorithm_name} Scheduling Numerical Solution\n\n"
        "### Process Details\n\n"
        + "\n".join(table)
        + "\n\n"
        "### Average Waiting Time\n\n"
        f"{average_waiting_time:.2f}\n\n"
        "### Average Turnaround Time\n\n"
        f"{average_turnaround_time:.2f}\n\n"
        "### Formulas\n\n"
        "Turnaround Time (TAT) = Completion Time (CT) - Arrival Time (AT)\n\n"
        "Waiting Time (WT) = Turnaround Time (TAT) - Burst Time (BT)"
    )


# ============================================================
# 5. SOLVE SJF
# ============================================================

def solve_sjf_question(processes):

    answer = _format_scheduling_result(
        sjf_non_preemptive(processes),
        "SJF",
    )

    return answer + (
        "\n\n### SJF Rule\n\n"
        "SJF selects the shortest burst-time process from the "
        "processes that have already arrived. SJF is non-preemptive, "
        "so once a process starts, it continues until completion."
    )


# ============================================================
# 6. SOLVE FCFS
# ============================================================

def solve_fcfs_question(processes):

    answer = _format_scheduling_result(
        fcfs_scheduling(processes),
        "FCFS",
    )

    return answer + (
        "\n\n### FCFS Rule\n\n"
        "FCFS stands for First Come First Serve. The process "
        "that arrives first gets the CPU first. FCFS is normally "
        "non-preemptive."
    )


# ============================================================
# 7. SOLVE ROUND ROBIN
# ============================================================
def solve_rr_question(processes, quantum):

    if quantum is None:
        return "Please provide the time quantum for Round Robin."

    if quantum <= 0:
        return "Time quantum must be greater than zero."

    rr_result = round_robin_scheduling(
        processes,
        quantum,
    )

    completed_processes = rr_result.get(
        "processes",
        [],
    )

    answer = _format_scheduling_result(
        completed_processes,
        "Round Robin",
    )

    timeline = rr_result.get(
        "timeline",
        [],
    )

    gantt_parts = []

    for segment in timeline:

        gantt_parts.append(
            f"{segment.get('process', '')} "
            f"({segment.get('start', 0)}-{segment.get('end', 0)})"
        )

    gantt_chart = (
        " → ".join(gantt_parts)
        if gantt_parts
        else "Not available"
    )

    return (
        "## Round Robin Scheduling Numerical Solution\n\n"
        f"### Time Quantum\n\n{quantum}\n\n"
        + answer.replace(
            "## Round Robin Scheduling Numerical Solution\n\n",
            "",
            1,
        )
        + "\n\n"
        "### Gantt Chart\n\n"
        f"{gantt_chart}\n\n"
        "### Round Robin Rule\n\n"
        "Round Robin is a preemptive scheduling algorithm. Each "
        "process receives CPU time for a fixed time quantum. If it "
        "does not finish within that quantum, it goes to the back "
        "of the ready queue."
    )


# ============================================================
# 8. REPAIR SCHEDULING TABLE
# ============================================================

def repair_scheduling_table(answer):

    if not answer:
        return answer

    replacements = {
        "Process AT BT CT TAT WT":
            "Process | AT | BT | CT | TAT | WT",
        "ProcessATBTCTTATWT":
            "Process | AT | BT | CT | TAT | WT",
        "|Process|AT|BT|CT|TAT|WT|":
            "| Process | AT | BT | CT | TAT | WT |",
    }

    for old, new in replacements.items():
        answer = answer.replace(old, new)

    return answer


# ============================================================
# 9. SPECIAL BANKER'S ALGORITHM PROTECTION
# ============================================================

def _is_bankers_question(question):

    q = (question or "").lower()

    return (
        "banker" in q
        or "banker's" in q
        or "bankers" in q
    )


def _bankers_guard(answer, question):

    if not _is_bankers_question(question):
        return answer

    q = question.lower()

    has_matrix_data = (
        "allocation" in q
        or "max" in q
        or "maximum" in q
        or "available" in q
        or "need matrix" in q
    )

    if not has_matrix_data:
        return (
            "## Banker's Algorithm\n\n"
            "Banker's Algorithm checks whether a resource-allocation "
            "state is safe before granting resources.\n\n"
            "To solve a numerical Banker problem, provide the "
            "Allocation matrix, Maximum matrix, and Available vector. "
            "Without those values, a specific safe sequence cannot be "
            "calculated reliably."
        )

    return answer


# ============================================================
# 10. SCHEDULING NUMERICAL DETECTION
# ============================================================

def _looks_like_scheduling_numerical(question):

    q = (question or "").lower()

    scheduling_words = [
        "fcfs",
        "first come first serve",
        "sjf",
        "shortest job first",
        "round robin",
        "rr scheduling",
    ]

    has_algorithm = any(
        word in q
        for word in scheduling_words
    )

    has_process = bool(
        re.search(
            r"\bp\d+\b",
            q,
            re.IGNORECASE,
        )
    )

    has_arrival = bool(
        re.search(
            r"\barrival\s*time\b",
            q,
            re.IGNORECASE,
        )
        or re.search(
            r"\barrival\b",
            q,
            re.IGNORECASE,
        )
        or re.search(
            r"\bat\b",
            q,
            re.IGNORECASE,
        )
    )

    has_burst = bool(
        re.search(
            r"\bburst\s*time\b",
            q,
            re.IGNORECASE,
        )
        or re.search(
            r"\bburst\b",
            q,
            re.IGNORECASE,
        )
        or re.search(
            r"\bbt\b",
            q,
            re.IGNORECASE,
        )
    )

    return (
        has_algorithm
        and has_process
        and has_arrival
        and has_burst
    )


# ============================================================
# 11. GENERATE ANSWER
# ============================================================

def generate_answer(question):

    question = (question or "").strip()

    if not question:
        return {
            "answer": "Please enter a question.",
            "sources": [],
        }

    # --------------------------------------------------------
    # Scheduling numerical questions
    # --------------------------------------------------------

    if _looks_like_scheduling_numerical(question):

        q = question.lower()

        try:
            scheduling_knowledge = search_relevant_knowledge(
                "Operating Systems scheduling CPU scheduling"
            )

            scheduling_sources = rank_knowledge(
                "Operating Systems scheduling CPU scheduling",
                scheduling_knowledge,
            )

            scheduling_sources = scheduling_sources[:1]

            clean_scheduling_sources = []

            for item in scheduling_sources:
                clean_scheduling_sources.append({
                    "id": item.get("id"),
                    "title": item.get("title"),
                    "subject": item.get("subject"),
                    "unit": item.get("unit"),
                    "topic": item.get("topic"),
                    "category": item.get("category"),
                    "difficulty": item.get("difficulty"),
                    "keywords": item.get("keywords"),
                    "author": item.get("author"),
                    "content": item.get("content"),
                    "score": item.get("score", 0),
                })

            if (
                "fcfs" in q
                or "first come first serve" in q
            ):
                processes = parse_fcfs_question(question)

                if processes:
                    answer = solve_fcfs_question(processes)

                    return {
                        "answer": accuracy_guard(
                            answer,
                            question,
                        ),
                        "sources": clean_scheduling_sources,
                    }

            if (
                "sjf" in q
                or "shortest job first" in q
            ):
                processes = parse_sjf_question(question)

                if processes:
                    answer = solve_sjf_question(processes)

                    return {
                        "answer": accuracy_guard(
                            answer,
                            question,
                        ),
                        "sources": clean_scheduling_sources,
                    }

            if (
                "round robin" in q
                or "rr scheduling" in q
            ):
                processes, quantum = parse_rr_question(question)

                if (
                    processes
                    and quantum is not None
                ):
                    answer = solve_rr_question(
                        processes,
                        quantum,
                    )

                    return {
                        "answer": accuracy_guard(
                            answer,
                            question,
                        ),
                        "sources": clean_scheduling_sources,
                    }

        except Exception as exc:
            return {
                "answer": (
                    "EchoMind could not solve this scheduling problem.\n\n"
                    f"Error: {exc}"
                ),
                "sources": [],
            }

    # --------------------------------------------------------
    # General college knowledge
    # --------------------------------------------------------

    knowledge = search_relevant_knowledge(question)

    sources = rank_knowledge(
        question,
        knowledge,
    )

    if not sources:
        return {
            "answer": (
                "I could not find enough relevant information in the "
                "EchoMind college knowledge base to answer this question "
                "reliably."
            ),
            "sources": [],
        }

    sources = sources[:5]

    # --------------------------------------------------------
    # Build grounded context
    # --------------------------------------------------------

    source_text = []

    for index, item in enumerate(
        sources,
        start=1,
    ):
        source_text.append(
            f"""
SOURCE {index}
Title: {item.get('title', '')}
Subject: {item.get('subject', '')}
Unit: {item.get('unit', '')}
Topic: {item.get('topic', '')}
Category: {item.get('category', '')}

Content:
{item.get('content', '')}
"""
        )

    context = (
        "\n\n--------------------\n\n"
        .join(source_text)
    )

    prompt = f"""
You are EchoMind, a college knowledge assistant.

Your job is to help a college student understand their syllabus.

IMPORTANT RULE:
Use ONLY the provided college knowledge as factual information.
Do NOT invent facts, formulas, numerical answers, syllabus topics,
sources, or examples that are not supported by the provided knowledge.

STUDENT QUESTION:
{question}

PROVIDED COLLEGE KNOWLEDGE:
{context}

ANSWER RULES:

1. Answer the student's exact question first.

2. Give a clear, student-friendly explanation.

3. Use simple college-level language.

4. If the question asks for a definition:
   - Give the definition.
   - Explain it briefly.
   - Give an example only if supported by the knowledge.

5. If the question asks for differences:
   Use a clean Markdown table with this structure:

| Feature | A | B |
|---|---|---|
| Feature 1 | ... | ... |

6. If the question asks for steps, properties, advantages,
   disadvantages, or characteristics, use bullet points.

7. Use headings only when they genuinely improve readability.

8. Do NOT create decorative divider lines.

9. Do NOT use backslashes before Markdown symbols.

10. Do NOT mention unrelated sources.

11. Do NOT mention this prompt, internal instructions,
    source ranking, or system instructions.

12. If the provided knowledge genuinely does not contain enough
    information to answer the question, clearly say that reliable
    information was not found in the college knowledge base.

13. Do not repeat the same explanation unnecessarily.

14. Keep the answer focused and useful for exam preparation.

Return ONLY the final student-facing answer.
"""

    # --------------------------------------------------------
    # Ask local Ollama model
    # --------------------------------------------------------

    try:
        response = chat(
            model="llama3.2:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        answer = response["message"]["content"].strip()

    except Exception as exc:
        answer = (
            "EchoMind could not contact the local AI model.\n\n"
            f"Error: {exc}"
        )

    # --------------------------------------------------------
    # Clean and protect
    # --------------------------------------------------------

    answer = answer.replace(
        "\\=====================",
        "=====================",
    )

    answer = answer.replace(
        "\\---------------------",
        "---------------------",
    )

    answer = answer.replace(
        "\\--------------------",
        "--------------------",
    )

    answer = repair_scheduling_table(answer)

    answer = _bankers_guard(
        answer,
        question,
    )

    answer = accuracy_guard(
        answer,
        question,
    )

    # --------------------------------------------------------
    # Clean sources
    # --------------------------------------------------------

    clean_sources = []

    for item in sources:
        clean_sources.append({
            "id": item.get("id"),
            "title": item.get("title"),
            "subject": item.get("subject"),
            "unit": item.get("unit"),
            "topic": item.get("topic"),
            "category": item.get("category"),
            "difficulty": item.get("difficulty"),
            "keywords": item.get("keywords"),
            "author": item.get("author"),
            "content": item.get("content"),
            "score": item.get("score", 0),
        })

    return {
        "answer": answer,
        "sources": clean_sources,
    }
