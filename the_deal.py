import random
import pandas as pd
from winners import Winners
from get_cards import BaccaratDeck

class DealCards:
    """Simulates a shoe of Baccarat."""
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
        self.last_win = None
        self.streak = None
        self.winners = Winners()
        
        self.df = None
        

    def cut_shoe(self):
        cut_card_value = self.shoe.pop(0)
        
        if cut_card_value == 0:
            cut_card_value = 10 
        else:
            cut_card_value = cut_card_value
        
        self.cut_front = cut_card_value
        self.shoe = self.shoe[self.cut_front:len(self.shoe)]

    def prepare_shoe(self):

        if not self.is_shoe_prepared:
            self.cut_shoe()

    #def get_current_streak(self):
         #return self.winners.get_streak(self)   ### this method doesn't seem to be used
    
    def deal_cards(self):
        self.prepare_shoe()


        rounds = 0
        outcome = None
    
        while len(self.shoe) > 14: # the main loop. includes third card rule. draws. totals. wins. need to add streaks here. 
            self.player_card_1 = self.shoe.pop(0) #draws the card. updates the shoe. 
            self.banker_card_1 = self.shoe.pop(0) 
            self.player_card_2 = self.shoe.pop(0)
            self.banker_card_2 = self.shoe.pop(0)


            self.player_total = (self.player_card_1 + self.player_card_2) % 10 #first draws of baccarat. next we determine if a third card is drawn for either of the sides
            self.banker_total = (self.banker_card_1 + self.banker_card_2) % 10
            
            if not self.player_total in [8, 9] or self.banker_total in [8, 9]:
                if self.player_total in [6, 7, 8, 9]:
                        self.player_card_3 = None

                if self.banker_total in [7, 8, 9]:
                        self.banker_card_3 = None

                if self.player_total in [0, 1, 2, 3, 4, 5] and self.banker_total not in [8, 9]:
                    self.player_card_3 = self.shoe.pop(0)
                    self.player_total = (self.player_total + self.player_card_3) % 10
                    self.p3cards= True
                
                if self.banker_total in [0, 1, 2, 3, 4, 5, 6]:
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
                            self.banker_total = (self.banker_total + self.banker_card_3) % 10


            if self.banker_total > self.player_total:
                outcome = "banker win"

            elif self.banker_total < self.player_total:
                outcome = "player win"

            else:
                self.banker_total == self.player_total
                outcome = "tie"

            
            self.winners.update_streak(winner=outcome)
            self.streak = self.winners.get_streak()

            rounds += 1

            result = [self.banker_total,                      
                      self.player_total, 
                      self.player_card_1, 
                      self.player_card_2, 
                      self.player_card_3, 
                      self.banker_card_1, 
                      self.banker_card_2, 
                      self.banker_card_3,
                      outcome,
                      rounds,
                      self.winners.banker_streak,
                      self.winners.player_streak,
                      self.winners.tie_streak,
                      ]
            
            result_df = pd.DataFrame([result], columns=["b total", "player total", "pcard1", "pcard2", "pcard3", "bcard1", "bcard2", "bcard3", "outcome", "rounds", "banker streak", "player streak", "tie streak"])

            self.df = pd.concat([self.df, result_df], ignore_index=True)  
            
            #("banker total", self.banker_total, "player total", self.player_total, "cards", "player card 1", self.player_card_1, "player card 2", self.player_card_2, "player card 3", self.player_card_3,
                     # "banker card 1", self.banker_card_1, "banker card 2", self.banker_card_2, "banker card 3", self.banker_card_3, "outcome", outcome, "round = ", rounds, self.streak) 
            

            
            self.last_win = outcome
        
        self.is_shoe_prepared = False

        return self.df



