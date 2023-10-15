import random

class BaccaratDeck:
    def __init__(self, total_decks=8):
        self.ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.total_decks = total_decks
        self.new_deck = []
        self._prepare_deck()

    def _prepare_deck(self):
        for _ in range(self.total_decks):
            for rank in self.ranks:
                for _ in range(8):  # You're adding each rank 8 times, is this intentional?
                    self.new_deck.append(rank)
        random.shuffle(self.new_deck)

    def get_deck(self):
        return self.new_deck

# Usage
deck_instance = BaccaratDeck()
another_variable = deck_instance.get_deck()
print(another_variable)

