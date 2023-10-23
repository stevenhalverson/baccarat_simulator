import random

class BaccaratSim: #maybe make this main.py and rename.
    def __init__(self, cards):
        self.cards = cards

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
            
    def deal_cards(self, x):
        player_cards = [x.pop(), x.pop()]
        banker_cards = [x.pop(), x.pop()]
        self.third_card_draw = 0

        self.player_total = self.baccarat_hand_value(player_cards)
        self.banker_total = self.baccarat_hand_value(banker_cards)

        if self.player_needs_third_card():
            player_cards.append(self.x.pop())
            self.player_total = self.baccarat_hand_value(player_cards)
            self.third_card_draw += 1

        if self.banker_needs_third_card():
            banker_cards.append(self.x.pop())
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
        
