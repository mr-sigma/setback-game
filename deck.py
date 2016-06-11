from card import Card
import random

class Deck:
    def __init__(self):
        """
        Creates deck and shuffles it
        """
        self.deck = []
        self.shuffle()
        pass

    def __str__(self):
        """
        Prints out the cards in the deck
        """
        to_return = ""
        for card in self.deck:
            to_return += card.__str__() + "\n"
        return to_return

    def shuffle(self):
        """
        Rewrites the deck array with a full 52 card set
        """
        self.deck = [ Card(rank, suit) for suit in ["S", "C", "H", "D"] for rank in range(2,15) ]
        random.shuffle(self.deck)

    def deal(self):
        """
        Deals one card from the top of the deck
        """
        return self.deck.pop()

    def cards_remaining(self):
        """
        Returns the number of cards remaining in the deck
        """
        return len(self.deck)
