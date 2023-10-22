import random
import shoe
import house_rules

class BaccaratGame: #maybe make this main.py and rename.
    def __init__(self):
        self.deck_instance = shoe.BaccaratDeck()
        self.deck = self.deck_instance.get_deck()
        self.removed_cards = []
        self.rule = house_rules.HouseRules()

    def make_cards(self): #is initiated in shuffled_deck(), not in play()
        return self.deck.copy()  # Return a static copy of the ordered shoe

    def shuffle_deck(self):
        ready_deck = self.make_cards()
        random.shuffle(ready_deck)
        self.static_deck = ready_deck.copy()

    def baccarat_hand_value(self, cards):
            total = sum(cards)
            return total % 10

    def player_needs_third_card(self):
        if self.banker_total in [8, 9]:
            return False 

        if self.player_total in [6, 7, 8, 9]: 
            return False
 
        else:
            return True
        
    def banker_needs_third_card(self):
        if self.player_total in [8, 9]:
            return False 
        
        elif self.banker_total in [6, 7, 8, 9]:
            return False
        
        else:
            return True
            
    def deal_cards(self):
        player_cards = [self.static_deck.pop(), self.static_deck.pop()]
        banker_cards = [self.static_deck.pop(), self.static_deck.pop()]
        self.third_card_draw = 0

        self.player_total = self.baccarat_hand_value(player_cards)
        self.banker_total = self.baccarat_hand_value(banker_cards)

        if self.player_needs_third_card():
            player_cards.append(self.static_deck.pop())
            self.player_total = self.baccarat_hand_value(player_cards)
            self.third_card_draw += 1

        if self.banker_needs_third_card():
            banker_cards.append(self.static_deck.pop())
            self.banker_total = self.baccarat_hand_value(banker_cards)
            self.third_card_draw += 1

        return self.player_total, self.banker_total, self.third_card_draw
    
    def determine_winning_bets(self):
        self.player_win = False
        self.banker_win = False
        self.tie_win = False

        if self.player_total == self.banker_total:
            self.tie_win = True
        elif self.player_total > self.banker_total:
            self.player_win = True
        elif self.banker_total > self.player_total:
            self.banker_win = True

        return self.player_win, self.banker_win, self.tie_win
        

    def play(self):
        self.shuffle_deck()
        self.deal_cards()
        self.determine_winning_bets()
        
        if self.player_win:
            print("player win") #there might be too many player wins statistically. something in the code could be making player win more than banker. 
        elif self.banker_win:
            print("banker win")
        elif self.tie_win:
            print("tie!")
            

if __name__ == "__main__": #example of main
    game = BaccaratGame()
    game.play()
