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
        self.player_total = None
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
        self.player_total = (self.player_card_1 + self.player_card_2) % 10
        self.banker_total = (self.banker_card_1 + self.banker_card_2) % 10

        print("player first total = "+str(self.player_total))

        if self.player_total in [0, 1, 2, 3, 4, 5]:
            self.player_card_3 = self.shoe.pop(0)
            self.player_total = (self.player_card_1 + self.player_card_2 + self.player_card_3) % 10
            print(f"player drew third card ="+str(self.player_card_3))
            return self.player_total
        
        if self.banker_total in [0, 1, 2, 3, 4, 5] and self.player_total not in [8, 9]:
            if self.banker_total in [0, 1, 2]:
                self.banker_card_3 = self.shoe.pop(0)
                self.banker_total = (self.banker_card_1 + self.banker_card_2 + self.banker_card_3) % 10
                print(f"banker drew third card")

            elif self.banker_total in [3] and self.player_card_3 in [8]:
                self.banker_total = (self.banker_card_1 + self.banker_card_2 + self.banker_card_3) % 10

            elif self.banker_total in [4] and self.player_card_3 in [2, 3, 4, 5, 6, 7]:
                self.banker_total = (self.banker_card_1 + self.banker_card_2 + self.banker_card_3) % 10

            elif self.banker_total in [5] and self.player_card_3 in [4, 5, 6, 7]:
                self.banker_total = (self.banker_card_1 + self.banker_card_2 + self.banker_card_3) % 10

            elif self.banker_total in [6] and self.player_card_3 in [6, 7]:
                self.banker_total = (self.banker_card_1 + self.banker_card_2 + self.banker_card_3 % 10)

    def deal_cards(self):

        self.shuffled_shoe()

        self.cut_shoe()

        self.baccarat_hand()
        return self.player_total

