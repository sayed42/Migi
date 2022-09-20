import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate',165)
engine.setProperty('volume',1.5)
engine.setProperty('voice','english_rp+f3')
engine.say("Hello sufiyan Sayed , my name is migi")
engine.runAndWait()