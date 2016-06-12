from card import Card
from hand import Hand
from deck import Deck

print("----------Card Tests----------")
a = Card(11, "S")
b = Card(10, "H")
c = Card(14, "C")

print(a, b, c,'\n')

print("----------Hand Tests----------")
hand = Hand(a,b,c)
print(hand,"\n")
empty_hand = Hand()
print("empty hand:", empty_hand, "\n")
empty_hand.add_card(a)
empty_hand.add_card(b)
print("empty hand added card:", empty_hand, "\n")
print("played card:", empty_hand.play_card(1))

print("----------Deck Tests----------")
deck = Deck()
deck.shuffle()
print(deck)
a = deck.deal()
print("Dealt card:", a)
print(deck)
