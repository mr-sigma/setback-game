from card import Card
from hand import Hand
from deck import Deck
from player import Player

class Setback:
    def __init__(self, num_players = 3, num_cpu = 0):
        self.num_players = num_players
        self.num_cpu = num_cpu
        self.deck = Deck()
        self.community = Hand()
        # need to find a way to generate computer players
        self.players = [
            Player(i + 1,
                True if i >= num_cpu else False
            ) for i in range(self.num_players)
        ]
        self.dealer = 0
        self.bid_winner = 0
        self.winning_bid = 0

    def __str__(self):
        to_return = ""
        return to_return

    def deal(self):
        deal_counter = 0
        while self.deck.cards_remaining() > 0:
            self.players[deal_counter % 4].hand.add_card([self.deck.deal()])

    def bid(self):
        valid = [0, 2, 3, 4, 5]
        # bid_list = [0 for dummy_i in range(self.num_players)]
        winning_bid = 0
        for i in range(self.num_players):
            # bid_list[i] = players[i % self.dealer].player_bid()
            current_bid = self.players[(i + self.dealer) % self.num_players].player_bid()
            print("Player {} bids {} points".format(i + 1, current_bid))
            if current_bid > winning_bid:
                winning_bid = current_bid
                bid_winner = i

        if winning_bid == 0:
            bid_winner = self.dealer
            winning_bid = 2
            print("Dealer takes force bid for two (2) points")
        else:
            print("Player {} wins the bid with {} points".format(bid_winner + 1, winning_bid))


    def play(self):
        self.deck.shuffle()
        self.deal()
        self.bid()
