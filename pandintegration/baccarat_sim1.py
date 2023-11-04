from get_cards import BaccaratDeck
from the_deal1 import DealCards
import random
import time

class BaccaratSimulation:
    """Simulates multiple decks for Baccarat."""
    def __init__(self):
        self.results = []
        self.data_frame = None

    def begin_simulation(self, shoes):

        for _ in range(shoes):
            shoe_count = 0
            c = BaccaratDeck()
            c.get_shoe(total_decks=8)
            d = DealCards(c.deck)
            shoe_count += 1
            self.data_frame = d.deal_cards()
            
        return(self.data_frame)
        #print(self.results) this created factorial like growth when printing. it should be OUTSIDE of teh loop
        #print(len(self.results))

      #print(self.results[-1])
      #print(self.results)

def main():
    sim = BaccaratSimulation()
    sim.begin_simulation(shoes=10)
    print(sim.data_frame)

if __name__ == "__main__":
    main()