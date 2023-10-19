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
        self.tie = 0  # Initializing tie attribute
        self.player_draw = False
        self.banker_draw = False

    def tie_condition(self, player_total, banker_total):
        if player_total == banker_total:
            self.tie = self.tie_odds
        else:
            self.tie = 0

    def dragon_condition(self, player_total, banker_total, player_draw):
            if player_draw = True
            if banker_draw_third = True
            if banker_total < player_total
