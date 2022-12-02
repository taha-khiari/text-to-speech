import pyttsx3

engine = pyttsx3.init()

engine.say("Hello World")
voices=engine.getProperty("voices")
for n in range(0,len(voices)):
    print(n,voices[n])