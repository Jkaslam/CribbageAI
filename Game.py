import Player
import itertools
import random

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = ['s', 'c', 'h', 'd']

class Game():
    def __init__(self):
        self.players = []
        self.score = [0] * len(players)
        self.deck = list(itertools.product(vals, suits))
        self.crib = []
        self.cut_card = []
        self.cards_played = []
        self.played_total

    # Deals a new hand, 6 to each player and 1 cut card.
    def deal():
        random_cards = random.sample(deck, 6*len(players) + 1)
        for i in range(len(players)):
            players[i].set_hand(random_cards[6*i:6*i + 6]
        cut_card = random_cards[-1]

    def score():
        # Check 15 or 31
        # Check pairs
        # Check runs
    
                                
    # Checks to see if any player has won and if they have, returns their index. 
    def check_win():
        for i in range(len(players)):
            if self.score[i] > 120:
                return i
            else:
                return -1

    # Computes the total of the current played cards.
    def comp_played_total():
        total = 0
        for card in cards_played:
            total += card[0]
        return total
    
    # Returns a list of cards the given player can play.
    def can_play(player_idx):
        return filter(lambda x: x[0] + self.played_total <= 31,player_idx.get_hand())

    
    
    
