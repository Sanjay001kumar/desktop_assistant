import os
import pyttsx3
import datetime
import speech_recognition as sr
engine=pyttsx3.init()
x=datetime.datetime.now()
a=x.strftime("%I")
b=x.strftime("%p")
hour=int(a)
def speak(speech):
    engine.say(speech)
    engine.runAndWait()
def wish():
    if((hour>=5 and hour<=10) and b=="AM"):
        print("good moring sir")
        engine.say("good moring sir")
        engine.runAndWait()
    elif(hour==11 and b=="AM" ):
        print("good afternoon sir")
        engine.say("good moring sir")
        engine.runAndWait()
    elif((hour==12 or hour<=3) and b=="PM"):
        print("good afternoon sir")
        engine.say("good afternoon si")
        engine.runAndWait()
    elif((hour>=4 and hour<=7)) and b=="PM":
        print("good evening sir")
        engine.say("good evening sir")
        engine.runAndWait()
    elif((hour>=8 and hour<=11) and b=="PM"):
        print("sweet night sir")
        engine.say("sweet night si")
        engine.runAndWait()
    else:
        speak("early moring sir")
        engine.say("early moring si")
        engine.runAndWait()
def comment():
    r=sr.Recognizer()
    with sr.Microphone() as s:
        print("listening.....")
        r.pause_threshold=1
        audio=r.listen(s)
    try:
        print("wait for few moments")
        global query
        query=r.recognize_google(audio,language="en-IN")
        print("user said :",query)
    except Exception as e:
        print(e)
        speak("say again")
def system():
    if "chrome" in query:
        os.system("google chrome")
    else:
            print("none")
def saytime():
    speak(x.strftime("%I"))
    speak("hours")
    speak(x.strftime("%M"))
    speak("minutes")
    speak(x.strftime("%p"))

wish()
print(" Hi sir I am none...\n How can you help you sir ")
speak(" Hi sir I am none how can you help you sir ")
comment()
if "time" in query:
    print(saytime())
elif( "open" in query):
    print(system())
