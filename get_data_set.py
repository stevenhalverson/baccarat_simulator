import pandas as pd
from baccarat_sim import BaccaratSimulation

class Get_Data_Set():
    def __init__(self, results):
        self.results = results
        
    def get_data_set(self):
        self.data_frame = pd.DataFrame(self.results)
        return self.data_frame

    def save_to_csv(self, file_name='BaccaratData.csv', index=False):
        self.data_frame.to_csv(file_name, index=index)

def main():
    sim = BaccaratSimulation()
    data = sim.begin_simulation(shoes=200)
    df = Get_Data_Set(data)
    BaccaratDataFrame = df.get_data_set()
    #df.save_to_csv()
    print(BaccaratDataFrame)

if __name__ == "__main__":
    main()
