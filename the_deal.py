import random
from get_cards import BaccaratDeck

class DealCards:
    """Simulates a game of Baccarat."""
    def __init__(self, cards):
        self.shoe = cards
        self.cut_back = 14
        self.cut_front = None
        self.player_card_1 = None
        self.banker_card_1 = None
        self.player_card_2 = None
        self.banker_card_2 = None
        self.player_card_3 = None
        self.banker_card_3 = None
        self.banker_total = None
        self.player_third_card_draw = None
        self.banker_third_card_draw = None
        self.banker_win = None
        self.player_win = None
        self.tie = None

    def shuffled_shoe(self):
        random.shuffle(self.shoe)
        return self.shoe

    
    def cut_shoe(self):
        cut_card_value = self.shoe.pop(0)
        
        if cut_card_value == 0:
            cut_card_value = 10 
        else:
            cut_card_value = cut_card_value
        
        self.cut_front = cut_card_value
        self.shoe = self.shoe[self.cut_front:len(self.shoe)]



    #def pop_shoe(self):
        #self.popped = self.shoe.pop()
        #return self.popped
    
    def baccarat_hand(self):
        """Deals cards in their respective spots. Determines third card draw"""
        self.player_card_1 = self.shoe.pop()
        self.banker_card_1 = self.shoe.pop()
        self.player_card_2 = self.shoe.pop()
        self.banker_card_2 = self.shoe.pop()
        self.play_total = (self.player_card_1 + self.player_card_2) % 10

    def deal_cards(self):

        self.shuffled_shoe()
        print(self.shoe)

        self.cut_shoe()
        print(self.shoe)

        self.baccarat_hand()
        print(self.play_total)

