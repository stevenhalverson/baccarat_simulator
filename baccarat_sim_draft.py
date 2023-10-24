import the_cards
import the_deal
import shoe
import random

class BaccaratSimulation:
    """Simulates multiple games of Baccarat."""

    third_card_draw = 0

    def __init__(self, rounds):
        """Initializes a new Baccarat simulator, with the given number of rounds to play."""
        self.rounds = int(rounds)
        self.results = []
        

    def run_simulation(self):
      """Simulates multiple games of Baccarat and returns the results."""

      c = the_cards.BaccaratCards()
      d = the_deal.BaccaratSim(cards=c.static_deck)

      results = []

      while self.rounds > 0:

        # Reshuffle the deck if necessary
        if len(c.static_deck) <= 14:
          c.shuffle_deck()
          print(results)
          print("shuffled")

        player_cards = [c.static_deck.pop(), c.static_deck.pop()]
        banker_cards = [c.static_deck.pop(), c.static_deck.pop()]

        player_total = d.baccarat_hand_value(player_cards)
        banker_total = d.baccarat_hand_value(banker_cards)

        if d.player_needs_third_card():
          if player_total < 6:
            player_cards.append(c.static_deck.pop())
            player_total = d.baccarat_hand_value(player_cards)
            self.third_card_draw += 1
          

        if d.banker_needs_third_card():
          if banker_total < 6:
            banker_cards.append(c.static_deck.pop())
            banker_total = d.baccarat_hand_value(banker_cards)
            self.third_card_draw += 1
        

        results.append((player_total, banker_total, self.third_card_draw))
        self.rounds -= 1

      print(results)
      return results
        
    
if __name__=="__main__":
    sim = BaccaratSimulation(rounds=100)
    sim.run_simulation()