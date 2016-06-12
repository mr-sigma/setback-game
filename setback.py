from card import Card
from hand import Hand
from deck import Deck
from player import Player

class Setback:
    def __init__(self, num_players = 3, num_cpu = 0):
        self.num_players = num_players
        self.num_cpu = num_cpu
        self.deck = new Deck()
        self.community = new Hand()
        # need to find a way to generate computer players
        self.players = [Player(True) for dummy_i in range(self.num_players)]
        self.dealer = 0

    def deal(self):
        deal_counter = 0
        while self.deck.cards_remaining() > 0:
            self.players[deal_counter % 4].hand.add_card([self.deck.deal()])

    def bid(self):
        valid = [0, 2, 3, 4, 5]
        bid_list = [0 for dummy_i in range(self.num_players)]
        for count in range(self.num_players):
            pass
