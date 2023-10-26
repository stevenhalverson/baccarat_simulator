import random

class CardShoe:
    def __init__(self, decks=8):
        self.ranks = [
            1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4,
            5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8,
            9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0
        ]
        self.shoe = []
        self.initialize_shoe(decks)

    def initialize_shoe(self, decks):
        for _ in range(decks):
            for rank in self.ranks:
                self.shoe.append(rank)
        return self.shoe

    def get_shoe(self):
        return self.shoe
    
    #def generate_cards(self)

# Usage
if __name__ == "__main__":
    card_shoe = CardShoe(decks=8)
    shoe = card_shoe.get_shoe()  # Get the shoe data
    
    print(len(shoe))
