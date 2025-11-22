from src.models.deck import Deck
import random

class CustomSpread:
    def __init__(self, num_cards, reading_type, positions):
        """Initialize the custom spread with specified number of cards and reading type."""
        self.num_cards = num_cards # Number of cards in the spread
        self.reading_type = reading_type # Type of reading: General, Love, Career
        self.positions = positions # List of position names
        self.cards_drawn = [] # List to hold drawn cards

    def perform_reading(self):
        deck = Deck() # Create a new deck
        deck.shuffle() # Shuffle the deck
        for i in range(self.num_cards):
            card = deck.draw_card() # Draw a card from the deck
            self.cards_drawn.append(card) # Store drawn card

            # Randomly set orientation
            if random.choice([True, False]): # Randomly choose orientation
                card.set_orientation(True)  # Card becomes REVERSED

    def get_results(self):
        """Return a list of dictionaries containing position, card, and meaning."""
        results = [] 
        for i in range(self.num_cards): # Iterate through drawn cards
            position = self.positions[i] # Get position name
            card = self.cards_drawn[i] # Get drawn card
            meaning = card.get_meaning(self.reading_type.lower()) # Get meaning based on reading type
            results.append({ # Append result dictionary
                "position": position,
                "card": card,
                "meaning": meaning
            })
        return results  # Return the results
