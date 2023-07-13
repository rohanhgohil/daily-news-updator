from win32com.client import Dispatch
import requests
import json


# Speak Function
def speak(str):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=dc3396eb187948f8a3795747fb027a4e"  # Getting API
response = requests.get(url)
text = json.loads(response.text)  # Storing the news
# a = text['articles'][0]['title']


if __name__ == "__main__":
    print("Today's News\n")
    speak("Today's News")
    for i in range(10):
        print(text["articles"][i]["title"])
        speak(text["articles"][i]["title"])
