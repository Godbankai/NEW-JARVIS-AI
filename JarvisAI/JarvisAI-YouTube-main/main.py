import speech_recognition as sr
import os
import webbrowser
import openai
from config import apikey
import datetime
import pyttsx3

chatStr = ""

import openai

def chat(query):
    global chatStr
    print(chatStr)
    
    client = openai.Client(api_key=apikey)  # Correct way to initialize OpenAI client
    
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

    reply = response.choices[0].message.content  # Extract the response
    say(reply)
    chatStr += f"{reply}\n"
    return reply


def ai(prompt):
    openai_client = openai.OpenAI(api_key=apikey)
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are Jarvis AI."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=256
    )

    text += response.choices[0].message.content
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip() }.txt", "w") as f:
        f.write(text)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"], ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])
        
        if "open music" in query:
            musicPath = "C:/Users/trive/Music/sample.mp3"  # Update to a valid music file path
            os.system(f"start {musicPath}")

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            say(f"Sir, the time is {hour} bajke {min} minutes")

        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""
        else:
            print("Chatting...")
            chat(query)
