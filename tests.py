from card import Card
from hand import Hand
from deck import Deck
from player import Player
from setback import Setback

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
print("full hand:", hand, "\n")
empty_hand.add_card(a)
empty_hand.add_card(b)
print("empty hand added card:", '\n', empty_hand, "\n")
print("played card:", empty_hand.play_card(1))

print("-----------More Hand Tests-----------")
hand1 = Hand(a,b)
hand2 = Hand(c)
print("hand1", hand1)
print("hand2", hand2)

print("----------Deck Tests----------")
deck = Deck()
deck.shuffle()
print(deck)
a = deck.deal()
print("Dealt card:", a)
print(deck, "\n")

print("-----------Deck-Hand Interactions----------")
deck = Deck()
hand1 = Hand()
hand2 = Hand()
deck.shuffle()
hand1.add_card(deck.deal())
hand2.add_card(deck.deal())
print(hand1)
print(hand2)
while deck.cards_remaining() > 0:
    if deck.cards_remaining() % 2 == 0:
        hand1.add_card(deck.deal())
    else:
        hand2.add_card(deck.deal())
print(hand1)
print(hand2)


print("----------Player Tests----------")
player = Player(12, True, Hand(a, b, c))
player.print_hand()
player.player_bid(2)
player.play_card("a")
player.print_hand()

print("----------Setback Tests----------")
setback = Setback()
card1 = setback.deck.deal()
card2 = setback.deck.deal()
print(card1)
print(card2)
setback.players[0].hand.add_card(card1)
setback.players[1].hand.add_card(card2)
print("Cards remaining: ",setback.deck.cards_remaining())
print(setback.players[0].hand.number_of_cards())
setback.players[1].print_hand()
setback.players[2].print_hand()
print(setback.community)
# print(setback)
# setback.play()
