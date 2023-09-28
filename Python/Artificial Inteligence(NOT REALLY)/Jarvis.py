import datetime
import webbrowser 
import pyttsx3
import speech_recognition as sr
import wikipedia
import os 

engine = pyttsx3.init("sapi5")

voices = engine.getProperty('voices') 

# print(voices[0].id)

engine.setProperty('voices', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour < 12 :
        engine.say("Good Mornning!")
    elif hour >=12 and hour < 18:
        engine.say("Good Afternoon!")
    else:
        engine.say("Good Evening!")
    
    speak("I am Jarvis how can I help you")

def takeCommand():
    # it takes microphone input from the user and returns str output 

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 550
        r.pause_threshold = 1 # wiats if i stop for a while (that is not  to complete the speech)
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language="en-IN")
            print(f"User said:{query}\n")
            return query.lower()
        except Exception as e :
            print(e)
            print("Say that agian please...")
            return "None"           
        

if __name__ == "__main__":
    # speak("Arya is a good boy")
    wishMe()
    while True:
        query = takeCommand()
        
        #Logic for executing tasks based on query

        if 'wikipedia' in query :
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=1)
            print(results)
            speak(f"According to wikipedia{results}")

        elif "open youtube" in query:
            speak("Opening Youtube")
            webbrowser.open("youtube.com") 
            break
        elif "open google" in query:
            webbrowser.open("google.com")
            break
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
            break
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The Time is {strTime}")
        elif "bye" in query:
            speak("Bye...have a nice time")
            break
        elif "open code" in query:
            codePath = "C:\\Users\\Aryak\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            break
        elif "gu kha" in query:
            speak("ok Sir,Gu Kha to mi")
            break
