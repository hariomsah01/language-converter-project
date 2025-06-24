# 💻 language-converter-project

**Convert code seamlessly from one programming language to another using LLMs.**

This project is a web-based code language converter built with [NiceGUI](https://nicegui.io/) and powered by the `StarCoder` model via `Ollama`. It allows users to input source code in one programming language and receive an AI-generated equivalent in another, all in a clean and interactive UI.


## 🚀 Features
🔁 Converts code between major languages: **Python**, **Java**, **C++**, **JavaScript**, and **C#**
🧠 Powered by **StarCoder** running via [Ollama](https://ollama.com/)
🧾 Copy-paste input interface with live LLM response generation
🖥️ Intuitive UI built entirely using **NiceGUI**

## 🛠️ Technologies Used

Python 3.10+
[NiceGUI](https://nicegui.io/)
[Ollama](https://ollama.com/) + StarCoder model
Local LLM inference (no API keys required)

## 📦 How to Run

1. **Install Ollama & pull StarCoder**
Download Ollama from [https://ollama.com](https://ollama.com)
Run: `ollama pull starcoder`

2. **Install dependencies**
bash
   pip install nicegui

python main.py

language-converter-project/
├── main.py       # Main app with UI and conversion logic
├── README.md     # Project documentation

The app sends your input code along with a natural language prompt to StarCoder via Ollama's local chat interface. It uses a simple chat format to instruct the model to perform a language translation. The output is displayed instantly in the right-hand panel.

