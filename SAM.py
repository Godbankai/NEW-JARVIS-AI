import speech_recognition as sp
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser

# Initialize speech and engine
listener = sp.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    """Convert text to speech"""
    engine.say(text)
    engine.runAndWait()

def wish():
    """Greet the user based on time"""
    hour = datetime.datetime.now().hour
    if hour < 12:
        talk("Good morning!")
    elif hour < 18:
        talk("Good afternoon!")
    else:
        talk("Good evening!")

# Initial Greetings
wish()
talk('Hello user, I am SAM')
print('HELLO USER, I AM SAM\n')
talk('I am a personal assistant of Master Ahqaf Ali')
print('I AM A PERSONAL ASSISTANT OF MASTER AHQAF ALI\n')
talk('How can I help you, Sir?')
print('HOW CAN I HELP YOU, Sir?\n')

def take_command():
    """Listen for user command and convert to text"""
    try:
        with sp.Microphone() as source:
            print("\nListening...")
            listener.adjust_for_ambient_noise(source)  # Reduce background noise
            voice = listener.listen(source)
            command = listener.recognize_google(voice).lower()
            if 'sam' in command:
                command = command.replace('sam', '').strip()
            return command
    except sp.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        talk("Sorry, I couldn't understand that.")
        return ""
    except sp.RequestError:
        print("API unavailable. Check your internet connection.")
        talk("API unavailable. Check your internet connection.")
        return ""
    except Exception as e:
        print(f"Error: {e}")
        talk("An error occurred.")
        return ""

def run_sam():
    """Main function to process commands"""
    command = take_command()
    print(f'Command: {command}')

    if 'play' in command:
        song = command.replace('play', '').strip()
        talk(f'Playing {song}')
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk(f'Current time is {time}')

    elif 'search on wikipedia' in command:
        person = command.replace('search on wikipedia ', '').strip()
        talk(f'Searching Wikipedia for {person}')
        print(f'SAM: Searching Wikipedia for {person}')
        try:
            info = wikipedia.summary(person, sentences=2)
            print(info)
            talk(info)
        except wikipedia.exceptions.DisambiguationError:
            talk("There are multiple results. Please be more specific.")
        except wikipedia.exceptions.PageError:
            talk("Sorry, I couldn't find that page.")

    elif 'search on google' in command:
        query = command.replace('search on google', '').strip()
        talk(f'Searching Google for {query}')
        pywhatkit.search(query)

    elif 'open youtube' in command:
        talk('Opening YouTube, Sir')
        webbrowser.open('https://www.youtube.com')

    elif 'open google' in command:
        talk('Opening Google, Sir')
        webbrowser.open('https://www.google.com')

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)

    elif 'are you single' in command:
        talk('I am in a relationship with WiFi')

    elif 'date with me' in command:
        talk('Sorry, I have a headache')

    elif any(x in command for x in ['quit', 'turn off', 'go to sleep', 'bye', 'goodbye']):
        talk('OK, bye user. Nice to talk to you.')
        print('Shutting Down the server...')
        exit()

    else:
        talk("I don't understand. Maybe I should go to sleep now, wake me if you need help.")

while True:
    run_sam()
