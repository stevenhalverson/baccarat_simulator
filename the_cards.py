import random
import shoe

class BaccaratCards: 
    def __init__(self):
        self.deck_instance = shoe.BaccaratDeck()
        self.cards = self.deck_instance.get_deck()
        self.removed_cards = []
        self.static_deck = []

    def make_cards(self): #is initiated in shuffled_deck(), not in play()
        return self.cards.copy()  # Return a static copy of the ordered shoe

    def shuffle_deck(self):
        ready_deck = self.make_cards() #this could be where the flaw of creating too many cards is at
        random.shuffle(ready_deck)
        self.static_deck = ready_deck.copy()
        return self.static_deck
