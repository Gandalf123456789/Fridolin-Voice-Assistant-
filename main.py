import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import time
import random



jokes = ['Der erfinder von Autokorrekt ist gestorben. Restaurant in peace',
         'Was sind die letzten Worte eines Zimmermanns? Wirf mal den Hammer rüber!',
         'was sind die letztenWorte eines Elektrikers? Kannst die sicherung wieder reinmachen!']

print("Loading...")

# Voice engine ini
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

# functions


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hourwish = datetime.datetime.now().hour
    minutewish = datetime.datetime.now().minute
    secondwish = datetime.datetime.now().second
    microsecondwish = datetime.datetime.now().microsecond

    if 0 <= hourwish < 12:
        speak("Guten Morgen!")
    elif 12 <= hourwish < 16:
        speak("Guten Nachmittag!")
    elif 16 <= hourwish < 22:
        speak("Guten Abend!")
    elif 22 <= hourwish < 24:
        speak("Gute Nacht!")
    else:
        speak("Guten Morgen!")
    speak(f"Es ist {hourwish} Uhr {minutewish} , {secondwish} Sekunden und {microsecondwish} Mikrosekunden.")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            statement = r.recognize_google(audio, language='de-de')
            if "Fridolin" in statement:
                print(f"user said:{statement}\n")
                speak("Ja?")


        except Exception as e:
            take_command()
            return "none"
        return statement

# datetime info

dateini = datetime.datetime.now().date()
timeini = datetime.datetime.now().time()
engine.setProperty('voice', voices[1].id)
speak(dateini)
speak(timeini)
engine.setProperty('voice', voices[0].id)

# loading dialogue

wish_me()
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

# Take Commands

take_command()

if __name__ == '__main__':

    while True:
        statement = take_command().lower()
        if statement == 0:
            continue


        # commands

        elif 'youtube' in statement:
            webbrowser.open_new_tab("https://youtube.com")
            time.sleep(3)

        elif 'google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            time.sleep(5)

        elif 'gmail' in statement:
            webbrowser.open_new_tab("https://www.gmail.com")
            time.sleep(5)

        elif 'kalender' in statement:
            webbrowser.open_new_tab("https://calendar.google.com/")

        elif 'wikipedia' in statement:
            webbrowser.open_new_tab("https://www.wikipedia.de")

        elif 'meine website' in statement:
            webbrowser.open_new_tab("https://test-d1f.pages.dev")
        elif 'spiele musik' in statement:
            webbrowser.open_new_tab('https://www.youtube.com/watch?v=7wtfhZwyrcc&list=PLjfTMzhxDB5Lfil0D-I_o-8I__tUX4Sf5')

        elif 'wie spät' in statement:
            hour = datetime.datetime.now().hour
            minute = datetime.datetime.now().minute
            second = datetime.datetime.now().second
            microsecond = datetime.datetime.now().microsecond
            speak(f"Es ist {hour} Uhr, {minute} Minuten, {second} Sekunden und {microsecond} Mikrosekunden.")

        elif 'github' in statement:
            webbrowser.open_new_tab('https://github.com')

        elif 'danke' in statement:
            speak("Bitteschön.")
