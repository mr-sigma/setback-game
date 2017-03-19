import unittest

from card import Card
from hand import Hand
from deck import Deck
from player import Player
from setback import Setback
import gc

class TestCardMethods(unittest.TestCase):
    """
    Test the methods of the Card class
    """
    def setUp(self):
        """
        Initilize cards of different rank and suit
        """
        self.card1 = Card(11, "S") # jack
        self.card2 = Card(13, "C") # king
        self.card3 = Card(2, "D")
        self.card4 = Card(7, "H")
        self.card5 = Card(12, "H") # queen
        self.card6 = Card(14, "S") # ace

    def test_get_suit(self):
        """
        Test get_suit method
        """
        self.assertEqual(self.card1.get_suit(), "S", "Suit should be Spades")
        self.assertEqual(self.card2.get_suit(), "C", "Suit should be Clubs")
        self.assertEqual(self.card3.get_suit(), "D", "Suit should be Diamonds")
        self.assertEqual(self.card4.get_suit(), "H", "Suit should be Hearts")

    def test_get_rank(self):
        """
        Test get_rank method
        """
        self.assertEqual(self.card1.get_rank(), 11, "Rank should be 11")
        self.assertEqual(self.card5.get_rank(), 12, "Rank should be 12")
        self.assertEqual(self.card2.get_rank(), 13, "Rank should be 13")
        self.assertEqual(self.card6.get_rank(), 14, "Rank should be 14")
        self.assertEqual(self.card4.get_rank(), 7, "Rank should be 7")

class TestHandMethods(unittest.TestCase):
    def setUp(self):
        self.card1 = Card(11, "S")
        self.card2 = Card(10, "H")
        self.card3 = Card(14, "C")
        self.card4 = Card(3, "D")
        self.hand1 = Hand([self.card1, self.card2, self.card3])
        self.hand2 = Hand()

    def test_add_card(self):
        self.assertEqual(self.hand2.number_of_cards(), 0, "hand3 is not empty to begin with")
        self.hand2.add_card(self.card4)
        self.assertEqual(self.hand2.number_of_cards(), 1, "hand3 could not add initial card")
        self.hand2.add_card(self.card1)
        self.assertEqual(self.hand2.number_of_cards(), 2, "hand3 does not contain exactly two cards after adding")

    def test_add_cards(self):
        self.assertEqual(self.hand2.number_of_cards(), 0)
        self.hand2.add_cards([self.card1, self.card2, self.card3])
        self.assertEqual(self.hand2.number_of_cards(), 3)

    def test_get_hand(self):
        self.assertIsInstance(self.hand1.get_hand(), list, "get_hand did not return an array")
        self.assertIsInstance(self.hand2.get_hand(), list, "get_hand did not return an array")

    def test_play_card(self):
        self.hand2.add_cards([self.card1, self.card2])
        played_card = self.hand2.play_card(1)
        self.assertIsInstance(played_card, Card)
        self.assertEqual(played_card.get_suit(), "H")
        self.assertEqual(played_card.get_rank(), 10)
        self.assertEqual(self.hand2.number_of_cards(), 1)

    def test_dump_hand(self):
        self.assertEqual(self.hand1.number_of_cards(), 3)
        self.hand1.dump_hand()
        self.assertEqual(self.hand1.number_of_cards(), 0)

    def test_find_suit(self):
        self.hand1.add_cards([self.card4, Card(2, "D")])
        diamonds = self.hand1.find_suit("D")
        self.assertEqual(len(diamonds), 2, "hand1 should contain exactly 2 diamonds")
        for card in diamonds:
            self.assertEqual(card.get_suit(), "D", "find_suit returned a card with an off-suit")

    def test_find_off_suit(self):
        self.hand1.add_cards([self.card4, Card(2, "D")])
        not_diamonds = self.hand1.find_off_suit("D")
        self.assertEqual(len(not_diamonds), 3)
        for card in not_diamonds:
            self.assertNotEqual(card.get_suit(), "D", "find_off_suit returned a card with a diamond")

class TestDeckMethods(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_shuffle(self):
        old_deck = self.deck.return_deck()
        self.deck.shuffle()
        self.assertNotEqual(old_deck, self.deck.return_deck(), "deck was not shuffled")

    def test_deal(self):
        self.assertEqual(self.deck.cards_remaining(), 52, "standard deck contains 52 cards")
        dealt_card = self.deck.deal()
        self.assertIsInstance(dealt_card, Card)
        self.assertEqual(self.deck.cards_remaining(), 51, "deck did not deal exactly 1 card")

class TestPlayerMethods(unittest.TestCase):
    def setUp(self):
        pass

    def test_player_bid(self):
        pass



if __name__ == '__main__':
    unittest.main()
