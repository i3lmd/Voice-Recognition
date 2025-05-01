import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests, json, sys

listener = sr.Recognizer()
engine = pyttsx3.init('nsspeech')  # Use macOS voice engine

engine.say("I am your virtual assistant.")
engine.say("Say something.")
engine.runAndWait()

try:
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            print(f"Command received: {command}")
            engine.say(f"You said: {command}")
            engine.runAndWait()
except Exception as e:
    print(f"Error: {e}")