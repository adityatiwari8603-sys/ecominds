from ai import analyze_knowledge


tests = [
    "Students often confuse FCFS Completion Time and Turnaround Time.",
    "In Python, students commonly forget indentation inside if statements.",
    "In a stack, remember that insertion and deletion happen at the top.",
    "Students often make mistakes while solving Fourier series problems.",
    "The Waterfall model is difficult to change once a phase is completed.",
    "Students often confuse SOP and POS forms in Boolean algebra."
]


for i, content in enumerate(tests, start=1):

    result = analyze_knowledge(content)

    print(f"\nTEST {i}")
    print("-" * 50)
    print("Subject :", result["subject"])
    print("Unit    :", result["unit"])
    print("Topic   :", result["topic"])
    print("Category:", result["category"])
    print("Difficulty:", result["difficulty"])
    print("Keywords:", result["keywords"])