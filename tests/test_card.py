import unittest
from models.card import Card

class TestCard(unittest.TestCase):
    def test_major_arcana_card(self):
        """Test creation and representation of a Major Arcana card."""
        card = Card("The Fool", "Major")
        self.assertEqual(card.name, "The Fool")
        self.assertEqual(card.arcana, "Major")
        self.assertEqual(card.suit, None)
        self.assertEqual(card.rank, None)
        self.assertEqual(repr(card), "The Fool (Major Arcana) Upright")

    def test_minor_arcana_card(self):
        """Test creation and representation of a Minor Arcana card."""
        card = Card("Three of Cups", "Minor", "Cups", "Three")
        self.assertEqual(card.name, "Three of Cups")
        self.assertEqual(card.arcana, "Minor")
        self.assertEqual(card.suit, "Cups")
        self.assertEqual(card.rank, "Three")
        self.assertEqual(repr(card), "Three of Cups (Minor Arcana) Upright")

    def test_card_orientation(self):
        """Test setting and getting card orientation."""
        card = Card("The Magician", "Major")
        self.assertFalse(card.is_reversed) # Default should be upright 
        card.set_orientation(True)  # Try to change it
        self.assertTrue(card.is_reversed) # Verify it changed
        self.assertEqual(repr(card), "The Magician (Major Arcana) Reversed")

    def test_get_meaning(self):
        interpretations = {
            "general": {
            "upright": "Intuition, wisdom.",
            "reversed": "Secrets, confusion."
        }
    }
        card = Card("The High Priestess", "Major", interpretations=interpretations)
        upright_meaning = card.get_meaning()
        self.assertIsInstance(upright_meaning, str)
        card.set_orientation(True)
        reversed_meaning = card.get_meaning()
        self.assertIsInstance(reversed_meaning, str)
        self.assertNotEqual(upright_meaning, reversed_meaning)

if __name__ == '__main__':
    unittest.main()


        

        

