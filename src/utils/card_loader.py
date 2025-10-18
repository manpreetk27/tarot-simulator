import json
import os

def load_tarot_interpretations():
    """Load tarot card interpretations from JSON files."""

    interpretations = {}

    base_path = os.path.dirname(__file__)
    data_path = os.path.join(base_path, "..", "data")
    data_path = os.path.abspath(data_path)  # get full path (important)
    
    try:
        # Load Major Arcana
        major_path = os.path.join(data_path, "major_arcana.json")
        with open(major_path, 'r') as f:
            major_data = json.load(f)
            interpretations.update(major_data)

        # Load Minor Arcana
        minor_path = os.path.join(data_path, "minor_arcana.json")
        with open(minor_path, 'r') as f:
            minor_data = json.load(f)
            interpretations.update(minor_data)

    except FileNotFoundError as e:
        print(f"Warning: Could not load interpretations - {e}")
        return {}
    
    return interpretations    

