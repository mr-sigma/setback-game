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
        self.players = []
        for i in range(self.num_players):
            is_cpu = True if i >= self.num_cpu else False
            new_player = Player(i+1, is_cpu)
            self.players = self.players + [new_player]

        self.dealer = 0
        self.bid_winner = 0
        self.winning_bid = 0

    def __str__(self):
        to_return = ""
        # Print Players
        to_return += "Number of Players: " + str(self.num_players) + "\n"
        # Print Computers
        to_return += "Number of Computers: " + str(self.num_cpu) + "\n"
        # Print Dealer
        to_return += "Current Dealer: Player " + str(self.dealer + 1) + "\n"
        # Print len of Players array
        to_return += str(len(self.players))

        # Print Hands
        to_return += "\nPrinting Hands...\n-------------------"
        for i in range(len(self.players)):
            to_return += "Player " + str(i + 1) + "\n"
            to_return += self.players[i].print_hand()
            to_return += "\n"
        return to_return

    def deal(self):
        deal_counter = 0
        while self.deck.cards_remaining() > 0:
            # self.players[deal_counter % (self.num_players)].hand.add_card(self.deck.deal())
            # self.players[2].hand.add_card(self.deck.deal())
            self.players[deal_counter % self.num_players].hand.add_card(self.deck.deal())
            print(deal_counter%self.num_players)
            deal_counter += 1

    def bid(self):
        valid = [0, 2, 3, 4, 5]
        # bid_list = [0 for dummy_i in range(self.num_players)]
        winning_bid = 0
        for i in range(self.num_players):
            # bid_list[i] = players[i % self.dealer].player_bid()
            current_bid = self.players[i].player_bid()
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
