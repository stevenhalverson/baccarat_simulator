
class Winners:
    def __init__(self):
       self.who_won = None
       self.banker_streak = 0
       self.player_streak = 0
       self.tie_streak = 0
       self.last_win = None

    def update_streak(self, winner):
        self.who_won = winner  # Update who won

        if self.who_won == "banker win":
            self.banker_streak += 1 if self.last_win == "banker win" else 1
            self.player_streak = 0
            self.tie_streak = 0

        elif self.who_won == "player win":
            self.player_streak += 1 if self.last_win == "player win" else 1
            self.banker_streak = 0
            self.tie_streak = 0

        elif self.who_won == "tie":
            self.tie_streak += 1 if self.last_win == "tie" else 1
        
        self.last_win = winner
        
    def get_streak(self):
        return {
        'banker_streak' : self.banker_streak,
        'player_streak' : self.player_streak,
        'tie_streak' : self.tie_streak,
        }

        #print(self.who_won)
        #return streak