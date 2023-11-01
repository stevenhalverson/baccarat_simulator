from get_cards import BaccaratDeck
from the_deal import DealCards
import random

class BaccaratSimulation:
    """Simulates multiple decks for Baccarat."""
    def __init__(self):
      
      self.results = []
        

    def begin_simulation(self, shoes):
          
      for _ in range(shoes):
        c = BaccaratDeck()
        c.get_shoe(total_decks=8)
        d = DealCards(c.deck)
        result = d.deal_cards()
        self.results.append(result)

        #print(self.results) this created factorial like growth when printing. it should be OUTSIDE of teh loop
        #print(len(self.results))

      print(len(self.results))
      print(self.results)


def main():
  sim = BaccaratSimulation()
  sim.begin_simulation(shoes=2)


if __name__=="__main__":
  main()