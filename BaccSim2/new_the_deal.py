import random
import new_get_cards

class DealCards:
    """Simulates a game of Baccarat."""
    def __init__(self,cards):
        self.cards = cards
        self.player_total = None
        self.banker_total = None
        self.third_card_draw = 0
        