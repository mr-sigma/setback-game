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
        count = 0
        for card in self.hand:
            to_return += string.ascii_lowercase[count] +\
            ") " +\
            card.__str__() + '\n'
            count += 1
        return to_return

    def number_of_cards(self):
        """
        Returns the number of cards in the hand
        """
        return len(self.hand)

    def add_card(self, *args):
        """
        Takes a list of cards and adds them to the hand
        """
        for card in args:
            self.hand.append(card)

    def play_card(self, index):
        return self.hand.pop(index)
