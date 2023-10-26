
import random

class Shoe:
    def __init__(self, decks):
        self.decks = decks
        self.cards = []
        self.shuffle()

    def shuffle(self):
        # Each deck has 52 cards
        self.cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"] * 4 * self.decks
        random.shuffle(self.cards)

    def deal(self):
        return self.cards.pop() if self.cards else None

class BaccaratGame:
    def __init__(self, shoe):
        self.shoe = shoe

    def play_round(self):
        print(f"Remaining cards: {len(self.shoe.cards)}") 
        if len(self.shoe.cards) < 10:  # Assume cut card at 10 cards
            print("Shuffling...")
            self.shoe.shuffle()
        player_card1, player_card2 = self.shoe.deal(), self.shoe.deal()
        banker_card1, banker_card2 = self.shoe.deal(), self.shoe.deal()
        print(f"Player's cards: {player_card1}, {player_card2}")
        print(f"Banker's cards: {banker_card1}, {banker_card2}")

# Set up the shoe with 8 decks
shoe = Shoe(decks=8)
game = BaccaratGame(shoe=shoe)

# Simulate 100 rounds of Baccarat
for i in range(200):
    print(f"Round {i + 1}")
    game.play_round()