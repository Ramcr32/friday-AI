# import pylint
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import random
import requests
import json
# from gtts import gTTS
import playsound
import wikipedia



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)




    
    
    

    

def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")

    speak("i am   Ram   personal assistant  sir. please tell me how may i help you")

def takecommand():
    # '''it takes microphone input from the user and return string output'''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold=1
        
        audio = r.listen(source)

    try:
        print("Recognizing.......")
        query =r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        print(e)
        print("say that again please.....")
        return "None"
    return query

if __name__ == '__main__':
    wishme()
    # speak("ram is good boy")
    while 1:
        
        query=takecommand().lower()
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            # ram=wikipedia.search(query,results=10, suggestion=False)
            results = wikipedia.summary(query, sentences=2)
             
            speak("According to Wikipedia")
            print(results)
            speak(results)
            
            
        elif 'open youtube' in query:
           
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play video' in query:
            music_dir='E:\my songs'
            video=os.listdir(music_dir)
            print(video)
            numbers=[i for i in range(len(video))]
            os.startfile(os.path.join(music_dir,video[random.choice(numbers)]))
        
        elif 'open chrome' in query:
            add='C:\\Users\\hp\\AppData\\Local\\Google\\Chrome\\Application\\chrome'
            os.startfile(add)
        

        elif 'news' in query:
            engine.setProperty('rate',125)
            speak("hiiii...i am your news reporter ")
            url="http://newsapi.org/v2/top-headlines?country=in&apiKey=222fbef7c2594f41826767e93deeb350"
            news=requests.get(url).text
            news_in_dict=json.loads(news)
            art=news_in_dict['articles']
            for article in art:
                speak(article['title'])
                print(article['title'])
                speak(article['description'])
                print()
                print(f"more: {article['url']}")
                print()
                print()
                

        if "hii" in query:
            speak("hello")
        elif "hello" in query:
            speak("hello")
        elif 'who are you' in query:
            speak('you can call me friday!')
            
        elif 'what is your name' in query:
            speak('you can call me friday!')
        elif "friday" in query:
            speak("yes sir!")
            speak("how may i help you")
            
        
        if "stop" in query:
            speak("thank you!")
            break
        if "quit" in query:
            speak("thank you!")
            break
        if "close" in query:
            speak("thank you!")
            break
        elif "time" in query:
            speak(datetime.datetime.now().strftime("%H:%M:%S"))
        elif "thank you" in query:
            speak("welcome")
        

        


        

            



















