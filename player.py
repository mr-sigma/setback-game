from card import Card
from hand import Hand

class Player:
    def __init__(self, human = True):
        self.human = human
        self.hand = new Hand()
        self.won_tricks = new Hand()
