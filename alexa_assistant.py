import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import pyjokes
import random
import sys
import os

# Terminal colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'

listener = sr.Recognizer()

# Speak text using macOS 'say'
def engine_talk(text):
    plain_text = text.replace(RED, "").replace(GREEN, "").replace(YELLOW, "").replace(RESET, "")
    plain_text = plain_text.replace('"', '')  # Remove double quotes
    print(YELLOW + "Assistant:", text + RESET)
    os.system(f"say '{plain_text}'")


# Listen for voice command
def get_command():
    try:
        with sr.Microphone() as source:
            print(RED + "Listening..." + RESET)
            listener.adjust_for_ambient_noise(source, duration=0.5)
            listener.pause_threshold = 1.5  # Waits 1 second after you stop talking
            audio = listener.listen(source)
            command = listener.recognize_google(audio)
            return command.lower().strip()
    except (sr.WaitTimeoutError, sr.UnknownValueError):
        return ""
    except sr.RequestError:
        engine_talk(RED + "Speech recognition service issue." + RESET)
        return ""


def clean_command(command):
    filler_phrases = [
        "oh yeah", "by the way", "so", "and", "then", "well", "okay", "ok" , "based on that", 
        "you know", "actually", "just", "though", "like", "um", "uh", "ah", "hmm", "let's see",
        "can you", "speaking of", "which", 
    ]
    for phrase in filler_phrases:
        command = command.replace(phrase, "")
    return command.strip()


# Handle commands
def run_alexa():
    """
    run_alexa()

    This function listens to the user's voice command, processes it,
    and performs actions based on recognized keywords.

    Examples of commands:

    1. Play song (YouTube): "play despacito"
    2. Greetings: "hello", "good morning"
    3. Ask how the assistant is: "how are you"
    4. Thanking the assistant: "thank you", "thanks"
    5. Ask the assistant's name: "what's your name"
    6. Ask who made the assistant: "who created you"
    7. Ask what the assistant can do: "what can you do"
    8. Get current time: "what time is it", "time"
    9. Get current date: "what's the date today", "date"
    10. Tell a joke: "tell me a joke", "joke"
    11. Define a term: "define quantum physics"
    12. Answer general knowledge (who/where): "who is Albert Einstein", "where is Germany"
    13. Basic math calculations: "calculate 5 plus 3", "what is 10 divided by 2"
    14. Exit the program: "exit", "quit", "stop"

    If a command is not recognized, the assistant replies with: 
    "Sorry, I didn't understand that command."
    """

    command = get_command()
    if not command:
        return

    print(GREEN + "User:", command + RESET)
    command = clean_command(command)


    # Play song
    if command.startswith("play"):
        song = command.replace('play', '').strip()
        if song:
            engine_talk(f"Playing {song}")
            pywhatkit.playonyt(song)
        else:
            engine_talk("What do you want me to play?")
        
    #Greetings
    elif any(greet in command for greet in ["hello", "hi", "hey", "good morning", "good evening", "good afternoon"]):
        responses = [
            "Hello! How can I help you today?",
            "Hi there! What would you like me to do?",
            "Hey! I'm ready to assist.",
            "Good to hear from you! Need anything?",
            "Hi! Let me know how I can assist you."
        ]
        engine_talk(random.choice(responses))
    # How are you
    elif "how are you" in command:
        engine_talk("I'm just a bunch of code, but I'm doing great! How about you?")

# Thanks / thank you
    elif any(phrase in command for phrase in ["thanks", "thank you"]):
        engine_talk("You're welcome!")


    # What's your name
    elif "your name" in command:
        engine_talk("I'm your virtual assistant. You can call me anything you like.")

    # Who made you
    elif any(phrase in command for phrase in ["who made", "who created", "who's your creator", "who built you"]):
        engine_talk("I was created by a curious developer!")
    

# What can you do
elif "what can you do" in command:
    responses = [
        "I can play music, tell jokes, give you the time or date, calculate math, and answer general questions.",
        "I'm here to help with music, jokes, time, math, and more.",
        "I can assist you with calculations, funny jokes, and playing songs—just ask!",
        "My skills include telling jokes, providing time or date, doing math, and answering questions."
    ]
    engine_talk(random.choice(responses))

    # Time
    elif "time" in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        engine_talk(f"The current time is {time}")

    # Date
    elif "date" in command:
        date = datetime.datetime.now().strftime('%A, %B %d, %Y')
        engine_talk(f"Today is {date}")

    # Joke
    elif "joke" in command:
        engine_talk(pyjokes.get_joke())

    # Define something
    elif command.startswith("define"):
        term = command.replace("define", "").strip()
        try:
            summary = wikipedia.summary(term, sentences=1)
            engine_talk(summary)
        except:
            engine_talk("I couldn't find a definition for that.")

    # Wikipedia-based questions (who is / where is / who's / where's)
    elif any(command.startswith(kw) for kw in ["who is", "where is", "who's", "where's"]):
        subject = (
            command.replace("who is", "")
                .replace("where is", "")
                .replace("who's", "")
                .replace("where's", "")
                .strip()
        )
        try:
            info = wikipedia.summary(subject, sentences=1)
            engine_talk(info)
        except:
            engine_talk("I couldn't find information about that.")

        # Basic math calculation
    elif command.startswith("calculate") or command.startswith("what is") or command.startswith("what's"):
        expression = (
            command.replace("calculate", "")
                .replace("what is", "")
                .replace("what's", "")
                .replace("plus", "+")
                .replace("minus", "-")
                .replace("times", "*")
                .replace("divided by", "/")
                .strip()
        )
        try:
            # Evaluate basic math expression safely
            result = eval(expression)
            engine_talk(f"The result is {result}")
        except Exception as e:
            engine_talk("Sorry, I couldn't calculate that.")

    # Exit
    elif any(kw in command for kw in ["exit", "quit", "stop"]):
        engine_talk("Goodbye!")
        sys.exit()

    else:
        engine_talk("Sorry, I didn't understand that command.")

# Run assistant loop
while True:
    run_alexa()
