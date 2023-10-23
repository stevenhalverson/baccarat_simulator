import place_bets

bets = place_bets.PlaceBets()

try:
    player_value = int(input())
    player_total = bets.set_player_bet(player_value)
    print("you bet " + str(player_total) + " on player")
except ValueError:
    print("Please enter a valid number.")