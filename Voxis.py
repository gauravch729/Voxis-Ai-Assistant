import pyttsx3
import speech_recognition
import requests
from bs4 import BeautifulSoup
import pyautogui
import time
import os
from Dictapp import closeappweb
import pyjokes
from plyer import notification
from pygame import mixer
from bardapi import BardCookies 
import datetime 
import pyperclip 
import webbrowser 
from time import sleep 
import json 
import keyboard 

print("\nPlease say wake up to activate me\n")
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
# print(voices)
rate = engine.setProperty('rate', 130)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 250
        audio = r.listen(source, 0, 4)

    try:
        print("Understanding..")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query


def alarm(query):
    timehere = open("Alarmtext.txt", "a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")


def news():
    main_url = 'https://newsapi.org/v2/top-headlines?'
    main_page = requests.get(main_url).json()

    # print(main_page)
    articles = main_page["articles"]
    # print(articles)
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's{day[i]} news is : {head[i]}")


if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query or "listen" in query or "hey" in query or "breakup" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break

                elif "hello" in query:
                    speak("Hello sir, how are you ?")

                elif "i am fine" in query:
                    speak("that's great, sir")

                elif "how are you" in query:
                    speak("Perfect, sir! What about you?")

                elif "thank you" in query:
                    speak("you are welcome, sir")

                elif "what can you do" in query:
                    speak("I can help you in automating your daily system tasks! like opening and closing applications! Moreover i can also help you get information from the internet")

                elif "what makes you different" in query:
                    speak("I was designed to  provide users the ability to take control over the system and automating their daily tasks just by their voice commands and providing users a personalized internet experience.")

                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)

                elif "news" in query:
                    speak("Yes fetching the latest news...")
                    news()
                    speak("That's all about today's news thank you")

                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)

                elif "youtube" in query:
                    from SearchNow import searchYoutube
                    searchYoutube(query)

                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)

                elif "room" in query:
                    speak("Looking for your current location please wait...")
                    speak("Foundend...")
                    url = f"https://www.google.com/search?q=weather+in+Greater Noida"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(
                        f"current weather at GL Bajaj! Greater Noida is {temp}")

                elif "weather" in query:

                    query = query.replace("weather", "")
                    query = query.replace("at", "")
                    query = query.replace("tell me", "")
                    query = query.replace("the", "")

                    speak("Sure here it is...")
                    url = f"https://www.google.com/search?q=weather+in+{query}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current weather at {query} is {temp}")

                elif "change the window" in query or "switch the window" in query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    speak("Okay....doing")
                    time.sleep(1)
                    pyautogui.keyUp("alt")

                elif "shutdown the system" in query:
                    speak(
                        "Sure !bye...bye! system is going to shut down in 3...2....1...!")
                    os.system("shutdown /s /t 5")

                elif "restart the system" in query:
                    speak("Okay restarting your pc please wait")
                    os.system("shutdown /r /t 5")

                elif "time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"The time is {strTime}")

                elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")

                elif "play" in query or "pause" in query:
                    speak("Done")
                    pyautogui.press("k")

                elif "mute" in query or "unmute" in query:
                    pyautogui.press("m")
                    if "mute" in query:
                        speak("Video muted")
                    else:
                        speak("Video unmuted")

                elif "volume up" in query or "increase volume" in query:
                    from keyboard import volumeup
                    speak("Turning volume,up")
                    volumeup()

                elif "volume down" in query or "decrease volume" in query:
                    from keyboard import volumedown
                    speak("Turning volume,down")
                    volumedown()

                elif "remember this" in query:
                    rememberMessage = query.replace("remember this", "")
                    rememberMessage = query.replace("remember that", "")
                    rememberMessage = query.replace("that", "")
                    rememberMessage = query.replace("boxes", "")
                    speak("Okay! I have remembered this for you")
                    remember = open("Remember.txt", "w")
                    remember.write(rememberMessage)
                    remember.close()

                elif "what do i said to remember" in query:
                    remember = open("Remember.txt", "r")
                    speak("You told me that ! "+remember.read())

                elif "your name" in query:
                    speak(
                        "My name is Voxis ! Where VO means voice and XIS an acronym for  assistant.")

                elif "coded" in query:
                    speak(
                        "I am coded in python language ! Which is a very advanced language used for AI ! ML and object oriented purpose.")

                elif "battery" in query or "power" in query:
                    import psutil
                    battery = psutil.sensors_battery()
                    percentage = battery.percent
                    speak(f"Current power we have is {percentage}percentage")

                    if percentage >= 60:
                        speak("We have enough power to continue our work")

                    elif percentage >= 40 and percentage < 60:
                        speak(
                            "We should look for a charging point nearby to charge the system in case battery runs low.")

                    elif percentage >= 15 and percentage < 40:
                        speak(
                            "We don't have enough power,try to charge the system as soon as possible")

                    elif percentage < 15:
                        speak(
                            "Very low power,system may shutdown soon.Please charge the system")

                elif "schedule my day" in query or "plan my day" in query:
                    tasks = []  # Empty list
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt", "w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                elif "joke" in query:

                    speak("yes,here it is...")
                    joke = pyjokes.get_joke()
                    speak(joke)

                elif "show my schedule" in query or "show my tasks":
                    file = open("tasks.txt", "r")
                    content = file.read()
                    file.close()
                    # mixer.init()
                    # mixer.music.load("notify.mp3")
                    # mixer.music.play()
                    notification.notify(
                        title="My schedule :-",
                        message=content,
                        timeout=15
                    )
                 
                 
                 
 # Voxis AI                

# Acquiring the essential cookies through scraping.



def speak(text):
    engine.say(text)
    engine.runAndWait()



def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,5)

    try:
        print("Understanding..")
        query  = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        print("Say that again")
        return "None"
    return query 


def CookieScrapper():
    print("")
    print("*The extraction of essential cookies has been accomplished successfully.*")
    webbrowser.open("https://bard.google.com")
    
    sleep(5)
    pyautogui.click(x=1778, y=73)
    sleep(2)
    pyautogui.click(x=1541, y=270)
    sleep(2)
    pyautogui.click(x=1490, y=114)
    sleep(2)
    keyboard.press_and_release('ctrl + w')
    sleep(2)

    data = pyperclip.paste()

    try:
        json_data = json.loads(data)
        print("*The process of loading cookies has been executed without any issues, and the cookies are now successfully integrated into the system.*")
        pass

    except json.JSONDecodeError as e:
        print("*Cookies Loaded Unsuccessfully*")
        print("""*The error has been identified as a result of unsuccessful cookie replication from the Chrome extension, 
which is causing a disruption in the intended functionality.*""")
     
    SID = "__Secure-1PSID"
    TS = "__Secure-1PSIDTS"
    CC = "__Secure-1PSIDCC"

    try:
        SIDValue = next((item for item in json_data if item["name"] == SID), None)
        TSValue = next((item for item in json_data if item["name"] == TS), None)
        CCValue = next((item for item in json_data if item["name"] == CC), None)

        if SIDValue is not None:
            SIDValue = SIDValue["value"]
        else:
            print(f"{SIDValue} not found in the JSON data.")

        if TSValue is not None:
            TSValue = TSValue["value"]
        else:
            print(f"{TSValue} not found in the JSON data.")
 
        if CCValue is not None:
            CCValue = CCValue["value"]
        else:
            print(f"{CCValue} not found in the JSON data.")

        cookie_dict = {
            "__Secure-1PSID": SIDValue ,
            "__Secure-1PSIDTS": TSValue,
            "__Secure-1PSIDCC": CCValue,
        }

        print("")
        print(f"===> Cookie 1 - {SIDValue}")
        print(f"===> Cookie 2 - {TSValue}")
        print(f"===> Cookie 3 - {CCValue}")
        print("")
        return cookie_dict

    except Exception as e:
        print(e)

cookie_dict = CookieScrapper()


try:
    voxis = BardCookies(cookie_dict=cookie_dict)
    print("*The verification of cookies has been successfully completed.*")
    print("*All processes have been completed successfully, and you now have the capability to Use Voxis as an AI model.")
    print("")

except Exception as e:
    print("*The verification of cookies has encountered an issue and has not been successful.*")
    print("*This issue may arise due to the unsuccessful extraction of cookies from the extension.*")
    print(e)
 
# Initiating the text modification function to generate a summarized version of the result text.

def split_and_save_paragraphs(data, filename):
        
        try:
            paragraphs = data.split('\n\n')
            with open(filename, 'w') as file:
                file.write(data)
            data = paragraphs[:2]
            separator = ', '
            joined_string = separator.join(data)
            return joined_string
        except Exception as e:
            print(e)
 
# Commencing the main execution phase.

def MainExecution():

    while True:
        try:
            Question = takeCommand().lower()
            # Question = input("Enter The Query : ")
            RealQuestion = str(Question)
            results = voxis.get_answer(RealQuestion)['content']
            current_datetime = datetime.datetime.now()
            formatted_time = current_datetime.strftime("%H%M%S")
            filenamedate = str(formatted_time) + str(".txt")
            filenamedate = "Brain\\DataBase\\" + filenamedate
            Term=""
            for char in results:
                if char!="*":
                    Term+=char
            lines=Term.split('\n')
            output='\n'.join(lines[:8])
                    
            print(split_and_save_paragraphs(output, filename=filenamedate))
            
            if output.__contains__('/'):
                speak("No Speakable Output for this Query! However I have provided the desired information in text")
            else:
             speak(output)

        except Exception as e:
            print(e)

MainExecution()

