"""
Install an additional SDK for JSON schema support Google AI Python SDK

$ pip install google.ai.generativelanguage
$ pip install SpeechRecognition
$ pip install python-dotenv
$ pip install pyttsx3
$ pip install pyaudio  (Do no use just pip it.)

"""

import os
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content
from dotenv import load_dotenv
import speech_recognition as sr #converts voice commands into text
import pyttsx3 # read out text output to voice
import webbrowser # to handle certain activities on my web browser
import re

load_dotenv()

genai.configure(api_key=os.getenv('api_data'))

# Create the model
generation_config = {
  "temperature": 0.3,
  "top_p": 0.8,
  "top_k": 20,
  "max_output_tokens": 512,
  "response_mime_type": "text/plain",
}

# Set your own instructions here

model = genai.GenerativeModel(
  model_name="gemini-2.0-flash-exp",
  generation_config=generation_config,
  system_instruction="Response in Shorter text, concise and to the point. ",
)

# Convert to Markdown

def strip_markdown(model_response):
    return re.sub(r'\*\*(.*?)\*\*', r'\1', model_response)  # Remove bold formatting


# response model

history = []

print("Bot: Hello...!, How can I help you today?")

def Reply(user_input):

    chat_session = model.start_chat(
        history=history
    )

    response = chat_session.send_message(user_input)

    model_response = response.text

    # Appends each and every conversation into history

    history.append({"role": "user", "parts": [user_input]})
    history.append({"role": "model", "parts": [model_response]})

    # print(f'Bot: {model_response}')

    return strip_markdown(model_response)  # Return the response Markdown formatting

    '''print(f'Bot: {model_response}')
    print()'''

# text to speech

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speech(text):
    engine.say(text)
    engine.runAndWait()

speech("Hello, How are you?")

def takeCommands(active=True):
    """Capture voice input and convert to text, adjust sensitivity based on mode."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 300 if active else 1000  # Higher threshold needs louder tone
        r.dynamic_energy_threshold = True  # Adapts to background noise
        print("Listening..." if active else "Sleeping, say 'Wake Up' to wake me...")
        r.pause_threshold = 1
        audio = r.listen(source)  # No timeout, always listening
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except Exception:
        print("Say that again...")
        return "none"

if __name__ == "__main__":
    active = True  # Start in active mode
    while True:
        query = takeCommands(active)
        if query == "none":
            if active:
                speech("I didn't catch that, can you repeat?")
            continue

        # Wake-up logic
        if not active and "Wake up" in query:
            active = True
            speech("I’m up, What’s the word?")
            continue

        # Skip processing if not active
        if not active:
            continue

        # Browser moves
        handled = False
        try:
            if "open youtube" in query:
                webbrowser.open("https://www.youtube.com")
                speech("Openning YouTube, let’s vibe!")
                handled = True
            elif "open google" in query:
                webbrowser.open("https://www.google.com")
                speech("Google, here we come!")
                handled = True
            elif "search" in query and "on google" in query:
                search_term = query.replace("search", "").replace("on google", "").strip()
                webbrowser.open(f"https://www.google.com/search?q={search_term}")
                speech(f"Searching {search_term}—let’s see what’s good!")
                handled = True
        except Exception as e:
            speech(f"Browser’s clowning: {str(e)}")

        # Only hit the AI if we didn’t handle it
        if not handled:
            try:
                ans = Reply(query)
                print(f"Bot: {ans}")
                speech(ans)
            except Exception as e:
                speech(f"AI’s having a meltdown: {str(e)}")
                continue

        # Sleep mode
        if "bye" in query:
            active = False
            speech("Napping now, Say 'Wake up' when you need me.")
        
        if "finish" in query:
            active = False
            print(Reply(query))
            break  # Exit the loop, end the program