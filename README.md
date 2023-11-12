# Baccarat Simulator (status: incomplete)

Eight-deck shoes can be simulated of rounds of baccarat. A "shoe" is a casino term for the plastic device used to deal the cards, that roughly resembles the shape of a shoe.  

Currently, thousands or more shoes can be simulated and exported to a .db file. The .db file can be appended with multiple passes through the simulation, potentially creating a database of millions of hands of baccarat.

Data points being tracked are: banker total, player total, all cards drawn and their rank, the outcome, rounds in shoe, and winning streaks. 

The cut in the front of the shoe depends on the rank drawn of the first card. The cut in the back of the shoe is set at 14, but that value can easily be changed in the code.


### Setup
Before running the simulation, in your target directory name the database file first (example:baccarat_database.db). Otherwise there will be an error. 

To run the simulation, run main.py. In the code for main.py it should be easy to find where the numbers of shoes can be modified. 


(status: needs to add logging, convert prints to logging, GUI needed, packaging)

