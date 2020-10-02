"""
JARVIS:
- Control windows programs with your voice
"""

# import modules
import datetime  # datetime module supplies classes for manipulating dates and times
import subprocess  # subprocess module allows you to spawn new processes

import \
    speech_recognition as sr  # speech_recognition Library for performing speech recognition with support for Google Speech Recognition, etc..

# pip install pyttsx3                   # need to run only once to install the library

# importing the pyttsx3 library
import pyttsx3

# initialisation
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



# obtain audio from the microphone


def speak(text):
    print('[JARVIS]:' + text)
    engine.say(text)
    engine.runAndWait()


def admin():
    def takeCommand():
        # It takes microphone input from the user and returns string output
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print("[Me]:" + query)

        except Exception as e:
            # print(e)
            return "None"
        return query

        # script starts here

        while True:
            # if 1:
            query = takeCommand().lower()

            # Logic for executing tasks based on query
            query = query.replace('Jarvis', '')

            if "time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak("Sir, The time is" + strTime)
            elif "notepad" in query:
                subprocess.call(['Notepad.exe'])
            elif "calculator" in query:
                subprocess.call(['calc.exe'])
            elif "sticky note" in query:
                subprocess.call(['StikyNot.exe'])
            elif "powershell" in query:
                subprocess.call(['powershell.exe'])
            elif "mspaint" in query:
                subprocess.call(['mspaint.exe'])
            elif "cmd" in query:
                subprocess.call(['cmd.exe'])
            elif "explorer" in query:
                subprocess.call(['C:\Program Files\Internet Explorer\iexplore.exe'])
            else:
                speak('I didn\'t quiet catch you sir. Can you please try that again?')


def start():
    speak('Say Something')
    admin()


start()
