import random
from .card import Card
from src.utils.card_loader import load_tarot_interpretations

class Deck:
    def __init__(self):
        """Initialize a Tarot deck with 78 cards."""
        self.interpretations = load_tarot_interpretations()
        self.cards = []  # List to hold Card objects
        self.create_major_arcana()
        self.create_minor_arcana()

    def create_major_arcana(self):
        """Create the 22 Major Arcana cards"""
        major_arcana_names = [
            "The Fool", "The Magician", "The High Priestess", "The Empress", "The Emperor",
            "The Hierophant", "The Lovers", "The Chariot", "Strength", "The Hermit",
            "Wheel of Fortune", "Justice", "The Hanged Man", "Death", "Temperance",
            "The Devil", "The Tower", "The Star", "The Moon", "The Sun", "Judgement", "The World"
        ]

        for major_name in major_arcana_names:
            card_meanings = self.interpretations.get(major_name, {}) # Fetch meanings
            card = Card(major_name, "Major", interpretations=card_meanings)
            self.cards.append(card)

    def create_minor_arcana(self):
        """Create the 56 Minor Arcana cards"""
        suits = ["Wands", "Cups", "Swords", "Pentacles"]
        ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Page", "Knight", "Queen", "King"]

        for suit in suits:
            for rank in ranks:
                card_name = f"{rank} of {suit}"  # Create proper name
                card_meanings = self.interpretations.get(card_name, {}) # Fetch meanings
                self.cards.append(Card(card_name, "Minor", suit, rank, interpretations=card_meanings))

    def shuffle(self):
        """Shuffle the deck of cards."""
        random.shuffle(self.cards)

    def draw_card(self):
        """Draw a card from the top of the deck."""
        if self.cards:
            card = self.cards.pop(0)  # Remove and return the top card
            card.set_orientation(random.choice([True, False]))  # Randomly set orientation
            return card 
        else:
            return None  # Deck is empty
        
    

    

