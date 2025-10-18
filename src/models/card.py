class Card:
    def __init__(self, name, arcana, suit=None, rank=None, interpretations=None):
        """Initialize a Tarot card."""
        self.name = name      # Name of the Tarot Card 
        self.arcana = arcana  # 'Major' or 'Minor'
        self.suit = suit      # 'Wands', 'Cups', 'Swords', 'Pentacles' for Minor Arcana
        self.rank = rank      # 'Ace', '2', ..., '10', 'Page', 'Knight', 'Queen', 'King' for Minor Arcana
        self.interpretations = interpretations if interpretations else {}
        self.is_reversed = False  # By default, cards are upright

    def __repr__(self):
        """Return a string representation of the card."""
        if self.is_reversed:
            orientation = "Reversed"
        else:
            orientation = "Upright"

        if self.arcana == "Major":
            return f"{self.name} ({self.arcana} Arcana) {orientation}"
        else:
            return f"{self.rank} of {self.suit} ({self.arcana} Arcana) {orientation}"
        
    def set_orientation(self, is_reversed):
        """Set the orientation of the card."""
        self.is_reversed = is_reversed

    def get_meaning(self, reading_type='general'):
        """Get the meaning of the card based on its orientation."""
        meanings = self.interpretations.get(reading_type.lower(), {})
        if self.is_reversed:
            return meanings.get('reversed', 'No meaning available')
        else:
            return meanings.get('upright', 'No meaning available')

        
        
