import pyttsx3
import speech_recognition as sr


class AI():
    __name = ""
    __skill = []

    def __init__(self, name=None):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate',175)
        self.engine.setProperty('volume',1.5)
        self.engine.setProperty('voice','english_rp+f3')
        self.r = sr.Recognizer()
        self.m = sr.Microphone()

        if name is not None:
            self.__name = name
        print("Listening")
        with self.m as source:
            self.r.adjust_for_ambient_noise(source)
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        sentence = "Hello , my name is"+ self.__name
        self.__name= value
        self.engine.say(sentence)
        self.engine.runAndWait()
        try:
            phrase = self.r.recognize_google(audio,show_all = False,language="en-US")
            sentence = "Got it , You Said"+ phrase
            self.engine.say(sentence)
            self.engine.runAndWait()
        except e as error:
            print("sorry , I didn't get you",e)
            self.engine.say("sorry , I didn't get you")
            self.engine.runAndWait()
        print("You said",phrase)
        return phrase
    def say(self,sentence):
        self.engine.say(sentence)
        self.engine.runAndWait()

    def listen(self):
        print("Say Something")
        with self.m as source:
            audio = self.r.listen(source)
        print("Got it")
        try:
            phrase = self.r.recognize_google(audio,show_all = False,language="en_US")
            sentence = "Got it , You Said"+ phrase
            self.engine.say(sentence)
            self.engine.runAndWait()
        except e as error:
            print("sorry , I didn't get you",e)
            self.engine.say("sorry , I didn't get you")
            self.engine.runAndWait()
        print("You said",phrase)
        return phrase
