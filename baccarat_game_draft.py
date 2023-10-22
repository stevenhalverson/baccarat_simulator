import random
from classes import shoe
from classes import house_rules

class BaccaratGame:
    def __init__(self):
        self.dealer = DealCards()
        self.rules = house_rules.HouseRules()
        self.reset_game()
    
    def reset_game(self):
        self.ready_deck = self.dealer.make_cards()
        random.shuffle(self.ready_deck)
        self.removed_cards = []
        # Add other initialization/reset tasks if needed
    
    def play(self):
        # Deal initial cards
        player_card_1 = self.ready_deck.pop()
        self.removed_cards.append(player_card_1)
        banker_card_1 = self.ready_deck.pop()
        self.removed_cards.append(banker_card_1)
        
        # Check for draw condition (and other game rules)
        if player_card_1 not in [6, 7, 8, 9]:
            player_card_2 = self.ready_deck.pop()
            self.rules.player_draw = True
            self.removed_cards.append(player_card_2)
        
        # ... Continue the rest of the game logic ...

if __name__ == "__main__": 
    game = BaccaratGame()
    
    for _ in range(100):
        game.play()
        game.reset_game()  # Reset the game state for the next round
