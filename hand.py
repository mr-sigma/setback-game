"""

"""
class Hand():
    def __init__(self, *args):
        self.hand = [arg for arg in args]

    def __str__(self):
        to_return = ""
        for card in self.hand:
            to_return += card.__str__() + '\n'
        return to_return
