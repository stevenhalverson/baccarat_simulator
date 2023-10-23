import the_cards
import the_deal
import shoe
#import random

def prepare_shoe(cards_obj):
   cards_obj.shuffle_deck()
   x = cards_obj
   return x

#def set_strategies():

def dealer(dealt_cards):
   dealt_cards.deal_cards()

#def get_results():

def main():

   c = the_cards.BaccaratCards()
   d = the_deal.BaccaratSim



   for _ in range(11):
      x= c.shuffle_deck()
      player_cards = [x.pop(), x.pop()]
      banker_cards = [x.pop(), x.pop()]
      third_card_draw = 0

      player_total = d.baccarat_hand_value(player_cards)
      banker_total = d.baccarat_hand_value(banker_cards)

      if d.player_needs_third_card():
            player_cards.append(x.pop())
            player_total = d.baccarat_hand_value(player_cards)
            d.third_card_draw += 1

      if d.banker_needs_third_card():
            banker_cards.append(x.pop())
            banker_total = d.baccarat_hand_value(banker_cards)
            third_card_draw += 1

      return player_total, banker_total, third_card_draw
      #game logic
      #game.reset_game()
      pass


if __name__ == "__main__":
   main()