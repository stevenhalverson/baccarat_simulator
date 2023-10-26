import random
import shoe


class HouseRules():
    def __init__(self):
        self.tie_odds = 8
        self.dragon_odds = 40
        self.panda_odds = 25
        self.pair_odds = 11

        self.cut_back = 14
        self.cut_front = 0

        self.min_bet = 0

        self.free_hands = 1000

        self.player_total = 0
        self.banker_total = 0


        self.player_draw_third = False
        self.banker_draw_third = False

        self.player_spot = 0
        self.banker_spot = 0
        
        self.panda_pay_out = 0
        self.tie = 0         


    def tie_condition(self, player_total, banker_total):
        if player_total == banker_total:
            self.tie = self.tie_odds
        else:
            self.tie = 0

    def panda_condition(self):
            if self.player_draw_third == True:
                    if self.banker_total < self.player_total:
                        if self.player_total == 8:
                            self.panda_pay_out = self.panda_odds
                        else:
                             self.panda_pay_out = 0
            else: 
                self.panda_pay_out = 0
