import unittest 
from src.models.deck import Deck 

class TestDeck(unittest.TestCase):
    def setUp(self):
        """Set up a new deck for each test."""
        self.deck = Deck()

    def test_deck_initialization(self):
        """Test that the deck initializes with 78 cards."""
        self.assertEqual(len(self.deck.cards), 78)

    def test_major_arcana_count(self):
        """Test that there are 22 Major Arcana cards."""
        major_arcana = [card for card in self.deck.cards if card.arcana == "Major"]
        self.assertEqual(len(major_arcana), 22)

    def test_minor_arcana_count(self):
        """Test that there are 56 Minor Arcana cards."""
        minor_arcana = [card for card in self.deck.cards if card.arcana == "Minor"]
        self.assertEqual(len(minor_arcana), 56)

    def test_shuffle_deck(self):
        """Test that shuffling the deck changes the order of cards."""
        original_order = self.deck.cards.copy()
        self.deck.shuffle()
        shuffled_order = self.deck.cards
        self.assertNotEqual(original_order, shuffled_order, "Deck order should change after shuffling")
    
    def test_draw_card(self):
        """Test drawing a card from the deck."""
        initial_count = len(self.deck.cards)  # Capture before state
        drawn_card = self.deck.draw_card()
        self.assertIsNotNone(drawn_card)
        # Verify after removal of the card 
        self.assertEqual(len(self.deck.cards), initial_count - 1)
        self.assertNotIn(drawn_card, self.deck.cards)  # Ensure drawn card is no longer in deck

if __name__ == '__main__':
    unittest.main()


    