import pyttsx3

def speak(word):
   eng=pyttsx3.init()
   eng.say(word)
   eng.runAndWait()

   
