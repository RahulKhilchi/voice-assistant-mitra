import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import musiclibrary
import requests
import google.generativeai as genai

# --- CONFIG & INITIALIZATION ---

# --- CORRECTED SECTION: Paste your real API key here ---
# Warning: Do not share this file publicly with the key in it.
GEMINI_API_KEY = "AIzaSyBwW34bZ07gKVKm5p7PA2ZdRbHnTReUA30"

# --- SIMPLIFIED AND CORRECTED API CONFIGURATION ---
if GEMINI_API_KEY and GEMINI_API_KEY != "AIzaSyDOKaJSkT4cXi9hreDF4h-gdBjPMOqdvBg":
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        print("Gemini API configured successfully.")
    except Exception as e:
        print(f"Error configuring Gemini API: {e}")
        GEMINI_API_KEY = None # Disable features if config fails
else:
    # Handle case where key is not pasted
    print("Warning: Gemini API key is not set. Conversational features will be disabled.")
    GEMINI_API_KEY = None


NEWSAPI_KEY = ""

# Initialize objects
engine = pyttsx3.init()
recognizer = sr.Recognizer()

# --- HELPER FUNCTIONS ---

def speak(text):
    """This function takes text and speaks it out loud."""
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    """Listens for audio, recognizes it, and returns the text as a string."""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            recognizer.adjust_for_ambient_noise(source, duration=1.5)
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=10)

        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except (sr.UnknownValueError, sr.WaitTimeoutError):
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

def fetch_india_headlines(api_key, top_n=3):
    """Fetch top India headlines from NewsAPI with robust error handling."""
    url = "https://newsapi.org/v2/top-headlines"
    params = {"country": "in", "pageSize": max(top_n, 3)}
    headers = {"X-Api-Key": api_key}
    try:
        r = requests.get(url, params=params, headers=headers, timeout=8)
        data = r.json()
    except (requests.RequestException, ValueError) as e:
        print(f"Error fetching news: {e}")
        return {"ok": False, "articles": []}

    if r.status_code != 200 or data.get("status") != "ok":
        print("NewsAPI error payload:", data)
        return {"ok": False, "articles": []}

    articles = data.get("articles", []) or []
    return {"ok": True, "articles": articles[:top_n]}

def ask_gemini(query):
    """Sends a query to the Gemini model and returns the response."""
    # Check if the API key was set correctly
    if not GEMINI_API_KEY:
        return "Sorry, my conversational AI is not configured. Please check the API key."

    try:
        model = genai.GenerativeModel('gemini-1.5-flash-latest')
        response = model.generate_content(query)
        cleaned_text = response.text.replace('*', '').replace('`', '')
        return cleaned_text
    except Exception as e:
        print(f"An error occurred with the Gemini API: {e}")
        return "Sorry, I'm having trouble thinking right now."

# --- MAIN COMMAND PROCESSING LOGIC ---

def processCommand(command):
    """This function processes the command spoken by the user."""
    print(f"Processing command: '{command}'")

    if 'open google' in command:
        speak("Opening Google for you, sir.")
        webbrowser.open("https://google.com")
    elif 'open youtube' in command:
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")
    elif 'the time' in command:
        strTime = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"Sir, the time is {strTime}")
    elif command.startswith("play"):
        song = command.replace("play", "").strip()
        try:
            link = musiclibrary.music[song]
            speak(f"Playing {song} for you.")
            webbrowser.open(link)
        except KeyError:
            speak(f"Sorry, I don't have the song {song} in my library.")
    elif "news" in command:
        speak("Fetching the latest news headlines.")
        result = fetch_india_headlines(NEWSAPI_KEY, top_n=3)
        if not result["ok"] or not result["articles"]:
            speak("Sorry, I couldn't fetch the news right now.")
            return
        for i, article in enumerate(result["articles"], start=1):
            title = article.get("title", "No title")
            speak(f"Headline {i}: {title}")
    else:
        speak("Let me think about that...")
        gemini_response = ask_gemini(command)
        speak(gemini_response)


# --- MAIN PROGRAM LOOP ---
if __name__ == "__main__":
    speak("Mitra shuru ho raha hai.")

    while True:
        phrase = takeCommand()

        if "mitra" in phrase:
            speak("Ji boliye.")
            command = phrase.replace("mitra", "").strip()
            if command:
                processCommand(command)

        if "stop" in phrase or "shutdown" in phrase:
            speak("Shutting down. Goodbye.")
            break