import random
import new_get_cards

class DealCards:
    """Simulates a game of Baccarat."""
    
    player_total = None
    banker_total = None

    def __init__(self, cards):
        """Initializes a new Baccarat simulator, with the given deck of cards."""
        self.cards = cards

    def baccarat_hand_value(self, cards):
        """Returns the Baccarat hand value of the given cards."""
        total = sum(cards)
        return total % 10

    def player_needs_third_card(self):
        """Returns True if the player needs a third card, False otherwise."""
        return self.player_total in [0, 1, 2, 3, 4, 5]

    def banker_needs_third_card(self):
        """Returns True if the banker needs a third card, False otherwise."""
        if self.player_total in [8, 9]:
            return False
        elif self.banker_total in [6, 7, 8, 9]:
            return False
        else:   #### !!!!!!!!!! this is not correct. banker draws based on the third card drawn by player if a third card is drawn. this must be redone
            return True
        
    def shuffle_decks():
        c = new_get_cards.CardShoe
        c.get_shoe()

    def deal_cards(self):
        """Deals two cards to the player and two cards to the banker.

        Returns a tuple containing the player's total, the banker's total, and the number of third cards drawn.
        """
        
        ready = self.cards

        self.results =[]
        player_cards = [ready.pop(), ready.pop()]
        banker_cards = [ready.pop(), ready.pop()]
        third_card_draw = 0

        self.player_total = self.baccarat_hand_value(player_cards)
        self.banker_total = self.baccarat_hand_value(banker_cards)

        if self.player_needs_third_card():
            player_cards.append(ready.pop())
            self.player_total = self.baccarat_hand_value(player_cards)
            third_card_draw += 1

        if self.banker_needs_third_card():
            banker_cards.append(self.cards.pop())
            self.banker_total = self.baccarat_hand_value(banker_cards)
            third_card_draw += 1

        self.results = (self.player_total, self.banker_total, third_card_draw)
        
        if len(ready) <= 14:
            c = new_get_cards.CardShoe
            self.cards = c.get_shoe
        return [self.results, self.cards]
        
        
        
        return self.results

    def determine_winning_bets(self):
        """Determines the winning bets for the current game of Baccarat.

        Returns a tuple containing the following Boolean values:

        * player_win: True if the player won, False otherwise.
        * banker_win: True if the banker won, False otherwise.
        * tie_win: True if there is a tie, False otherwise.
        """

        player_win = False
        banker_win = False
        tie_win = False

        if self.player_total == self.banker_total:
            tie_win = True
        elif self.player_total > self.banker_total:
            player_win = True
        elif self.banker_total > self.player_total:
            banker_win = True

        return player_win, banker_win, tie_win

        if self.player_total == self.banker_total:
            self.tie_win = True
        elif self.player_total > self.banker_total:
            self.player_win = True
        elif self.banker_total > self.player_total:
            self.banker_win = True

        return self.player_win, self.banker_win, self.tie_win
        
