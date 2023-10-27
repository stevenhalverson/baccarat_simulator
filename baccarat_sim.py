from get_cards import BaccaratDeck
from the_deal import DealCards
import random

class BaccaratSimulation:
    """Simulates multiple decks for Baccarat."""
    def __init__(self):
        #self.panda_bonus = panda_bonus or put as arg in __init__
      self.results = None #or [] ?

def main(rounds):
     
    for _ in range(rounds):
      c = BaccaratDeck()
      c.get_shoe(total_decks=8)

      d = DealCards(cards=c.deck)
      d.deal_cards() #erase print(), used only for test, replace w/ return. class produces "self.results"
      print(d.player_total)
      

      #r = Results()
      #r.calculate_results(self)
      #print(results_data) for return later to "results" above.         

if __name__=="__main__":
    main(2)