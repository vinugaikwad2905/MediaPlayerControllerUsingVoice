import pyttsx3
import speech_recognition as sr
import os
import pyautogui as p

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        speak("Speak Now")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=2)

    try:
        print("Recognizing..")
        speak("stop speaking.")
        query1 = r.recognize_google(audio, language='en-ln')
        print(f"user said : {query1}")

    except Exception as e:
        speak("Say that again please ....")
        return "none"
    return query1

while True:
    query = takecommand().lower()
    print(query)
    if "play" in query:
        p.press("space")
    elif "pause" in query:
        p.press("space")
    elif "volume up" in query:
        p.keyDown("shi  ft")
        p.press("f3")
        p.keyUp("shift")
    elif "volume down" in query:
        p.keyDown("shift")
        p.press("f2")
        p.keyUp("shift")