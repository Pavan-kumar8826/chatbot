import nltk
import spacy
from nltk.chat.util import Chat, reflections

nlp = spacy.load('en_core_web_sm')

pairs = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am fine, thank you!', 'Doing well, how about you?']),
    (r'what is your name?', ['I am a chatbot created by you.', 'You can call me Chatbot.']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!']),
]

def chatbot():
    print("Hi, I'm your chatbot. Type 'bye' to exit.")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()

def process_input(user_input):
    doc = nlp(user_input)
    for ent in doc.ents:
        print(ent.text, ent.label_)
    for token in doc:
        print(token.text, token.pos_)

while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'goodbye']:
        print("Chatbot: Goodbye!")
        break
    process_input(user_input)
    chatbot()
