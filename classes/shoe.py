class BaccaratDeck:
    def __init__(self, total_decks=32):
        self.ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
        self.total_decks = total_decks
        self.new_deck = []
        self._prepare_shoe()

    def _prepare_shoe(self):
        for _ in range(self.total_decks):
            for rank in self.ranks:
                self.new_deck.append(rank)

    def get_deck(self):
        return self.new_deck.copy()  # This returns a copy of the list

