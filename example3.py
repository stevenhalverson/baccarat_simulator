import the_cards
import the_deal
import shoe
#import random



class BaccaratSimulation:

    def __init__(self, deck):
        self.deck = deck
        # ... any other initialization code
        

    def run_simulation(self):
        self.list = []
        self.list = self.deck
        print(self.list)
        # The core logic of your main() function goes here
        # ...

def main():
    c = the_cards.BaccaratCards()
    c.shuffle_deck()

    # For example, run the simulation 100 times
    for _ in range(100):
        sim = BaccaratSimulation(deck=c.static_deck)
        sim.run_simulation()
            # Maybe collect results, analyze data, etc.

if __name__ == "__main__":
    main()  