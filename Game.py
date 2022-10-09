import player
import itertools
import random
import cribbage_scoring as cs

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = ['s', 'c', 'h', 'd']

class Game():
    def __init__(self, players):
        self.players = players
        self.score = [0, 0]
        self.deck = list(itertools.product(vals, suits))
        self.crib = []
        self.cut_card = []
        self.cards_played = []
        self.played_total = 0
        self.turn_index = 0
        self.crib_index = 0

    # Deals a new hand, 6 to each player and 1 cut card.
    def deal(self):
        random_cards = random.sample(self.deck, 6*len(self.players) + 1)
        for i in range(len(self.players)):
            self.players[i].set_hand(random_cards[6*i:6*i + 6])
        self.cut_card = random_cards[-1]

    # Counts pegging based on the most recently played card. 
    def score(self):
        score[turn_index] += cs.peg(self.cards_played)

    # Discards two cards from the current player's hand to the crib. 
    def discard_to_crib(self, cards):
        self.crib += self.players[self.turn_index].discard(cards)
        self.turn_index = (self.turn_index + 1) % len(self.players)
        
    
                                
    # Checks to see if any player has won and if they have, returns their index. 
    def check_win(self):
        for i in range(len(self.players)):
            if self.score[i] > 120:
                return i
            else:
                return -1
        return -1 

    # Computes the total of the current played cards.
    def comp_played_total(self):
        total = 0
        for card in self.cards_played:
            total += card[0]
        return total
    
    # Returns a list of cards the given player can play.
    def can_play(self, player_idx):
        return filter(lambda x: x[0] + self.played_total <= 31,player_idx.get_hand())

    
    
    
