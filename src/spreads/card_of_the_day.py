from src.models.deck import Deck
import os
import json
from datetime import date

FILE = "src/data/card_of_the_day.json"

def load_daily_card():
    """Load the daily card from a JSON file."""
    if not os.path.exists(FILE):
        return None
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
            if data.get("date") == str(date.today()):
                return data  # Today's card has already been generated
    except json.JSONDecodeError:
        pass
    return None

def save_daily_card(card_data):
    """Save the daily card to a JSON file."""
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(card_data, f, indent=4, ensure_ascii=False)