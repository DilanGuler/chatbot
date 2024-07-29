import random
import json
import os

# Greetings, farewells, and responses lists
greetings = ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Greetings! How may I help you?"]
farewells = ["Goodbye!", "See you later!", "Take care!"]
default_keywords = ["animal", "book", "game", "movie", "weather", "food", "music", "hobby", "sports", "travel"]
default_responses = [
    "My favorite animal is a horse.",
    "I love reading 'To Kill a Mockingbird'.",
    "I enjoy playing chess.",
    "I'm a big fan of Marvel movies.",
    "Today's weather is sunny and pleasant.",
    "I enjoy Italian cuisine, especially pasta.",
    "Classical music is my favorite.",
    "I like painting in my free time.",
    "I love playing and watching football.",
    "I dream of traveling to Japan one day."
]

# Load keywords and responses from file
def load_data():
    if os.path.exists('chatbot_data.json'):
        with open('chatbot_data.json', 'r') as file:
            data = json.load(file)
        return data['keywords'], data['responses']
    else:
        return default_keywords, default_responses

# Save keywords and responses to file
def save_data(keywords, responses):
    data = {'keywords': keywords, 'responses': responses}
    with open('chatbot_data.json', 'w') as file:
        json.dump(data, file, indent=4)

# Function to get a random greeting
def get_greeting():
    return random.choice(greetings)

# Function to get a random farewell
def get_farewell():
    return random.choice(farewells)

# Function to get a help message
def get_help(keywords):
    help_message = "I can respond to questions about:\n"
    for keyword in sorted(keywords):
        help_message += f"- {keyword.capitalize()}\n"
    help_message += "\nJust type a keyword related to these topics. If I don't understand, you can teach me new keywords and responses!\nType 'bye' to exit.\n"
    return help_message

# Main chatbot function
def chatbot():
    keywords, responses = load_data()
    print(get_greeting())
    print(get_help(keywords))

    user_input = input("How can I help you? (type 'bye' to quit): ").lower()

    while user_input != "bye":
        keyword_found = False

        for index in range(len(keywords)):
            if keywords[index] in user_input:
                print("Bot: " + responses[index])
                keyword_found = True
                break

        if not keyword_found:
            new_keyword = input("I don't understand your keyword. What keyword is it?: ").lower().strip()
            new_response = input("For the new keyword, what response would you like?: ").strip()
            
            # Validate and add new keyword and response
            if new_keyword and new_response:
                keywords.append(new_keyword)
                responses.append(new_response)
                print("Thank you! I've learned something new.")
                save_data(keywords, responses)  # Save the new keyword and response
                print(get_help(keywords))

        user_input = input("How can I help you? (type 'bye' to quit): ").lower()

    print(get_farewell())

# Run the chatbot
if __name__ == "__main__":
    chatbot()

