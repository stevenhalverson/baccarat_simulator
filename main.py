from get_cards import BaccaratDeck
from the_deal import DealCards
import pandas as pd
from data_access import save_to_db

class BaccaratSimulation:
    """Simulates multiple decks for Baccarat."""
    def __init__(self):
        self.results = []
        self.data_frames = None
        self.shoe_count = 0

    def begin_simulation(self, shoes):
        print(f'running simulation for {shoes} shoes')
        for _ in range(shoes):
            c = BaccaratDeck()
            c.get_shoe(total_decks=8)
            d = DealCards(c.deck)
            self.shoe_count += 1
            df_shoe = d.deal_cards()
            df_shoe['shoe number'] = self.shoe_count
            self.results.append(df_shoe) 
        print(f'simulation complete, dumping results to dataframe')
        self.data_frames = pd.concat(self.results, ignore_index=True)
        return self.data_frames
    
    def get_csv(self):
        file_path = r"...output.csv" #INSERT YOUR OWN FILEPATH HERE <<<
        self.data_frames.to_csv(file_path, index=False)

    def save_to_sqlite_db(self, append: bool = True):
        '''send results to local database, append or truncate and load
            pass in cli argument to append or replace here
        '''
        save_to_db(self.data_frames)
        


def main():
    sim = BaccaratSimulation()
    sim.begin_simulation(shoes=240) # pass shoes as argument, default to 240 if nothing passed.
    sim.get_csv() # allow for db or csv output, along with append or create from scratch
    sim.save_to_sqlite_db() # we are doing both but the db is appending to the table

if __name__ == "__main__":
    main()