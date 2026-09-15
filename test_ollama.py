from ollama import chat

response = chat(
    model="llama3.2:3b",
    messages=[
        {
            "role": "user",
            "content": "What is FCFS scheduling? Explain in simple words."
        }
    ]
)

print(response.message.content)