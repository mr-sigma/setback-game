# setback script
import random
import time
class SetDeck:
    def __init__(self, players = 3):
        self.deck = []
        self.players = players
        self.hands = []
        self.community = []
        self.tricks = []
        self.points = []
        self.winning_bid = 0
        self.bid_winner = 0 # Will be within [1, players] inclusively
        self.trump = ""
        self.dealer = 2 # player 2 will deal first
        
        for i in range(players):
            self.community.append("")
            self.tricks.append([])

        
        
    def shuffle(self):
        suits = ["D", "S", "H", "C"]
        cards = [str(x) for x in range(2,11)]
        cards.extend(["J", "Q", "K", "A"])
        deck = [x+"_"+y for y in suits for x in cards]
        random.shuffle(deck) # shuffle works in place and returns none
        self.deck = deck
        
    def deal(self):
        for x in range(self.players):
            self.hands.append([0,0,0,0,0,0])
        for i in range(6):
            for j in range(0, self.players):
                self.hands[j][i] = self.deck.pop(len(self.deck) - 1)
                
    def print_hand(self, player_num):
        print "\n"
        print "Player %d: " % (player_num) + ", ".join(self.hands[player_num-1])
            
    def bid(self):
        valid = [0,2,3,4]
        bid_list = []
        for i in range(self.players):
            bid_list.append(0)
        count = 0
        who_bid = self.dealer + 1
        win_bid = 1
        while count < self.players:
            if who_bid > self.players:
                who_bid = 1
            self.print_hand(who_bid)
            choice = raw_input("Player %d, what is your bid?\nMin 2, Max 4, 0 to Pass\n>" % (who_bid))
            if choice: #player enters something
                if int(choice) in valid: # player enters a valid number
                    if int(choice) == win_bid: 
                        print "\nYou must raise the bid or pass\n"
                    else:
                        bid_list[who_bid-1] = int(choice)  
                        count += 1
                        who_bid += 1
                    if int(choice) > win_bid: # player makes highest bid
                        win_bid = int(choice)
                else: print "\nPlease enter a valid bid\n"
            else: print "\nPlease enter a valid bid\n"
        
        bid_switch = all(item < 2 for item in bid_list)
        if bid_switch:
            print "\nDealer (Player %d) takes the bid for 2\n" % (self.dealer)
            bid_list[self.dealer - 1] = 2
            win_bid = 2
        self.bid_winner = (bid_list.index(win_bid) + 1)
        self.winning_bid = win_bid
        
    def pick_trump(self, bid_winner):
        valid = ["a", "b", "c", "d"]
        trumps = {"a":"S", "b":"C", "c":"H", "d":"D"}
        while True:
            print "\nPlayer %d, please select a trump suit" % (bid_winner)
            self.print_hand(bid_winner)
            choice = raw_input("\n  a) Spades\n  b) Clubs\n  c) Hearts\n  d) Diamonds\n\n>")
            choice = choice.lower()
            if choice in valid:
                self.trump = trumps[choice]
                break
            else: print "Please enter a valid choice\n"
        pass
        
    def redraw(self):
        print "\nDiscarding non-trump cards"
        temp = []
        for i in range(self.players):
            temp = self.hands[i]
            temp2 = [x for x in temp if self.trump in x]
            while len(temp2) < 6:
                temp2.append(self.deck.pop(len(self.deck) - 1))
            self.hands[i] = temp2
            print self.hands[i]
        pass
        
    def clear_community(self):
        for i in range(len(self.community)):       
            self.community[i] = ""
        pass
        
    def clear_tricks(self):
        for i in range(self.players):
            self.tricks[i] = []
        pass
        
    def convert_face(self, val):
        count = 0
        for thing in val:
            if thing == "J":
                val[count] = 11
            elif thing == "Q":
                val[count] = 12
            elif thing == "K":
                val[count] = 13
            elif thing == "A":
                val[count] = 14
            else:
                val[count] = int(val[count])
            count += 1
        return val

    def card_split(self, cards):
        suit = []
        val = []
        temp = cards
        for i in range(self.players):
            val.append("")
            suit.append("")
        for i in range(len(cards)):
            val[i] = temp[i].split("_")[0] 
            suit[i] = cards[i][-1]
        return (val, suit) # returns a tupple which requires unpacking
        pass
    
    def trick_logic(self, lead_suit):
        # temp = self.community
        # suit = []
        # val = []
        # for i in range(self.players):
            # val.append("")
            # suit.append("")
        # for i in range(len(self.community)):
            # val[i] = temp[i].split("_")[0] 
            # suit[i] = self.community[i][-1]
        val, suit = self.card_split(self.community)
        val = self.convert_face(val)
        count = 0
        for thing in suit:
            if thing == lead_suit and lead_suit != self.trump:
                val[count] += 20
            elif thing == self.trump:
                val[count] += 40
            count+= 1
        
        high_card = max(val)
        winner = 1 + val.index(high_card)
        print"\nPlayer %d wins the trick with the %s" % (winner, self.community[winner-1])
        self.tricks[winner-1].extend(self.community)
        self.clear_community()
        
        # X = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
        # Y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
        # [x for (y,x) in sorted(zip(Y,X))]
        return winner
        pass
        
    def play_round(self):
        trick_start = self.bid_winner
        lead_suit = self.trump
        print "\nPlayer %d, lead with the trump suit (%s)" % (trick_start, self.trump)
        go = trick_start
        for i in range(6):
            for j in range(self.players):
                if j == 0: # first card played for the trick
                    if i == 0: # first card played in the round
                       lead_suit = self.play_hand(go, self.trump)
                    else:
                        lead_suit = self.play_hand(go)
                else:
                    self.play_hand(go, lead_suit)
                print "\n"
                print self.community #display tricks so that players can choose appropriate card
                go += 1
                if go > self.players: go = 1
            go = self.trick_logic(lead_suit)
                
    def play_hand(self, player, lead_suit = "all"):
        letters = ["a", "b", "c", "d", "e", "f"]
        if lead_suit == "all":
            temp = self.hands[player-1]
            letters_temp = letters
        elif lead_suit == self.trump:
            temp = [x for x in self.hands[player-1] if self.trump in x]
            if len(temp) == 0:
                temp = self.hands[player-1]
        else:
            temp1 = [x for x in self.hands[player-1] if lead_suit in x and lead_suit != self.trump]
            if len(temp1) == 0:
                temp = self.hands[player-1]
            else:
                temp2 = [x for x in self.hands[player-1] if self.trump in x]
                temp = temp1+temp2
        letters_temp = letters[:len(temp)] 
        # if lead_suit == "all":
            # temp = self.hands[player-1]
            # letters_temp = letters
        # else:
            # temp = [x for x in self.hands[player-1] if lead_suit in x or self.trump in x]
            # letters_temp = letters[:len(temp)]
        # if len(temp) == 0:
            # temp = self.hands[player-1]
        while True:
            print "\nPlayer %d, please choose a card\n" % (player)
            print "Valid Plays:\n"
            for i in range(len(temp)):
                print letters[i] + ") " + temp[i]
            print "\n" 
            play = raw_input("\n>")
            if play.lower() in letters_temp: 
                play = temp[letters_temp.index(play)]
                if lead_suit == "all":
                    card_temp = play.split("_")
                    lead_suit = card_temp[1]
                self.community[player - 1] = play
                self.hands[player-1].remove(play)
                break
                pass
            else:
                print "\nPlease enter a valid choice\n"
        return lead_suit
        
    def scoring(self):
        game_point = []
        
        for trick in self.tricks:
            trick_val, trick_suit = self.card_split(trick)
            val_temp = self.convert_face(trick_val)
            game_point.append(got_game(val_temp))
            for i in range(len(trick)):
                if trick_suit[i] == self.trump:
                    trump_temp.append(trick_val[i])
            
            # convert to numbers
            # calculate game
            # discard non-trump
            # find high,low,jack
            # append to self.points
        pass
        
    def got_game(self, trick):
        temp = [x for x in trick if x >9]
        count = 0
        if len(temp) == 0:
            return 0
        for thing in temp:
            if thing != 10:
                temp[count] -= 10
            count += 1
        return sum(temp)
        
            
    def run(self):
        for i in range(self.players): #initialize score
            self.points.append(0)
        
        while True: # go until the loop breaks when someone wins
            self.shuffle()
            self.deal()
            self.bid()
            self.pick_trump(self.bid_winner)
            self.redraw()
            self.play_round()
            self.scoring()
            self.game_over()
            #gameplay
            self.dealer += 1
            self.bid_winner = 0
            self.winnidng_bid = 0
            self.clear_tricks()
            if self.dealer > self.players: self.dealer = 1
            pass
            
        
        
        
        pass
        
        
        
        
setback = SetDeck()
setback.shuffle()
setback.deal()
setback.bid()
setback.pick_trump(setback.bid_winner)
setback.redraw()
setback.play_round()

# print setback.got_game([10, 10, 14, 13])
# print setback.card_split(["K_S","A_D","10_H"])
# print setback.card_split([])