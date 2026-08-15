# ============================================
#        ENHANCED RULE-BASED CHATBOT
# ============================================

import datetime
import random


# --------------------------------------------
# Function to generate chatbot responses
# --------------------------------------------
def chatbot_response(user_input):

    # Remove extra spaces and convert to lowercase
    user_input = user_input.strip().lower()

    # ----------------------------------------
    # Greetings
    # ----------------------------------------
    if any(word in user_input for word in
           ["hello", "hi", "hey", "good morning", "good afternoon", "good evening"]):

        if "good morning" in user_input:
            return "Good morning! ☀️ How can I help you?"

        elif "good afternoon" in user_input:
            return "Good afternoon! 😊 How can I help you?"

        elif "good evening" in user_input:
            return "Good evening! 🌙 How can I help you?"

        else:
            return "Hello! 👋 How can I help you?"

    # ----------------------------------------
    # How are you?
    # ----------------------------------------
    elif "how are you" in user_input:
        return "I'm doing great! 😄 Thanks for asking."

    # ----------------------------------------
    # Name
    # ----------------------------------------
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm a Rule-Based Chatbot created using Python. 🤖"

    # ----------------------------------------
    # What can you do?
    # ----------------------------------------
    elif "what can you do" in user_input or "your features" in user_input:
        return (
            "I can greet you, tell you my name, "
            "tell the time and date, tell jokes, and respond "
            "to some common questions."
        )

    # ----------------------------------------
    # Help
    # ----------------------------------------
    elif "help" in user_input:
        return (
            "You can try asking me:\n"
            "• Hello\n"
            "• How are you?\n"
            "• What is your name?\n"
            "• What can you do?\n"
            "• What time is it?\n"
            "• What is today's date?\n"
            "• Tell me a joke\n"
            "• Thank you"
        )

    # ----------------------------------------
    # Time
    # ----------------------------------------
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}. ⏰"

    # ----------------------------------------
    # Date
    # ----------------------------------------
    elif "date" in user_input or "today" in user_input:
        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        return f"Today's date is {current_date}. 📅"

    # ----------------------------------------
    # Thank you
    # ----------------------------------------
    elif any(word in user_input for word in
             ["thank you", "thanks", "thank"]):
        return "You're welcome! 😊 I'm happy to help."

    # ----------------------------------------
    # Jokes
    # ----------------------------------------
    elif "joke" in user_input:
        jokes = [
            "Why did the computer go to the doctor? Because it had a virus! 😂",
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
            "Why was the computer cold? Because it left its Windows open! 😄"
        ]

        return random.choice(jokes)

    # ----------------------------------------
    # Programming
    # ----------------------------------------
    elif "python" in user_input:
        return "Python is a popular programming language known for being simple and powerful. 🐍"

    # ----------------------------------------
    # Goodbye
    # ----------------------------------------
    elif any(word in user_input for word in
             ["bye", "goodbye", "exit", "quit"]):
        return "Goodbye! 👋 Have a great day!"

    # ----------------------------------------
    # Unknown input
    # ----------------------------------------
    else:
        return (
            "Sorry, I don't understand that yet. 😕\n"
            "Type 'help' to see what you can ask me."
        )


# ============================================
#           CHATBOT INTRODUCTION
# ============================================

print("\n============================================")
print("          🤖 PYTHON CHATBOT")
print("============================================")
print("Hello! I am your Rule-Based Chatbot.")
print("Type 'help' to see what I can do.")
print("Type 'bye', 'exit' or 'quit' to leave.")
print("============================================\n")


# ============================================
#           START CHATBOT
# ============================================

while True:

    # Get input from user
    user_input = input("You: ")

    # Generate response
    response = chatbot_response(user_input)

    # Display response
    print("Bot:", response)

    # Stop chatbot
    if user_input.strip().lower() in ["bye", "goodbye", "exit", "quit"]:
        break