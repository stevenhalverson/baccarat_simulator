

class PlaceBets():
    def __init__(self):
        self.player_bet = 0
        self.banker_bet = 0
        self.tie_bet = 0
        self.dragon_bet = 0
        self.panda_bet = 0
        self.pairs_bet = 0

    def set_player_bet(self, player):
        self.player_bet = player
        return self.player_bet

    def set_banker_bet(self, banker):
        self.banker_bet = banker
        return self.banker_bet

    def set_tie_bet(self, tie):
        self.tie_bet = tie
        return self.tie_bet

    def set_dragon_bet(self, dragon):
        self.dragon_bet = dragon
        return self.dragon_bet

    def set_panda_bet(self, panda):
        self.panda_bet = panda
        return self.panda_bet

    def set_pairs_bet(self, pairs):
        self.pairs_bet = pairs
        return self.pairs_bet

