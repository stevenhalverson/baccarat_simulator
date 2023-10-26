import random
import shoe

class BaccaratCards:
    """Represents a deck of Baccarat cards."""

    def __init__(self):
        """Initializes a new deck of Baccarat cards."""
        self.deck_instance = shoe.BaccaratDeck()
        self.cards = self.deck_instance.get_deck()
        self.removed_cards = []
        self.static_deck = []

    def make_cards(self):
        """Returns a static copy of the ordered shoe."""
        return self.cards.copy()

    def shuffle_deck(self):
        """Shuffles the deck and returns a static copy of the shuffled deck."""
        random.shuffle(self.cards)
        self.static_deck = self.cards
        return self.static_deck

