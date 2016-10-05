"""

"""
import string

class Hand():
    def __init__(self, *args):
        """
        Accepts any arbitrary number of cards
        """
        self.hand = [arg for arg in args]

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

    def number_of_cards(self):
        """
        Returns the number of cards in the hand
        """
        return len(self.hand)

    def add_card(self, card):
        """
        Takes a list of cards and adds them to the hand
        """
        self.hand.append(card)

    def add_cards(self, *args):
        for card in args:
            self.add_card(card)

    def play_card(self, index):
        return self.hand.pop(index)
