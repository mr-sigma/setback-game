"""

"""
import string

class Hand():
    def __init__(self, cards=[]):
        """
        Is empty to begin with, will add from list of cards
        """
        self.hand = []
        if cards:
            self.add_cards(cards)

    def __str__(self):
        """
        Prints all cards in hand separated by a newline
        """
        to_return = ""
        if len(self.hand) == 0:
            to_return += "Empty"
        else:
            for i in range(len(self.hand)):
                to_return += string.ascii_lowercase[i] +\
                ") " + self.hand[i].__str__() + '\n'
        return to_return

    def get_hand(self):
        """
        Returns an array of cards
        """
        return self.hand

    def number_of_cards(self):
        """
        Returns the number of cards in the hand
        """
        return len(self.hand)

    def add_card(self, card):
        """
        Takes a single card and adds it to the hand
        """
        self.hand = self.hand + [card]

    def add_cards(self, cards):
        """
        Adds an arbitrary number of cards to the hand from a list
        """
        for card in cards:
            self.add_card(card)

    def play_card(self, index):
        """
        Pops the card at the given index and returns it
        """
        return self.hand.pop(index)

    def find_off_suit(self, suit):
        off_suit = []
        for i in range(len(self.hand)):
            card = self.hand[i]
            if card.get_suit().lower() != suit.lower():
                off_suit = off_suit + [card]
        return off_suit

    def find_suit(self, suit):
        suited = []
        for card in self.hand:
            if card.get_suit() == suit:
                suited = suited + [card]
        return suited

    def dump_hand(self):
        self.hand = []
