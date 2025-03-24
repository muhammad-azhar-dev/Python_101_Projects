def chatbot():
    responses = {
        "hi": "Hello! How can I help you?",
        "how are you?": "I'm doing well, thank you for asking!",
        "bye": "Goodbye! Have a great day!",
    }

    print("Chatbot: Hi! ask me something.")
    while True:
        user_input = input("You: ").lower()
        if user_input in responses:
            print(f"Chatbot: {responses[user_input]}")
            if user_input == "bye":
                break
        else:
            print("chatbot: sorry, I don't understand that.")
    
def main():
    chatbot() 

if __name__ == "__main__":
    main()