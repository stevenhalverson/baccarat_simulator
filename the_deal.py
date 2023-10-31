import random
from get_cards import BaccaratDeck

class DealCards:
    """Simulates a game of Baccarat."""
    def __init__(self, cards):
        self.shoe = cards
        self.is_shoe_prepared = False
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
        self.p3cards = False
        self.b3cards = False

        self.banker_win = None
        self.player_win = None

        self.tie = None

    def cut_shoe(self):
        cut_card_value = self.shoe.pop(0)
        
        if cut_card_value == 0:
            cut_card_value = 10 
        else:
            cut_card_value = cut_card_value
        
        self.cut_front = cut_card_value
        self.shoe = self.shoe[self.cut_front:len(self.shoe)]

    def prepare_shoe(self):
        #print(f"shoe before prep: {self.shoe}")
        if not self.is_shoe_prepared:
            self.cut_shoe()



    def deal_cards(self):
        self.prepare_shoe()
        results = []
        rounds = 0
    
        while len(self.shoe) > 14:
            self.player_card_1 = self.shoe.pop(0) #creates the cards. updates the shoe. 
            self.banker_card_1 = self.shoe.pop(0)
            self.player_card_2 = self.shoe.pop(0)
            self.banker_card_2 = self.shoe.pop(0)

            self.player_total = (self.player_card_1 + self.player_card_2) % 10 #first draws of baccarat. next we determine if a third card is drawn for either of the sides
            self.banker_total = (self.banker_card_1 + self.banker_card_2) % 10

            if self.player_total in [6, 7, 8, 9]:
                 self.player_card_3 = None

            if self.banker_total in (7, 8, 9):
                 self.banker_card_3 = None

            if self.player_total in [0, 1, 2, 3, 4, 5] and self.banker_total not in [8, 9]:
                self.player_card_3 = self.shoe.pop(0)
                self.player_total = (self.player_total + self.player_card_3) % 10
                self.p3cards= True
            
            if self.banker_total in [0, 1, 2, 3, 4, 5, 6] and self.player_total not in [8, 9]:
                if self.banker_total in [0, 1, 2]:
                    self.banker_card_3 = self.shoe.pop(0)
                    self.banker_total = (self.banker_total + self.banker_card_3) % 10

            if self.banker_total in [3] and self.player_card_3 not in [8]:
                    self.banker_card_3 = self.shoe.pop(0)
                    self.banker_total = (self.banker_total + self.banker_card_3) % 10

            if self.banker_total in [4] and self.player_card_3 in [2, 3, 4, 5, 6, 7]:
                    self.banker_card_3 = self.shoe.pop(0)
                    self.banker_total = (self.banker_total + self.banker_card_3) % 10

            if self.banker_total in [5] and self.player_card_3 in [4, 5, 6, 7]:
                    self.banker_card_3 = self.shoe.pop(0)
                    self.banker_total = (self.banker_total + self.banker_card_3) % 10

            if self.banker_total in [6] and self.player_card_3 in [6, 7]:
                    self.banker_card_3 = self.shoe.pop(0)
                    self.banker_total = (self.banker_total + self.banker_card_3 % 10)
                
            rounds += 1

            result = ("banker total", self.banker_total, "player total", self.player_total, "cards", "player card 1", self.player_card_1, "player card 2", self.player_card_2, "player card 3", self.player_card_3,
                      "banker card 1", self.banker_card_1, "banker card 2", self.banker_card_2, "banker card 3", self.banker_card_3, "outcome", "round = ", rounds)

            results.append(result)
        #print(len(results))
        
        self.is_shoe_prepared = False
        return(results)


