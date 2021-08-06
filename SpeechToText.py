import speech_recognition as sr
import pyttsx3 as p
from Music import *

r = sr.Recognizer()

engine = p.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.say("Hello what would you like me to do?")
engine.runAndWait()



with sr.Microphone() as source:

    audio = r.listen(source)

    try:
        query = r.recognize_google(audio)
        print(query)

        if "play" in query.lower():
            #removing the beginnning "play" from the query
            song = query.split(' ', 1)[1]
            bot = music()
            bot.play(song)

    except sr.UnknownValueError:
        print("Did not recognize your speech")
    except sr.RequestError as e:
        print("")