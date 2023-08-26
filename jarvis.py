import pyttsx3
import datetime
import pyaudio as audio
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak("Ohayou Gozaimash Jannaturu san!")
    elif hour >= 12 and hour<18:
        speak("good afternoon luxme")
    else:
        speak("oyousuminasai jannaturu san")
    speak("I am jarvis sensei. please tell me how may I help you")

def takeCommand():
    #it takes microphone input from the user and returns string output
    import speech_recognition as sr
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recogning...")
        query = r.recognize_google(audio, language="en-US")
        #print(f"User said: {query}\n")
        print("User said:", query)
    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query

def sendEmail(do, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("jannatulkhanam962@gmail.com", "jannat962...")
    server.sendmail("jannatulkhanam1930@gmail.com", to , content)
    server.close()
    


if __name__ =="__main__":
    wishme()
    #takeCommand()
    #while True:
    if 1:
          query = takeCommand().lower()
          #logic for executing tasks based on query
          if 'wikipedia' in query:
              speak('searching wikipedia')
              query = query.replace("wikipedia", "")
              results = wikipedia.summary(query, sentences=3 )
              speak("According to wikipedia")
              print(results)
              speak(results)
          elif 'open youtube' in query:
              webbrowser.open("youtube.com")

          elif 'open google' in query:
              webbrowser.open("google.com")

                  #   elif 'play music' in query:

          elif 'the time' in query:
              strTime = datetime.now().strfTime("%H:%M:%S")
              speak("Mam the time is:" , strTime)

          elif'open code' in query:
               codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
               os.startfile(codePath)

          elif 'send email to jannat' in query:
              try:
                  speak("What should I say")
                  content = takeCommand()
                  to = "jannatulkhanam1930@gmail.com"
                  sendEmail(to, content)
                  speak("Email has been send")
              except Exception as e:
                  print(e)
                  speak("Sorry! Iam not able to send this email")
              
              