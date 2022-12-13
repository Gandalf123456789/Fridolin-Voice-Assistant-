import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time
import random


#main_script
jokes = ['Der erfinder von Autokorrekt ist gestorben. Restaurant in peace', 'Was sind die letzten Worte eines Zimmermanns? Wirf mal den Hammer rüber!', 'was sind die letztenWorte eines Elektrikers? Kannst die sicherung wieder reinmachen!']

print("Lade...")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
print(rate)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = datetime.datetime.now().hour
    minute = datetime.datetime.now().minute
    second = datetime.datetime.now().second
    microsecond = datetime.datetime.now().microsecond

    if hour>=0 and hour<12:
        speak("Guten Morgen!")
    elif hour>=12 and hour<16:
        speak("Guten Nachmittag!")
    elif hour>=16 and hour<22:
        speak("Guten Abend!")
    elif hour>=22 and hour<24:
        speak("Gute Nacht!")
    else:
        speak("Guten Morgen!")
    speak(f"Es ist {hour} Uhr, {minute} Minuten, {second} Sekunden und {microsecond} Millisekunden.")
    speak("Villeicht sollte Carl Johann die Millisekunden und Sekunden wieder rausnehmen. Die verwirren nur.")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='de-de')
            if "Fridolin" in statement:
                print(f"user said:{statement}\n")
                speak("Ja?")


        except Exception as e:
            takeCommand()
            return "none"
        return statement



wishMe()
speak("Ich lade gerade das Programm von Fridolin")
speak("Soll ich dir einen kurzen witz erzählen?")
speak("Ich kann dich im moment sowieso noch nicht hören. Also ist es egal was du sagst. In meinem Programm steht das ich dir jetzt einen Witz erzählen soll.")
joke = random.choice(jokes)
speak(joke)
speak("HAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHAHA")
time.sleep(1.5)
engine.setProperty('voice', voices[1].id)
speak("loading is finished")
engine.setProperty('voice', voices[0].id)
speak("...Ja ich weiß das hat etwas länger gedauert...")
speak("Aber jetzt bin ich bereit!")
print("Fertig!")
engine.setProperty('voice', voices[1].id)
speak("listening...")
engine.setProperty('voice', voices[0].id)
takeCommand()

if __name__ == '__main__':

    while True:
        statement = takeCommand().lower()
        if statement == 0:
            continue



        elif 'youtube' in statement:
            webbrowser.open_new_tab("https://youtube.com")
            speak("youtube ist jetzt geöffnet...")
            time.sleep(3)

        elif 'google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google ist jetzt geöffnet...")
            time.sleep(5)

        elif 'gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            speak("Gmail ist jetzt geöffnet...")
            time.sleep(5)

        elif 'wikipedia' in statement:
            webbrowser.open_new_tab("https://www.wikipedia.de")
            speak("wikipedia ist jetzt geöffnet...")

        elif 'meine website' in statement:
            webbrowser.open_new_tab("https://test-d1f.pages.dev")
            speak("Deine Website ist jetzt geöffnet...")
