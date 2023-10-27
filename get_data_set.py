import the_cards
import the_deal
import shoe
import baccarat_sim_draft



if __name__=="__main__":
    sim = baccarat_sim_draft.BaccaratSimulation(rounds=100)
    sim.run_simulation()
    print(sim.decks)
    

    