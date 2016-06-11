"""
Class and associated constants for creating a card
"""

# import sys

RANK = {
2: "2",
3: "3",
4: "4",
5: "5",
6: "6",
7: "7",
8: "8",
9: "9",
10: "10",
11: "J",
12: "Q",
13: "K",
14: "A"
}

# Implement after figuring out unicode
# if sys.platform == "win32":
#     SUITS = {
#     "S": "\x06",
#     "C": "\x05",
#     "H": "\x03",
#     "D": "\x04"
#     }
# else:
#     SUITS = {
#     "S": "\xE2\x99\xA0",
#     "C": "\xE2\x99\xA3",
#     "H": "\xE2\x99\xA5",
#     "D": "\xE2\x99\xA6"
#     }

class Card:
    """
    Creates a single card
    """
    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
        # self.suit = SUITS[suit]

    def get_suit(self):
        """
        Returns the suit of the card as a string
        """
        return self.suit

    def get_rank(self):
        """
        Returns the rank of the card as a number
        """
        return self.rank

    def __str__(self):
        """
        Returns the string to print for the card
        """
        return RANK[self.rank] + " of " + self.suit
