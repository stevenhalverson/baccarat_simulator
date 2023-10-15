import random

ranks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
total_decks = 8
new_deck = []

for _ in range(total_decks):
    for rank in ranks:
        for _ in range(8):
            new_deck.append(rank)

# Optionally, shuffle the deck
random.shuffle(new_deck)

print(new_deck)