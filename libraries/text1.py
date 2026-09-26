import pyttsx3
def speak(text):
    engine = pyttsx3.init()
    engine= pyttsx3.setproperty("rate", 100)
    engine= pyttsx3.setproperty("volumn", 100)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

y = True
while (y):
    x=input("enter the string to be spoken: ")
    if(x.lower()=="exit"):
        pyttsx3.init.stop()
        break

    speak(x)
   
#wao