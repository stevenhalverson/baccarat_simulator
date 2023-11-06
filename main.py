from get_cards import BaccaratDeck
from the_deal import DealCards
import random
import time
import pandas as pd

class BaccaratSimulation:
    """Simulates multiple decks for Baccarat."""
    def __init__(self):
        self.results = []
        self.data_frames = None
        self.shoe_count = 0

    def begin_simulation(self, shoes):

        for _ in range(shoes):
            c = BaccaratDeck()
            c.get_shoe(total_decks=8)
            d = DealCards(c.deck)
            self.shoe_count += 1
            df_shoe = d.deal_cards()
            df_shoe['shoe number'] = self.shoe_count
            self.results.append(df_shoe) 

        self.data_frames = pd.concat(self.results, ignore_index=True)
        return self.data_frames
    
    def get_csv(self):
        file_path = r"...output.csv" #INSERT YOUR OWN FILEPATH HERE <<<
        self.data_frames.to_csv(file_path, index=False)


def main():
    sim = BaccaratSimulation()
    sim.begin_simulation(shoes=240)
    sim.get_csv()


if __name__ == "__main__":
    main()