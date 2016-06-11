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

print("----------Deck Tests----------")
deck = Deck()
deck.shuffle()
print(deck)
a = deck.deal()
print("Dealt card:", a)
print(deck)
