import json
import os

def load_tarot_interpretations():
    """Load tarot card interpretations from JSON files."""

    interpretations = {} # dictionary to hold interpretations

    base_path = os.path.dirname(__file__) # gets the folder where this file is located
    data_path = os.path.join(base_path, "..", "data") # moves up one level and into data folder
    data_path = os.path.abspath(data_path)  # this gives the absolute path to data folder
    
    try:
        # Load Major Arcana
        major_path = os.path.join(data_path, "major_arcana.json") # path to major arcana file
        with open(major_path, 'r') as f: # open file
            major_data = json.load(f) # load JSON data
            interpretations.update(major_data) # update interpretations dictionary

        # Load Minor Arcana
        minor_path = os.path.join(data_path, "minor_arcana.json") # path to minor arcana file
        with open(minor_path, 'r') as f: # open file
            minor_data = json.load(f) # load JSON data
            interpretations.update(minor_data) # update interpretations dictionary

    except FileNotFoundError as e: # handle file not found error
        print(f"Warning: Could not load interpretations - {e}") # print warning
        return {} # return empty dictionary
    
    return interpretations  # return interpretations dictionary  

