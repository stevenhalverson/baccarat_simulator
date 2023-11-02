# Baccarat Simulation
A work in progress.

Currently the program can simulate any amount of shoes of baccarat that a system can handle. The simulation includes tracking of the banker/player totals, if they drew a third card or not, the winning side, ties, win streaks, round in the shoe, and cards used out of the shoe (for testing card counting systems). 

The next step is being able to export as a .db file using SQLite, or using Pandas and DataFrames. The option to do either may be added instead of just one. It is not determined yet. 

Bets still need to be added. It is not clear what the best step to take is: should it be implemented in the baccarat engine itself, or should it be implemented in the interface used to analyze the results. Since "banker/player/tie" is already defined there can be a separate class/file/language altogether analyzing the results from the database/DataFrame instead of the variable within the class. 
