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

        # General Stats
        to_return += "\n-------------------\nGeneral Stats\n-------------------\n"
        # Print Players
        to_return += "Number of Players: " + str(self.num_players) + "\n"
        # Print Computers
        to_return += "Number of Computers: " + str(self.num_cpu) + "\n"
        # Print Dealer
        to_return += "Current Dealer: Player " + str(self.dealer + 1) + "\n"

        # Print Hands
        to_return += "\n-------------------\nPrinting Hands\n-------------------\n"
        for i in range(len(self.players)):
            to_return += "<<Player " + str(i + 1) + ">>\n"
            to_return += self.players[i].hand.__str__() + "\n"
            to_return += "\n"

        to_return += "<<Trick>>\n" + self.community.__str__()
        return to_return

    def deal(self):
        deal_counter = 0
        for dummy_i in range(6 * self.num_players):
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
            if current_bid > winning_bid or (current_bid == winning_bid and i == self.dealer):
                winning_bid = current_bid
                bid_winner = i

        if winning_bid == 0:
            bid_winner = self.dealer
            winning_bid = 2
            print("Dealer takes force bid for two (2) points")
        else:
            print()
            print("----------------End of Bidding----------------")
            print("Player {} wins the bid with {} points\n".format(bid_winner + 1, winning_bid))
        return bid_winner, winning_bid

    def pick_trump(self, bidder):
        """

        """
        suits = ["S", "C", "H", "D"]
        print("\nPlayer {}, please select a Trump suit:\n(S)pades\n(C)lubs\n(D)iamonds\n(H)earts\n".format(bidder + 1))
        self.players[bidder].print_hand()

        choice = input(">>").upper()

        while choice.upper() not in suits:
            self.players[bidder].print_hand()
            choice = input("Please select a valid suit:\n(S)pades\n(C)lubs\n(D)iamonds\n(H)earts\n>>").upper()

        return choice

    def round(self, trump, bidder):
        # whoever won bid goes first
        # lead with trump

        pass

    def play(self):
        # Shuffle and deal
        self.deck.shuffle()
        self.deal()

        # Bid and let the winner pick the trump suit
        bid_winner, winning_bid  = self.bid()
        trump_suit = self.pick_trump(bid_winner)

        # Discard and re-draw?
        for player in self.players:
            off_trump = player.hand.find_off_suit(trump_suit)
            player.hand.play_cards(off_trump)
            while player.hand.number_of_cards() != 6:
                player.hand.add_card(self.deck.deal())
            player.print_hand()

        # Play a round with the given trump suit and bidder
