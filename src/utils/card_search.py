import streamlit as st
import json # for handling JSON files
import os # for file operations

def load_cards():
    """Load all tarot card data from JSON files."""
    base_path = "src/data" # base path to data directory
    all_cards = [] # list to hold all cards

    for file_name, arcana_type in [("major_arcana.json", "Major"), ("minor_arcana.json", "Minor")]: # iterate over files
        file_path = os.path.join(base_path, file_name) # construct file path
        if os.path.exists(file_path): # check if file exists
            with open(file_path, "r", encoding="utf-8") as f: # open file
                data = json.load(f) # load JSON data
                for name, details in data.items(): # iterate over card details
                    card = {"name": name, "arcana": arcana_type} # create card dictionary
                    card.update(details) # add details to card
                    all_cards.append(card) # add card to list
    return all_cards # return list of all cards