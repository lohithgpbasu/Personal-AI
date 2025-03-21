# Personal-AI

## Overview
**Personal-AI** is a voice-controlled AI assistant powered by the **Gemini model**, designed to understand and respond to natural language queries. The assistant leverages **speech recognition** and **text-to-speech conversion** to provide a seamless user experience.

## Features
- 🎤 **Voice Command Processing**: Captures audio input from users.
- 📝 **Speech-to-Text Conversion**: Uses **SpeechRecognition** for transcribing user commands.
- 🤖 **AI-Powered Responses**: Processes text using the **Google Gemini API**.
- 🔊 **Text-to-Speech Output**: Converts AI-generated responses into speech using **pyttsx3**.
- ⚙️ **Customizable Assistant**: Modify the behavior and responses as needed.

---

## Installation

Ensure you have **Python 3.x** installed on your system.

### 1. Install Required Dependencies
Run the following command to install the necessary packages:

```sh
pip install google.ai.generativelanguage
pip install SpeechRecognition
pip install python-dotenv
pip install pyttsx3
pip install pyaudio  # Use this exact command, avoid just "pip install"
```

### 2. Set Up API Key
You need a **GEMINI API Key** to enable the AI assistant.

- Visit [Google AI Studio](https://aistudio.google.com/app/apikey) to get a free API key.
- Check pricing and rate limits at:
  - [Google Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing)
  - [Google Gemini API Rate Limits](https://ai.google.dev/gemini-api/docs/rate-limits)

### 3. Configure Environment Variables
- Create a **`.env`** file in your project directory.
- Add the following line, replacing `'YOUR_GEMINI_API_KEY'` with your actual API key:

```env
api_data = 'YOUR_GEMINI_API_KEY'
```

---

## Usage

Run the script to activate the voice assistant:

```sh
python app.py
```

### How It Works:
1. 🎙️ The assistant listens for user commands.
2. 📝 Converts speech to text using **SpeechRecognition**.
3. 🤖 Processes the query using the **Gemini API**.
4. 🔊 Converts the response into speech using **pyttsx3**.
5. 🎧 Speaks the response back to the user.

---

## Customization

You can personalize your AI assistant’s behavior:

- Modify the **voice settings** in `pyttsx3` to change the speech output.
- Fine-tune **query handling** to fit specific needs.
- Enhance response generation with additional logic or integrations.

---

## Troubleshooting

- **Pyaudio Installation Issues (Windows)**
  - Run the following before installing `pyaudio`:
  
    ```sh
    pipwin install pyaudio
    ```

- **API Key Not Working?**
  - Double-check your **`.env`** file.
  - Ensure you have activated the correct **Python environment**.

---

## Future Enhancements
- 🚀 Add **wake-word activation** (e.g., "Hey AI").
- 🏠 Integrate with **smart home devices**.
- 🌍 Improve **multi-language support**.

---

## License
This project is licensed under the **MIT License**. Feel free to use and modify it.
