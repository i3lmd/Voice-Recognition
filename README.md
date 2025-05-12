# 🎙️ Voice-Controlled Python Assistant (Alexa-Style)

Welcome to **Alexa Assistant in Python**, a fully voice-controlled, terminal-based AI assistant inspired by Alexa! Built entirely in Python, this project handle voice recognition, natural language commands, and build a seamless user experience through audio feedback.

> 🧠 _"Developed with a focus on intelligent interaction, clean command parsing, and a touch of personality."_  

---

## 🚀 Features

✅ **Voice Recognition** via `speech_recognition`  
✅ **Play YouTube Music** via `pywhatkit`  
✅ **Ask Anything** with answers from **Wikipedia**  
✅ **Get the Date & Time **  
✅ **Ask for Definitions**  
✅ **Tell Jokes** using `pyjokes`  
✅ **Perform Basic Math** with natural language  
✅ **Friendly Greetings & Conversation**  
✅ **Exit Gracefully** via voice command  
✅ **macOS TTS (Text-to-Speech)** output  
✅ **Terminal Color Highlights** for visual feedback

---

## 🛠️ Tech Stack

- **Python 3**
- `speech_recognition` – for capturing and interpreting voice commands  
- `pywhatkit` – to play YouTube videos  
- `wikipedia` – to fetch quick facts  
- `pyjokes` – for a bit of fun  
- `datetime`, `random`, `sys`, `os` – core Python utilities

---

## 🧪 Example Commands

| Category             | Example Commands                              |
|----------------------|-----------------------------------------------|
| 🎵 Music             | `play despacito`, `play lofi beats`           |
| 🗓️ Date & Time      | `what time is it`, `what's the date today`    |
| 📖 Definitions       | `define quantum physics`                      |
| ❓ General Questions  | `who is Elon Musk`, `where is Japan`          |
| 😂 Jokes             | `tell me a joke`, `joke`                      |
| ➕ Calculations      | `calculate 5 plus 7`, `what is 9 times 3`      |
| 🙋 Greetings         | `hello`, `how are you`, `what's your name`    |
| 🛑 Exit              | `exit`, `quit`, `stop`                         |

---

## 💡 What Makes It Special?

- ✨ **Human-Like Conversation**: Includes filler phrase cleanup for better recognition.
- 🎨 **Visual Feedback**: Terminal colors enhance interaction clarity.
- 🧼 **Clean Code**: Modular functions, documented logic, and exception handling.
- 🔒 **Minimal Dependencies**: Easy to run on any macOS with Python.

---

## 🖥️ Setup Instructions

### Requirements

- Python 3
- macOS (uses `say` command for TTS)
- Microphone

### Installation

```bash
git clone https://github.com/yourusername/alexa-assistant-python.git
cd alexa-assistant-python
pip install -r requirements.txt
