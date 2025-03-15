import speech_recognition as sr
import os
import webbrowser
import openai
import datetime
import pyttsx3
from config import apikey  # Ensure this file exists with your OpenAI API key

# Initialize OpenAI Client
client = openai.OpenAI(api_key=apikey)

chatStr = ""

def chat(query):
    """Handles chatbot responses using OpenAI API"""
    global chatStr
    print(chatStr)

    chatStr += f"User: {query}\nJarvis: "

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Jarvis AI."},
            {"role": "user", "content": query}
        ],
        temperature=0.7,
        max_tokens=256
    )

    reply = response.choices[0].message.content  # Extract response
    say(reply)
    chatStr += f"{reply}\n"
    return reply

def ai(prompt):
    """Generates AI response and saves it to a file."""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Jarvis AI."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=256
    )

    text = f"OpenAI response for Prompt: {prompt}\n*************************\n\n{response.choices[0].message.content}"

    # Ensure directory exists
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    filename = prompt.replace(" ", "_")[:20]  # Limit filename length
    with open(f"Openai/{filename}.txt", "w") as f:
        f.write(text)

def say(text):
    """Text-to-Speech function."""
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    """Captures voice input and converts it to text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)  # Adjusts for background noise
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()  # Normalize input for better matching
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError as e:
            return f"Could not request results; {e}"
        except Exception as e:
            return f"Error: {e}"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I activated!")

    while True:
        query = takeCommand()

        # Website Shortcuts
        sites = {
            "youtube": "https://www.youtube.com",
            "wikipedia": "https://www.wikipedia.org",
            "google": "https://www.google.com",
            "browser": "https://www.google.com"
        }
        for site, url in sites.items():
            if f"open {site}" in query:
                say(f"Opening {site}, sir...")
                webbrowser.open(url)

        # Play Music (Ensure correct path)
        if "open music" in query:
            musicPath = "C:/Users/YourUsername/Music/sample.mp3"  # Update this path
            if os.path.exists(musicPath):
                os.system(f"start {musicPath}")
            else:
                say("Sorry, the music file was not found.")

        # Tell Time
        elif "the time" in query:
            now = datetime.datetime.now().strftime("%H:%M")
            say(f"Sir, the time is {now}")

        # AI Query Handling
        elif "using artificial intelligence" in query:
            ai(prompt=query)

        # Exit Command
        elif "jarvis quit" in query:
            say("Goodbye, sir!")
            exit()

        # Reset Chat Memory
        elif "reset chat" in query:
            chatStr = ""

        # General Chat
        else:
            print("Chatting...")
            chat(query)
