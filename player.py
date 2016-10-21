from card import Card
from hand import Hand
import string

VALID_BIDS = [0, 2., 3., 4., 5.]

class Player:
    def __init__(self, player_number, human = True):
        self.player_number = player_number
        self.human = human
        self.hand = Hand()
        self.won_tricks = Hand()

    def player_bid(self, bid = 0):
        # if self.human:
        if True: # short circuit for the time being
            self.print_hand()
            while True:
                if not bid:
                    bid = input("Player {}, ".format(self.player_number) +
                    "what is your bid?\n(Min 2, Max 5, 0 to pass)\n>> ".format(self.player_number))
                while int(bid) not in VALID_BIDS:
                    # can break this by inputting a string
                    bid = input("\nPlease enter a valid bid\n")
                return int(bid)

        else:
            # Will implement AI for bidding later
            pass

    def print_hand(self):
        print()
        print("Hand:")
        print(self.hand)

    def play_card(self, to_play=""):
        valid_plays = string.ascii_lowercase[0:self.hand.number_of_cards()]
        while True:
            if not to_play:
                self.print_hand()
                to_play = input("Which card will you play?\n>> ")
            if to_play in valid_plays:
                self.hand.play_card(string.ascii_lowercase.index(to_play))
                break
            else:
                print("\nPlease make a valid selection\n")

    def dump_hand(self):
        self.hand.dump_hand()
