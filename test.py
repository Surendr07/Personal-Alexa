import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os;
import smtplib
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("speak anything")
        print("Listening.....")
        audio = r.listen(source)
        r.pause_threshold = 1
        try:
            print("recogninzing ur voice sir")
            speak("recognizing ur voice aditya sir")

            query = r.recognize_google(audio, language='en-in')
            # query = r.recognize_google(audio)  # Using google for voice recognition.
            print(f"user said :{query}\n")
            # this code will speak what i just told
            # engine.say("u just told "+query)
            # engine.runAndWait()
        except:
            speak("sorry please say that again aditya sir")
            
            
            
#  here the programm end u can suggest me if u want facility more in this 

    return query


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("good Morning Aditya")
    elif 12 <= hour < 18:
        speak("good Afternoon aditya")
    else:
        speak("good Evening")
    speak("I am Zira.Please tell me how can i help you aditya sir")


def sendEmail(to ,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email','your password')
    server.sendmail('youremail')
    server.close()

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower();
    #logic to execute task based on query
        if 'wikipedia' in query:
            speak('seaching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("accordin to wikipedia")
            speak(results)
            print(results)
        elif 'youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir='C:\\Users\\aditya gujrati\\Music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif "time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open code' in query:
            codePath='C:\\Users\\aditya gujrati\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            # "C:\Users\aditya gujrati\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        elif 'email to harry' in query:
            try:
                speak("what shhould i say")
                content=takeCommand()
                to="the email u wanna sent"
                sendEmail(to,content)
                speak("email has been  sent")
            except Exception as e:
                print(e)
                speak("sorry i cant sent that email")

