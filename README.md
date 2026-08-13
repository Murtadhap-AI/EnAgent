# EnAgent (Jake) 🎙️
### Your AI-Powered English Speaking Partner

---

## What is EnAgent?

EnAgent is a **voice-first AI agent** designed to help you improve your English speaking skills through real conversation — not flashcards, not multiple choice, not typing.

You speak. Jake listens. Jake responds — out loud, in a casual American voice.

No keyboard. No chat window. Just conversation.

---

## Meet Jake 🇺🇸

Jake is your personal English coach built into the agent. He's:

- **Casual and friendly** — talks like a real American, not a textbook
- **Always correcting** — catches your grammar mistakes naturally, mid-conversation
- **Always teaching** — introduces new vocabulary and phrases in context
- **Always remembering** — tracks your mistakes and topics across sessions so he never forgets what you struggled with

---

## How It Works

```
You speak in English
        ↓
Jake listens (Speech-to-Text)
        ↓
Jake thinks and responds (Local LLM via Ollama)
        ↓
Jake speaks back (Text-to-Speech)
        ↓
Mistakes and topics saved to memory
        ↓
Next session: Jake picks up where you left off
```

---

## Key Features

| Feature | Description |
|---|---|
| 🎙️ **Voice Input** | Speak naturally — no typing required |
| 🔊 **Voice Output** | Jake replies with a real American voice |
| 🧠 **Persistent Memory** | Your mistakes and topics are saved locally across sessions |
| ✏️ **Smart Corrections** | Jake corrects your grammar in a natural, non-robotic way |
| 📚 **Topic Tracking** | Jake notices what English topics you're working on |
| 🔒 **100% Local & Free** | No API keys, no cloud, no cost — runs entirely on your machine |

---

## Tech Stack

| Tool | Role |
|---|---|
| `speech_recognition` | Converts your voice to text |
| `Ollama` + local LLM | Jake's brain — processes and responds |
| `pyttsx3` | Converts Jake's reply to speech |
| `JSON` | Stores your memory locally |

---

## Project Structure

```
EnAgent/
├── src/
│   ├── agent.py        # Core logic — thinks, updates memory, runs the loop
│   ├── memory.py       # Load, save, and update mistakes + topics
│   ├── prompts.py      # Jake's personality and system prompt
│   ├── stt.py          # Speech-to-Text (your voice → text)
│   └── tts.py          # Text-to-Speech (text → Jake's voice)
├── memory/
│   └── user_memory.json  # Auto-created — stores your progress
├── .env                  # Your environment config
├── requirements.txt
└── README.md
```

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/EnAgent.git
cd EnAgent
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up your environment

```bash
cp .env.example .env
```

Edit `.env` and fill in your settings (model name, etc.)

### 4. Make sure Ollama is running

```bash
ollama run qwen3:8b
```

### 5. Run Jake

```bash
python src/agent.py
```

---

## Example Session

```
🎙️  Listening...
You:  "Yesterday I go to the market and buyed some food."

Jake: "Ha, nice! Quick thing though — it's 'went' not 'go',
       and 'bought' instead of 'buyed'. Past tense gets tricky!
       So what did you buy at the market?"

🎙️  Listening...
```

Jake corrects, continues the conversation, and saves the mistake — all in one move.

---

## Roadmap

- [x] Voice input and output
- [x] Jake's personality and system prompt
- [x] Persistent memory (mistakes + topics)
- [ ] Structured memory extraction via `[MEMORY]` blocks
- [ ] GitHub Actions for basic CI
- [ ] Web UI (optional future phase)

---

## Why EnAgent?

Most language learning apps teach you to read and write English.  
EnAgent teaches you to **speak** it — by making you actually speak it, every session.

The fastest way to get comfortable with a language is to use it.  
Jake makes sure every session counts.

---

## Author

Built by **Murtadha** — pharmacy student, AI engineering learner, future software founder.

> *"I didn't just build this. I built it to use it."*

---

## License

MIT License — free to use, modify, and build on.