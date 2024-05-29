from flask import Flask, render_template, request, jsonify
import pyttsx3
import datetime
import wikipedia
import random
import webbrowser
import speech_recognition as sr

app = Flask(__name__)

# Initialize speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 180)
engine.setProperty('voice', engine.getProperty('voices')[1].id)
engine.setProperty('volume', 0.8)

def speak(text):
    """Convert text to speech and print it."""
    engine.say(text)
    engine.runAndWait()
    print(text)

def wish_me():
    """Wish the user according to the time of day."""
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        return 'Good morning! How are you?'
    elif hour < 16:
        return 'Good afternoon! How are you?'
    else:
        return 'Good evening! How are you?'

def search_wikipedia(query, narrate=True):
    """Search Wikipedia and either narrate the summary or open the page."""
    results = wikipedia.summary(query, sentences=1, auto_suggest=False)
    if narrate:
        return 'According to Wikipedia: ' + results
    else:
        page = wikipedia.page(query, auto_suggest=False)
        return page.url

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def handle_command():
    data = request.json
    command = data.get('command', '').lower()

    response = ""

    if 'search' in command:
        if 'wikipedia' in command:
            query = command.replace('wikipedia', '').replace('search', '').strip()
            response = search_wikipedia(query)
        else:
            response = 'Please specify if you want to search in Google, Wikipedia, or YouTube.'
    elif 'your name' in command or 'what is your name' in command:
        response = 'My name is Panda.'
    elif 'hi' in command or 'hello' in command:
        response = 'Hello! How can I help you?'
    elif 'how are you' in command or 'what about you' in command:
        response = 'I am great. Do you need any help?'
    elif 'who created you' in command:
        response = 'I was created by Himanshu Chandola.'
    elif 'introduce yourself' in command or 'who are you' in command:
        response = 'I am Panda, a virtual assistant created by Abarna J, Karthikeyan M and Kisanth R using Python. I am currently in development stage.'
    elif 'who are they' in command:
        response = 'They are the student from KRCT. they created me as a practice project.'
    elif 'thank you' in command or 'thanks' in command:
        response = 'You are welcome! Anything else?'
    elif 'roll' in command and 'dice' in command:
        dice = str(random.randint(1, 6))
        response = 'You got ' + dice
    elif 'quit' in command or 'bye' in command:
        response = 'Bye bye! Thanks for your time'
    elif 'time' in command:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        response = f"The time is {current_time}"
    else:
        response = 'Sorry, that is not assigned. Do you want to search for it?'

    return jsonify(response=response)

if __name__ == '__main__':
    app.run(debug=True)
