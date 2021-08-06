import pyttsx3 as p

engine = p.init()
#Currently setting the voice property to a female voice.
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

engine.say("Hello, how are you?")
engine.runAndWait()