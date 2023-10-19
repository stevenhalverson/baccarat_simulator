import random

class BaccaratDeck:
    def __init__(self, total_decks=8):
        self.ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.total_decks = total_decks
        self.new_deck = []
        self._prepare_shoe()

    def _prepare_shoe(self):
        for _ in range(self.total_decks):
            for rank in self.ranks:
                for _ in range(8):  # You're adding each rank 8 times, is this intentional?
                    self.new_deck.append(rank)
        random.shuffle(self.new_deck)

    def get_deck(self):
        return self.new_deck.copy()  # This returns a copy of the list

# Usage (delete before implementation in main.py)
deck_instance = BaccaratDeck()
shuffled_shoe = deck_instance.get_deck()

static_shoe = shuffled_shoe.copy()  # This creates a static copy of the shuffled shoe

print(static_shoe)
print(static_shoe[3])