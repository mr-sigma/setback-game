from card import Card
from hand import Hand
import string

VALID_BIDS = [0, 2, 3, 4, 5]

class Player:
    def __init__(self, player_number, human = True, hand = Hand()):
        self.player_number = player_number
        self.human = human
        self.hand = hand
        self.won_tricks = Hand()

    def player_bid(self):
        # if self.human:
        if True: # short circuit for the time being
            self.print_hand()
            while True:
                bid = input("Player {}, ".format(self.player_number) +
                "what is your bid?\n(Min 2, Max 5, 0 to pass)\n>> ".format(self.player_number))
                if int(bid) in VALID_BIDS:
                    return int(bid)
                else:
                    print("\nPlease enter a valid bid\n")

        else:
            # Will implement AI for bidding later
            pass

    def print_hand(self):
        print()
        print("Your hand:")
        print(self.hand)

    def play_card(self):
        valid_plays = string.ascii_lowercase[0:self.hand.number_of_cards()]
        while True:
            self.print_hand()
            to_play = input("Which card will you play?\n>> ")
            if to_play in valid_plays:
                self.hand.play_card(string.ascii_lowercase.index(to_play))
                break
            else:
                print("\nPlease make a valid selection\n")
