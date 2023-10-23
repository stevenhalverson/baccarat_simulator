import the_cards
import the_deal
import shoe
#import random

def main():
    c = the_cards.BaccaratCards()  # Create an instance of BaccaratCards
    d = the_deal.BaccaratSim(cards=c.static_deck)     # Create an instance of BaccaratSim

    c.shuffle_deck()  # Shuffle the deck

    while len(c.static_deck) > 4:  # Assuming static_deck holds your cards
        player_cards = [c.static_deck.pop(), c.static_deck.pop()]
        banker_cards = [c.static_deck.pop(), c.static_deck.pop()]
        third_card_draw = 0

        d.player_total = d.baccarat_hand_value(player_cards)
        d.banker_total = d.baccarat_hand_value(banker_cards)

        if d.player_needs_third_card():
            player_cards.append(c.static_deck.pop())
            d.player_total = d.baccarat_hand_value(player_cards)
            third_card_draw += 1

        if d.banker_needs_third_card():
            banker_cards.append(c.static_deck.pop())
            banker_total = d.baccarat_hand_value(banker_cards)
            third_card_draw += 1

        print(d.player_total, d.banker_total)

if __name__ == "__main__":
   main()