from src.models.deck import Deck 
import random 

class PastPresentFutureSpread:
    def __init__(self):
        """Initialize the spread with three positions: Past, Present, Future."""
        self.past_card = None # Past card
        self.present_card = None # Present card
        self.future_card = None # Future card
        self.reading_type = None # Type of reading: General, Love, Career

    def perform_reading(self, reading_type):
        """Initialize a deck, shuffle it, and draw three cards for the spread"""
        # Set reading type
        self.reading_type = reading_type
        # Initialize the deck
        deck = Deck()
        # Drawing three cards for Past, Present, Future
        self.past_card = deck.draw_card()
        self.present_card = deck.draw_card()
        self.future_card = deck.draw_card()

        for i in range(3):
            if random.choice([True, False]): # Randomly choose orientation
                self.past_card.set_orientation(True) # If True chosen card becomes REVERSED

        








    


