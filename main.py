import pyttsx3 as speak
eng = speak.init()



def word():
    msg = input('Enter any word ')
    eng.say(msg)
    eng.runAndWait()

word()


