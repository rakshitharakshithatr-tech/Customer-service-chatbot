print("🤖 Customer Service Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! Welcome to our customer service. How can I help you?")

    elif "hours" in user or "working" in user:
        print("Bot: Our working hours are 9 AM to 6 PM.")

    elif "contact" in user:
        print("Bot: You can contact our support team through email.")

    elif "order" in user:
        print("Bot: Please provide your order ID to check your order status.")

    elif "refund" in user:
        print("Bot: Refund requests are processed within 5-7 working days.")

    elif "thank" in user:
        print("Bot: You're welcome! 😊")

    elif user == "bye":
        print("Bot: Thank you for contacting us. Have a nice day!")
        break

    else:
        print("Bot: Sorry, I didn't understand. Please ask another question.")
