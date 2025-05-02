# Import Dependancies
import nltk
from nltk.chat.util import Chat, reflections

# Run this command for first run
# nltk.download('punkt')

# Define the chatbot responses
pairs = [
    [
        r"hi|hello|hey|greetings",
        ["Hello! How can I assist you?",]
    ],
    [
        r"my name is (.*)",
        ["Hello %1! How can I help you today?",]
    ],
    [
        r"(.*)how are you ?",
        ["I'm doing great! Thank you for asking.", "I'm just a chatbot. I don't have feelings but I'm here to help.",]
    ],
    [
        r"(.*) your name?",
        ["You can call me Chatbot.",]
    ],
    [
        r"(.*) your age?",
        ["I am just a chatbot, I do not age.",]
    ],
    [
        r"(.*) do for me?",
        ["I can provide information, answer questions, or just have a chat with you.",]
    ],
    [
        r"(.*) can you do?",
        ["I can provide information, answer questions, or just have a chat with you.",]
    ],
    [
        r"(.*) (love|like) you", 
        ["I appreciate that!", "Thank you!", "You are kind."]
    ],
    [
        r"(.*) (love|like|watch|enjoy) sports?", 
        ["I %2 football and cricket!"]
    ],
    [
        r"(.*) sports do you (love|like|watch|enjoy) ?", 
        ["I %2 football and cricket!"]
    ],
    [
        r"(.*) you live?", 
        ["I live inside your computer."]
    ],
    [
        r"(.*) weather in (.*)?",
        ["Weather in %2 is great, like always", "Pleasant weather here in %2", "Its really hot here in %2",
         "Its very pleasant here in %2", "Sorry, I can't give you real-time information about the weather in %2."]
    ],
    [
        r"(.*) (favourite|favorite) (sportsperson|player)?", 
        ["I like Cristiano Ronaldo", "I like Virat Kohli!","I like MS Dhoni!",
         "I like Lionel Messi!","I like Babar Azam!", "I like Neymar Jr.!",
         "I like Sachin Tendulkar!","I like Mbappe!", "I like Shaheen Afridi!",]
    ],
    [
        r"(.*) (help|assist)(.*)", 
        ["How can I help you?", "I am here to assist you."]
    ],
    [
        r"(.*)", 
        ["I'm sorry, I did not understand that.", "Can you please rephrase that?", "Can you ask me a different question?", 
         "I prefer not to answer this.", "I not sure what are you talking about.", "I'm not comfortable answering this question."]
    ],
]

# Create the chatbot
chatbot = Chat(pairs, reflections)

# Define the conversation loop
def chat():
    print("Hello! I am your friendly chatbot. How can I assist you?")
    print("Type 'quit' to exit.")
    print()
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'quit':
            print("\nGoodbye! Have a great day.")
            break
        response = chatbot.respond(user_input)
        print("\nChatbot: ", response)
        print()

# Start the conversation
if __name__ == "__main__":
    chat()