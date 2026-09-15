from ai import analyze_knowledge


content = """
Students often confuse Completion Time with Turnaround Time
in FCFS scheduling. Always remember that Turnaround Time is
Completion Time minus Arrival Time.
"""


result = analyze_knowledge(content)

print("AI Analysis:")
print(result)