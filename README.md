# Voice Assistant Mitra
A voice-controlled AI assistant that can open websites, play music, tell the time, fetch news headlines, and answer general queries using Google Gemini API.


## 🔎 Project Overview

This project is a **voice-activated personal assistant** named **Mitra** that combines speech recognition, text-to-speech, and generative AI to perform everyday tasks.  
It listens to voice commands, processes them, and responds with either actions (like opening apps/websites, fetching news, or playing music) or conversational replies using Google’s **Gemini AI**.  

### ✨ Key Capabilities
- 🎤 **Speech Recognition**: Uses `speech_recognition` to capture and process spoken commands.  
- 🔊 **Voice Output**: Replies naturally using `pyttsx3` for text-to-speech.  
- 🌐 **Web Shortcuts**: Opens Google, YouTube, and other sites on command.  
- 🎵 **Music Playback**: Plays songs from a predefined library.  
- 📰 **News Headlines**: Fetches the latest India news via the **NewsAPI**.  
- 🤖 **Conversational AI**: Leverages **Google Gemini API** for natural, AI-powered responses when no direct command is matched.  
- ⏰ **Utilities**: Tells the current time and performs simple assistant tasks.  

### 🛠 Tech Stack
- **Python**  
- **speech_recognition** (voice input)  
- **pyttsx3** (voice output)  
- **webbrowser** (to open sites)  
- **requests** (API calls for news)  
- **Google Generative AI (Gemini)**  
- **NewsAPI**  

This assistant demonstrates how to integrate **voice commands** with **AI-driven responses**, creating a lightweight but functional personal assistant you can extend with more skills.  


## How to Run
1.Clone the repository
2.Install dependencies:
3.Insert your API keys (GEMINI_API_KEY, NEWSAPI_KEY) in the script mitra.py.
4.Run the assistant:
5.Speak commands prefixed with the word "Mitra".

## Dependencies
• SpeechRecognition
• pyttsx3
• requests
• google-generativeai

## Dataset / Related Files
• musiclibrary.py: Contains a dictionary of song names mapped to URLs for playback.

## Key Performance Indicators (KPIs)
• Voice recognition accuracy and reliability
• Response latency for commands and AI queries
• Number of supported voice commands
• Successful news headline retrieval rate

## Project Insights
• Integrates speech recognition with web automation and conversational AI.
• Uses Google Gemini API for advanced language understanding.
• Modular and extendable codebase for adding more features.

## Conclusion
Voice Assistant Mitra is a foundation for building interactive voice applications combining speech input, external API integration, and dynamic web-based actions to create a responsive AI assistant.
