
from get_cards import BaccaratDeck
from the_deal import DealCards
import randomclass BaccaratSimulation:
  
    """Simulates multiple decks for Baccarat."""
    def __init__(self):
        #self.panda_bonus = panda_bonus or put as arg in __init__
      self.results = []
        

    def begin_simulation(self):
          
          c = BaccaratDeck()
          c.get_shoe(total_decks=8)
          d = DealCards(c.deck)
          result = d.deal_cards()
          self.results.append(result)

          print(self.results)
          print(len(self.results))


def main():
  sim = BaccaratSimulation()
  sim.begin_simulation()

  

        


          

          #r = Results()
          #r.calculate_results(self)
          #print(results_data) for return later to "results" above.         

if __name__=="__main__":
  main()