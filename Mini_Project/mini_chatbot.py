from ollama import chat

system_msg = "You are my friendly tutor. Answer in warm tones. Answer in one sentence."

history = [{"role" : "system", "content" : system_msg}]
question_counter = 0


print("Madhu 🤖: Welcome user!!")
while True:
    question = input("You:")
    if question == "":
        print("Madhu 🤖: Please try something.")
        continue
    if question.lower().strip() == "/history":
        print("----- Your Conversation so far -----")
        if len(history) < 2:
            print("Nothing so far!")
        for msg in history[1:]:
            if msg.role == "user":
                speaker = "You"
            else:
                speaker = "Madhu 🤖"
            print(f"{speaker}: {msg.content}")
            print("-------------------------------")
            print()
            continue
    if question.lower().strip() =="/clear":
        history = [{"role" : "system", "content" : system_msg}]
        print("your history is cleared.Start a fresh conversation ")
        print()
        continue
    if question.lower().strip() == "/help":
        print("----Available commanda----")
        print("/history - displays conversation history")
        print("/clear - clears chat history")
        print("/help - displays this list")
        print("exit - quits the chatbot")
        print("------------------------------")
        print()
        continue
    if question.lower().strip() == "/personality":
        print("1. Friendly Tutor")
        print("2. Funny Comedian")
        print("3. Strict Teacher")

        choice = input("Choose personality: ")

        if choice == "1":
            system_msg = "You are a friendly tutor. Answer in one sentence."
        elif choice == "2":
            system_msg = "You are a funny comedian. Answer in one sentence."
        elif choice == "3":
            system_msg = "You are a strict teacher. Answer in one sentence."
        else:
            print("Invalid choice!")
            continue

    history[0] = [{"role": "system", "content": system_msg}]
    print("Madhu 🤖: Personality changed successfully!")
    continue

    if question.lower().strip() == "exit":
        print("Madhu 🤖: GoodBye user.Please come back soon!😘")
        print(f"You asked {question_counter} questions today. Good Job!")
        break
    history.append({"role" : "system", "content" : question})
    question_counter += 1
    try:
        response = chat(
                model="llama3.2",
                messages = history
            )
        reply = response.message.content
        history.append({"role" : "system", "content" : reply})
        print(f"Madhu 🤖:{reply}")
        print()
    except Exception as e:
        print("Unknown issue.Is Ollama running?")