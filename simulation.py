from get_cards import BaccaratDeck
from the_deal import DealCards
import pandas as pd
from data_access import *
from tkinter import filedialog



class BaccaratSimulation:
    """Simulates multiple decks for Baccarat."""
    def __init__(self, progress_queue=None):
        self.results = []
        self.data_frames = None
        self.shoe_count = 0
        self.db = database()
        self.progress_queue = progress_queue

    def begin_simulation(self, shoes):
        print(f'running simulation for {shoes} shoes')
        for i in range(shoes):
            c = BaccaratDeck()
            c.get_shoe(total_decks=8)
            d = DealCards(c.deck)

            self.shoe_count += 1
            progress = (i + 1) / shoes * 100
            if self.progress_queue:
                 self.progress_queue.put(progress)

            df_shoe = d.deal_cards()
            df_shoe['shoe number'] = self.shoe_count
            self.results.append(df_shoe) 
        print(f'simulation complete, dumping results to dataframe')
        self.data_frames = pd.concat(self.results, ignore_index=True)
        return self.data_frames
    
    def get_csv(self):
            # Open the save file dialog
            file_path = filedialog.asksaveasfilename(
                defaultextension='.csv',
                filetypes=[('CSV Files', '*.csv')],
                title="Save CSV File"
            )
        # Check if a file path was provided
            if file_path:
                # Save the DataFrame to the chosen CSV file
                self.data_frames.to_csv(file_path, index=False)
                print(f"Data saved to {file_path}")
            else:
                print("Save file operation cancelled.")


    def save_to_sqlite_db(self, append: bool = True):
        '''send results to local database, append or truncate and load
            pass in cli argument to append or replace here
        '''
        
        save_to_db(self.data_frames, self.db)