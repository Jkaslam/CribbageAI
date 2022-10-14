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
        self.go = False

    # Deals a new hand, 6 to each player and 1 cut card.
    def deal(self):
        random_cards = random.sample(self.deck, 6*len(self.players) + 1)
        for i in range(len(self.players)):
            self.players[i].set_hand(random_cards[6*i:6*i + 6])
        self.cut_card = random_cards[-1]

    # Counts pegging based on the most recently played card. 
    def update_score(self):
        self.score[self.turn_index] += cs.peg(self.cards_played)

    # Discards two cards from the current player's hand to the crib.
    # Also saves the 4 chosen cards to the player's final hand for
    # scoring.
    def discard_to_crib(self, cards):
        curr_player = self.players[self.turn_index]
        self.crib += curr_player.discard(cards)
        curr_player.set_hand_for_scoring(curr_player.get_hand())
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
            print(card)
            total += min(card[0], 10)
        return total
    
    # Returns a list of cards the given player can play.
    def can_play(self, player_idx):
        for card in self.players[player_idx].get_hand():
            print(min(card[0], 10) + self.played_total)
        return list(filter(lambda x: min(x[0], 10) + self.played_total <= 31, self.players[player_idx].get_hand()))

    # Returns the cut card for the current hand.
    def get_cut_card(self):
        return self.cut_card
    
    # Checks to see if the cut card is a jack. 
    def check_nibs(self):
        if (self.cut_card[0] == 11):
            self.score[self.turn_index] += 2

    # Returns the current list of cards that have been played this hand.
    def get_cards_played(self):
        return self.cards_played

    # Adds a recently played card to the pile of cards that have been played. 
    def update_cards_played(self, card):
        self.cards_played += [card]
        self.played_total += card[0]

    # Let's us know whose turn it is. 
    def get_turn_index(self):
        return self.turn_index

    # Updates the turn index to the next player's turn.
    def next_turn(self):
        self.turn_index = (self.turn_index + 1) % len(self.players)

    # Adds 1 to the score of the next player after the current player
    # couldn't play.
    def call_go(self):
        self.next_turn()
        self.score[self.turn_index] += 1

    # Returns the current players.
    def get_players(self):
        return self.players

    # Resets the cards that have been played after 
    def reset_cards_played(self):
        self.cards_played = []
        self.played_total = 0

    # Checks if a go has been called.
    def check_go(self):
        return self.go

    # Resets the go boolean
    def toggle_go(self):
        self.go = not(self.go)

    def score_hand(self, player_index):
        hand_score = cs.score_hand(self.players[player_index].get_hand(), self.cut_card, False)
        crib_score = 0
        if player_index == self.crib_index:
            crib_score = cs.score_hand(self.crib, self.cut_card, True)
        return hand_score + crib_score

    def get_score(self):
        return self.score

    def check_thirty_one(self):
        if self.played_total == 31:
            print("in check thirty one")
            self.reset_cards_played()
