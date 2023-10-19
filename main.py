import random
import shoe

def make_cards():
    deck_instance = shoe.BaccaratDeck()
    deck = deck_instance.get_deck()
    return deck.copy()  # Return a static copy of the ordered shoe

ready_deck = make_cards()
random.shuffle(ready_deck)  # Shuffle the ready_deck before using it for simulation
static_deck = ready_deck.copy()

print(static_deck)
print(static_deck)
print(static_deck[3])
print(static_deck[:5])