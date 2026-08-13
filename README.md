# EnAgent (Jake) 🎙️

A voice-based English learning agent I built to practice my own speaking skills.

---

## Why I Built This

I'm an Iraqi pharmacy student learning English — specifically trying to get better at **speaking**, not just reading or writing.

Most apps focus on grammar exercises and multiple choice. I wanted something that actually talks back.

So I built Jake — an AI agent I can have a real voice conversation with in English. He listens, responds out loud, corrects my mistakes naturally, and remembers what I struggled with across sessions.

I built this for myself. It's also one of my first real AI engineering projects.

---

## What It Does

- Listens to my voice and converts it to text
- Sends it to a local LLM (via Ollama) with Jake's personality
- Jake responds as a casual American friend — corrects mistakes without being robotic
- Speaks the reply back out loud using text-to-speech
- Saves my mistakes and topics to a local JSON file so Jake remembers them next session

---

## Tech Stack

| Tool | Role |
|---|---|
| `speech_recognition` | Voice → Text |
| `Ollama` + `qwen3:8b` | Local LLM (Jake's brain) |
| `pyttsx3` | Text → Voice |
| `JSON` | Local memory storage |

Everything runs locally — no API keys, no cloud, no cost.

---

## How to Run

```bash
# Install dependencies
pip install -r requirements.txt

# Make sure Ollama is running with your model
ollama run qwen3:8b

# Run Jake
python src/agent.py
```

---

## Project Structure

```
EnAgent/
├── src/
│   ├── agent.py      # Main loop — listens, thinks, speaks, updates memory
│   ├── memory.py     # Load/save/update mistakes and topics
│   ├── prompts.py    # Jake's personality prompt
│   ├── stt.py        # Speech-to-Text
│   └── tts.py        # Text-to-Speech
├── memory/
│   └── user_memory.json  # Auto-created — stores my progress
├── .env.example
├── requirements.txt
└── README.md
```

---

*Built by Murtadha — pharmacy student, learning AI engineering.*