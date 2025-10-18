import json
import os
from datetime import datetime

FILE = "src/data/readings.json"

def load_readings():
    """Load saved readings from JSON, or return empty list if not found."""
    if not os.path.exists(FILE):
        return []
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                return []
            return json.loads(content)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

from datetime import datetime

def create_reading_entry(spread_type, cards, reading_type, reflection):
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "spread_type": spread_type,
        "cards": [
            {
                "name": card.name,
                "arcana": card.arcana,
                "is_reversed": getattr(card, "is_reversed", False),
                "meaning": card.get_meaning(reading_type.lower())
            }
            for card in cards
        ],
        "reading_type": reading_type,
        "reflection": reflection
    }


def save_readings(new_entry):
    """Save readings to a JSON file safely (creates folder if missing)."""
    # Make sure folder exists
    os.makedirs(os.path.dirname(FILE), exist_ok=True)

    readings = load_readings()
    readings.append(new_entry)

    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(readings, f, indent=4, ensure_ascii=False)


    

