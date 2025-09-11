# Voice Assistant Mitra

A voice-controlled AI assistant that can open websites, play music, tell the time, fetch news headlines, and answer general queries using Google Gemini API.

## Project Overview

This project features voice recognition and text-to-speech for natural interaction. Commands are processed to control browser actions or query Google Gemini conversational AI with response synthesis.

## How to Run

1. Clone the repository
2. Install dependencies:
3. Insert your API keys (`GEMINI_API_KEY`, `NEWSAPI_KEY`) in the script `mitra.py`.
4. Run the assistant:
5. Speak commands prefixed with the word "Mitra".

## Dependencies

- SpeechRecognition
- pyttsx3
- requests
- google-generativeai

## Dataset / Related Files

- `musiclibrary.py`: Contains a dictionary of song names mapped to URLs for playback.

## Key Performance Indicators (KPIs)

- Voice recognition accuracy and reliability
- Response latency for commands and AI queries
- Number of supported voice commands
- Successful news headline retrieval rate

## Project Insights

- Integrates speech recognition with web automation and conversational AI.
- Uses Google Gemini API for advanced language understanding.
- Modular and extendable codebase for adding more features.

## Conclusion

Voice Assistant Mitra is a foundation for building interactive voice applications combining speech input, external API integration, and dynamic web-based actions to create a responsive AI assistant.

