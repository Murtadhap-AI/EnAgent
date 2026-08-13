import json
import os
from datetime import date

MEMORY_FILE = "memory/user_memory.json"

DEFAULT_MEMORY = {
    "user": "Murtadha",
    "sessions": 0,
    "mistakes": [],
    "topics_covered": []
}

def load_memory() -> dict:
    if not os.path.exists(MEMORY_FILE):
        return DEFAULT_MEMORY.copy()
    
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(memory: dict) -> None:
    os.makedirs("memory", exist_ok=True)
    
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2, ensure_ascii=False)

def update_mistakes(memory: dict, error: str, correction: str) -> dict:
    today = str(date.today())
    
    for mistake in memory["mistakes"]:
        if mistake["error"] == error:
            mistake["count"] += 1
            mistake["last_seen"] = today
            return memory
    
    memory["mistakes"].append({
        "error": error,
        "correction": correction,
        "count": 1,
        "last_seen": today
    })
    
    return memory

def update_topics(memory: dict, topic: str) -> dict:
    if topic not in memory["topics_covered"]:
        memory["topics_covered"].append(topic)
    
    return memory