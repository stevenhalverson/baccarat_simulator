import the_cards
import new_the_deal
import new_get_cards
import shoe
import random

class BaccaratSimulation:
    """Simulates multiple decks for Baccarat."""
    def __init__(self):
        #self.panda_bonus = panda_bonus or put as arg in __init__
        pass

    def generate_cards(self):
        """Simulates multiple decks of Baccarat and returns the results."""
        c = new_get_cards.CardShoe()
        self.decks = c.get_shoe()
        return self.decks

def main():
    c = new_get_cards.CardShoe()
    prepared_shoe = c.get_shoe()

    if len(prepared_shoe) <= 14:
      prepared_shoe = c.get_shoe
      return prepared_shoe
    
    for _ in range(200):
      games = new_the_deal.DealCards()
      games.deal_cards(prepared_shoe) #passes the list of shuffled cards (sim.deck) to process as game.results. 
      if len(prepared_shoe) <= 14:
          c = new_get_cards.CardShoe
          prepared_shoe = c.get_shoe
          return prepared_shoe
    
      print(games.results)

if __name__=="__main__":
    main()