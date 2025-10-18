import streamlit as st
import json
import os

import json
import os

def load_cards():
    """Load all tarot card data from JSON files."""
    base_path = "src/data"
    all_cards = []

    for file_name, arcana_type in [("major_arcana.json", "Major"), ("minor_arcana.json", "Minor")]:
        file_path = os.path.join(base_path, file_name)
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for name, details in data.items():
                    card = {"name": name, "arcana": arcana_type}
                    card.update(details)
                    all_cards.append(card)
    return all_cards