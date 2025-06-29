import re
import nltk
from nltk.tokenize import word_tokenize
import datetime
import webbrowser as wb
import asyncio
from AppOpener import close, open as appopen
from webbrowser import open as webopen
from pywhatkit import search, playonyt
from bs4 import BeautifulSoup
import requests
import keyboard
import os
nltk.download('punkt', quiet=True)

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

def preprocess_input(user_input):
    user_input = user_input.lower()
    tokens = word_tokenize(user_input)
    return tokens, user_input

def bot_print(message: str):
    print(f"🤖 Bot: {message}")

def wishme() -> None:
    hour: int = datetime.datetime.now().hour
    if 4 <= hour < 12:
        bot_print(f"Good Morning {name}!!")
    elif 12 <= hour < 16:
        bot_print(f"Good Afternoon {name}!!")
    elif 16 <= hour < 24:
        bot_print(f"Good Evening {name}!!")
    bot_print("Hello! How may I help you. (Type 'bye' to exit)")

def open_websites(raw_text):
    raw_text = raw_text.lower().strip()
    if "open" not in raw_text:
        return False
    command = raw_text.replace("open", "").strip()
    site_names = [site.strip().replace(" ", "") for site in command.split("and") if site.strip()]
    if not site_names:
        bot_print("I didn't catch any website names.")
        return False
    for site in site_names:
        url = f"https://www.{site}.com"
        bot_print(f"Opening {url}")
        wb.open(url)
    return True

def GoogleSearch(topic):
    search(topic)
    return True

def YoutubeSearch(topic):
    url = f"https://www.youtube.com/results?search_query={topic}"
    wb.open(url)
    return True

def PlayYoutube(query):
    playonyt(query)
    return True

def OpenApp(app, sess=requests.session()):
    try:
        appopen(app, match_closest=True, output=True, throw_error=True)
        return True
    except:
        def extract_links(html):
            if html is None:
                return []
            soup = BeautifulSoup(html, 'html.parser')
            links = soup.find_all("a", {'jsname': 'UWckNb'})
            return [link.get('href') for link in links]
        def search_google(query):
            url = f"https://www.google.com/search?q={query}"
            headers = {"User-Agent": useragent}
            response = sess.get(url, headers=headers)
            return response.text if response.status_code == 200 else None
        html = search_google(app)
        if html:
            links = extract_links(html)
            if links:
                webopen(links[0])
        return True

def CloseApp(app):
    try:
        close(app, match_closest=True, output=True, throw_error=True)
        return True
    except:
        return False

def system(command):
    if command == "mute" or command == "unmute":
        keyboard.press_and_release("volume mute")
    elif command == "volume up" or command == "increase volume":
        keyboard.press_and_release("volume up")
    elif command == "volume down" or command == "decrease volume":
        keyboard.press_and_release("volume down")
    return True

async def TranslateAndExecute(commands: list[str]):
    funcs = []
    for command in commands:
        if command.startswith("open "):
            funcs.append(asyncio.to_thread(OpenApp, command[5:]))

        elif command.startswith("close "):
            funcs.append(asyncio.to_thread(CloseApp, command[6:]))

        elif command.startswith("play "):
            funcs.append(asyncio.to_thread(PlayYoutube, command[5:]))

        elif command.startswith("google search"):
            funcs.append(asyncio.to_thread(GoogleSearch, command[14:]))

        elif command.startswith("youtube search "):
            funcs.append(asyncio.to_thread(YoutubeSearch, command[15:]))

        elif command.startswith("system "):
            funcs.append(asyncio.to_thread(system, command[7:]))

    await asyncio.gather(*funcs)
    return True

if __name__ == "__main__":
    name = input("Enter Your Name: ")
    wishme()
    while True:
        user_input = input("You: ").strip().lower()
        if user_input in ["bye", "goodbye", "see you", "exit", "quit", "time to sleep"]:
            bot_print("Goodbye! Talk to you later.")
            break

        tokens, raw_text = preprocess_input(user_input)

        if re.search(r"\b(hii|hiii|hiiii|hello|hey|namaste)\b", raw_text):
            bot_print("Hello! How can I assist you today?")

        elif re.search(r"\b(time|what's the time|current time)\b", raw_text):
            bot_print(f"The current time is {datetime.datetime.now().strftime('%H:%M')}.")

        elif re.search(r"\b(date|today's date|what day)\b", raw_text):
            bot_print(f"Today's date is {datetime.datetime.now().strftime('%d-%m-%Y')}.")

        elif re.search(r"\b(who are you|your name|what is your name)\b", raw_text):
            bot_print("My Name is TyZe, I'm your chatbot assistant!")
        
        elif re.search(r"\b(my name|what is my name)\b", raw_text):
            bot_print(f"Your Name is {name}")

        elif any(word in tokens for word in ["thanks", "thank", "thankyou"]):
            bot_print("You're welcome!")

        elif any(word in tokens for word in ["weather", "temperature", "rain", "sunny"]):
            bot_print("I'm not connected to weather APIs yet, but it looks like a great day!")

        elif "open youtube" in raw_text:
            bot_print("Opening YouTube...")
            wb.open("https://www.youtube.com")

        elif "open" in raw_text and "and" in raw_text:
            if not open_websites(raw_text):
                bot_print("Sorry, I couldn't open the sites.")

        elif any(raw_text.startswith(cmd) for cmd in ["open ", "close ", "play ", "google search ",  "youtube search ", "system"]):
            bot_print("Processing your request...")
            asyncio.run(TranslateAndExecute([raw_text]))

        else:
            bot_print("I'm not sure I understand that. Could you please rephrase?")
