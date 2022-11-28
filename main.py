import pyttsx3

speak = pyttsx3.init()

this = input("Type your words here: ")
def say_this():
    speak.say(this)
    speak.runAndWait()

say_this()
