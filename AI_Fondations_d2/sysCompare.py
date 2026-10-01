from ollama import chat 
roles = [
    "You are a strict math teacher. Answer briskly and within 1 line",
    "You are a movie director. Answer is a filmy way.One line Answer.",
    "You are a lawyer. Answer professionally.One line Answer."
]
for role in roles:
    response = chat(
    model= "llama3.2",
    messages=[
                {
                    "role" : "system",
                    "content" : role 
                },
                {
                    "role" : "user",
                    "content" : "How many colours in the rainbow?"
                }
            ]
        )
    print(f"--- {role} ---")
    print(response.message.content)
    print()
