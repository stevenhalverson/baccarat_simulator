import pandas as pd
from baccarat_sim1 import BaccaratSimulation

class Get_Data_Set():
    def __init__(self):
        self.data_frame = pd.DataFrame()
        
    def update_data_set(self, result):
        temp_df = pd.DataFrame([result])
        self.data_input = pd.concat([self.data_frame, temp_df], ignore_index=True)

def main():
    sim = BaccaratSimulation()
    
    data = sim.begin_simulation(shoes=200)
    print(data)

if __name__ == "__main__":
    main()
