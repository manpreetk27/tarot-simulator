from src.models.deck import Deck

def main():
    """Main function to demonstrate deck functionality."""
    print("🔮 Welcome to the Tarot Reading Simulator 🔮")
    
    # Create and shuffle the deck
    deck = Deck()
    print(f"Deck is created with {len(deck.cards)} cards\n")

    # Drawing a few cards
    print("Drawing 3 cards for a simple reading:\n")
    positions = ["Past", "Present", "Future"]
    for position in positions:
        card = deck.draw_card()
        print(f"{position}: {card}")

    print(f"\nCards remaining in the deck: {len(deck.cards)}")
    print("\n Thank you for using Tarot Reading Simulator!")

if __name__ == "__main__":
    main()