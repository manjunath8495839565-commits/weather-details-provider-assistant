
# 🌤️ Weather Details Provider Assistant

A conversational AI weather assistant built using **Google Agent Development Kit (ADK)** and **Ollama** (local LLM) — no cloud API keys required!

---

## 🚀 Demo

> "I am in Bangalore"
> 
> 🤖 *"Bangalore is a beautiful city! Currently, it's partly cloudy with a high of 28°C (82°F) and a low of 18°C (64°F)..."*

---

## ✨ Features

- 💬 Natural language weather conversations
- 🏙️ Supports any city worldwide
- 🖥️ Runs fully locally using Ollama (no API costs!)
- ⚡ Built on Google's Agent Development Kit (ADK)
- 🔒 Privacy-first — everything runs on your machine

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Google ADK | Agent framework |
| Ollama + LiteLLM | Local LLM inference |
| Python | Core language |

---

## ⚙️ Setup & Run

### Prerequisites
- Python 3.10+
- Ollama installed → [ollama.ai](https://ollama.ai)
- Google ADK installed

### Steps

```bash
# 1. Clone the repo
git clone https://github.com/manjunath8495839565-commits/weather-details-provider-assistant.git
cd weather-details-provider-assistant

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux

# 3. Install dependencies
pip install google-adk

# 4. Pull Ollama model
ollama pull llama3

# 5. Run the agent
adk web
Then open → http://localhost:8000
📁 Project Structure
weather-details-provider-assistant/
├── agent/
│   ├── agent.py        # Main agent logic
│   ├── __init__.py
│   └── .env            # Local config
├── .env
└── README.md
👨‍💻 Author
Manjunath Y
Built with ❤️ using Google ADK + Ollama
⭐ Support
If you found this helpful, give it a star ⭐ on GitHub!
