class BaccaratDeck:

    RANKS = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 
    4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 
    7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,  
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0,
    0, 0, 0, 0]

    def __init__(self):
        self.deck = []

    def get_shoe(self, total_decks):
        self.deck = self.RANKS*total_decks