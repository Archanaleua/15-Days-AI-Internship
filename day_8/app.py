print("🤖 AI Chatbot Started!")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot Closed.")
        break

    # Simple AI Responses
    if "hello" in user_input.lower():
        response = "Hello! How can I help you today?"

    elif "your name" in user_input.lower():
        response = "I am an AI Chatbot."

    elif "python" in user_input.lower():
        response = "Python is a powerful programming language."

    elif "machine learning" in user_input.lower():
        response = "Machine Learning helps systems learn from data."

    else:
        response = "Sorry, I am still learning."

    print("\nAI:", response)
    print()