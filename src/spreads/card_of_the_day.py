from src.models.deck import Deck
import os
import json
from datetime import date

FILE = "src/data/card_of_the_day.json"

def load_daily_card(): 
    """Load the daily card from a JSON file."""
    if not os.path.exists(FILE): # Check if file exists
        return None # No saved card
    try:
        with open(FILE, "r") as f: # Open file
            data = json.load(f) # Load JSON data
            if data.get("date") == str(date.today()): # Check if date matches today
                return data  # Today's card has already been generated
    except json.JSONDecodeError: # Handle JSON errors
        pass # Ignore JSON errors
    return None # No valid saved card

def save_daily_card(card_data): 
    """Save the daily card to a JSON file."""
    with open(FILE, "w", encoding="utf-8") as f: # Open file in write mode
        json.dump(card_data, f, indent=4, ensure_ascii=False) # Save JSON data