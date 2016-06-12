"""

"""
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
        for card in self.hand:
            to_return += card.__str__() + '\n'
        return to_return

    def add_card(self, *args):
        """
        Takes a list of cards and adds them to the hand
        """
        for card in args:
            self.hand.append(card)

    def play_card(self, index):
        return self.hand.pop(index)
