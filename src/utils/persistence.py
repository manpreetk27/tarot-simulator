import json # for handling JSON files
import os # for file operations
from datetime import datetime # for timestamping, adding timestamps to readings

FILE = "src/data/readings.json" # Path to readings file

def load_readings():
    """Load saved readings from JSON, or return empty list if not found."""
    if not os.path.exists(FILE): # Check if file exists
        return [] # Return empty list if not found
    try:
        with open(FILE, "r", encoding="utf-8") as f: # Open file
            content = f.read().strip() # Read content
            if not content: # Check if content is empty
                return [] # Return empty list if empty
            return json.loads(content) # Load and return JSON data
    except (json.JSONDecodeError, FileNotFoundError): # Handle JSON errors and file not found
        return [] # Return empty list on error

def create_reading_entry(spread_type, cards, reading_type, reflection): 
    return {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), # current timestamp
        "spread_type": spread_type,
        "cards": [
            {
                "name": card.name,
                "arcana": card.arcana,
                "is_reversed": getattr(card, "is_reversed", False), # get orientation
                "meaning": card.get_meaning(reading_type.lower())
            }
            for card in cards # list comprehension for cards
        ],
        "reading_type": reading_type,
        "reflection": reflection
    }


def save_readings(new_entry):
    """Save readings to a JSON file safely (creates folder if missing)."""
    # Make sure folder exists
    os.makedirs(os.path.dirname(FILE), exist_ok=True) 

    readings = load_readings() # Load existing readings
    readings.append(new_entry) # Append new entry

    with open(FILE, "w", encoding="utf-8") as f: # Open file in write mode
        json.dump(readings, f, indent=4, ensure_ascii=False) # Save updated readings


    

