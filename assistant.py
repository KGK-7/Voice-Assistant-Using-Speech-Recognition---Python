import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import pywhatkit
import time
import psutil
import urllib.parse
import subprocess

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # Selecting a voice
newVoicesRate = 180
engine.setProperty('rate', newVoicesRate)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        print("Good Morning sir!")
        speak("Good Morning sir!")
    elif 12 <= hour < 18:
        print("Good Afternoon sir!")
        speak("Good Afternoon sir!")   
    else:
        print("Good Evening sir!")
        speak("Good Evening sir!")  
    print("I am JARVIS. I am here to assist you sir!")
    speak("I am JARVIS. I am here to assist you sir!")       

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1.0)  # Adjust for ambient noise
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  
        return query.lower()
    except Exception as e:
        print("Say that again please...")  
        return "None" 

def open_application(application_name):
    app_mapping = {
        'chrome': 'chrome.exe',
        'notepad': 'notepad.exe',
        'calendar': 'outlookcal:',
        'settings': 'ms-settings:',
        'control panel': 'control.exe',
        'photos': 'microsoft.photos:',
        'weather': 'bingweather:',
        'camera': 'microsoft.windows.camera:',
        'media player': 'wmplayer.exe',
        'adobe reader': 'AcroRd32.exe',
        'paint': 'mspaint.exe',
        'ms store': 'ms-windows-store:',
        'mail': 'outlookmail:',
        'map': 'bingmaps:',
        # Add more applications or settings as needed
    }

    executable_name = app_mapping.get(application_name.lower())

    if executable_name:
        try:
            os.startfile(executable_name)
            speak(f"Opening {application_name}")
        except Exception as e:
            print(f"Error opening application: {e}")
            speak(f"Sorry, I encountered an error while trying to open {application_name}.")
    else:
        speak(f"Sorry, I don't have information on how to open {application_name}.")

def close_application(app_name):
    app_mapping = {
        'chrome': 'chrome.exe',
        'notepad': 'notepad.exe',
        'calendar': 'outlookcal:',
        'settings': 'ms-settings:',
        'control panel': 'control.exe',
        'photos': 'microsoft.photos:',
        'weather': 'bingweather:',
        'camera': 'microsoft.windows.camera:',  
        'media player': 'wmplayer.exe',
        'adobe reader': 'AcroRd32.exe',
        'paint': 'mspaint.exe',
        'ms store': 'ms-windows-store:',
        'mail': 'outlookmail:',
        'map': 'bingmaps:',
        # Add more applications or settings as needed
    }

    executable_name = app_mapping.get(app_name.lower())

    executable_name = app_mapping.get(app_name.lower())


    if executable_name:
        try:
            subprocess.Popen(["taskkill", "/f", "/im", executable_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            speak(f"Closing {app_name}.")
        except Exception as e:
            print(f"Error closing application: {e}")
            speak(f"Sorry, I encountered an error while trying to close {app_name}.")
    else:
        speak(f"Sorry, I don't have information on how to close {app_name}.")

def google_search(query):
    query = urllib.parse.quote(query)
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if 'goodbye jarvis' in query:
            print("Goodbye sir")
            speak("Goodbye sir!")
            break

        elif 'exit jarvis' in query:
            print("ok sir , Let me know if I can help you again. Have a great day")
            speak("ok sir , Let me know if I can help you again. Have a great day")
            break

        elif "hello" in query :
            print("Hello, welcome sir")
            speak("Hello, welcome sir")

        elif "how are you" in query :
            print("I am good. I hope you are doing good as well.")
            speak("I am good. I hope you are doing good as well.") 
        
        
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
            
        elif 'open google' in query:
            webbrowser.open("www.google.com")

        elif 'open amazon' in query:
            webbrowser.open("www.amazon.in")   

        elif 'open flipkart' in query:
            webbrowser.open("www.flipkart.com")   

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open' in query:
            app_name = query.replace('open', '').strip()
            open_application(app_name)

        elif 'close' in query:
            app_name = query.replace('close', '').strip()
            close_application(app_name)

        elif 'play' in query:
            song = query.replace('play', '')
            speak('playing ' + song)
            try:
                pywhatkit.playonyt(song) 
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't play the song.")

        elif 'make a google search on' in query:
            search_query = query.replace('make a google search on', '').strip()
            google_search(search_query)

        elif 'open' in query:
            channel = query.replace('open', '')
            speak('opening ' + channel)
            try:
                pywhatkit.playonyt(channel) 
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't open the channel")

        elif 'what is' in query:
            search_query = query.replace('what is', '').strip()
            google_search(search_query)

        elif ' ' in query:
            search_query = query.replace(' ', '').strip()
            google_search(search_query)

        elif 'vanakam' in query:
            print("vanakam , epdi erukinga")
            speak("vanakam , epdi erukinga")

        elif 'what is my name' in query:
            print("Gokulakrishnan")
            speak("Gokulakrishnan")
        
'''this mini-project aims  on usage of python's speech recognition to create aa voice assistant, 
you can modify it according to your purposes.'''
