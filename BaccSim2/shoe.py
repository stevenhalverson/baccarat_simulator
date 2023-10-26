class BaccaratDeck:
    def __init__(self, total_decks=8):
        self.ranks = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 
                      4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 
                      7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9,  
                      0, 0, 0, 0,
                      0, 0, 0, 0,
                      0, 0, 0, 0,
                      0, 0, 0, 0]
        
        self.total_decks = total_decks
        self.new_deck = []
        self._prepare_shoe()

    def _prepare_shoe(self):
        for _ in range(self.total_decks):
            for rank in self.ranks:
                self.new_deck.append(rank)
                
    def get_deck(self):
        return self.new_deck.copy# This returns a copy of the list
    
