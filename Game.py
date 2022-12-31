import player
import RandomAgent
import itertools
import random
import cribbage_scoring as cs

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = ['s', 'c', 'h', 'd']

# The model for a cribbage game between two players. 
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
        #print(random_cards)
        for i in range(len(self.players)):
            #print("testing deal", random_cards[6*i:6*i + 6])
            self.players[i].set_hand(random_cards[6*i:6*i + 6])
            #print(self.players[i].get_hand())
        self.cut_card = random_cards[-1]

    # Counts pegging based on the most recently played card. 
    def update_score(self):
        self.score[self.turn_index] += cs.peg(self.cards_played)

    # Discards two cards from the current player's hand to the crib.
    # Also saves the 4 chosen cards to the player's final hand for
    # scoring.
    def discard_to_crib(self):
        curr_player = self.players[self.turn_index]
        self.crib += curr_player.discard(self.get_state(self.turn_index))
        curr_player.set_hand_for_scoring(curr_player.get_hand())
        self.turn_index = (self.turn_index + 1) % len(self.players)
                                        
    # Checks to see if any player has won and if they have, returns their index. 
    def check_win(self):
        for i in range(len(self.players)):
            if self.score[i] > 120:
                return i
        return -1 

    # Computes the total of the current played cards.
    def get_played_total(self):
        return self.played_total
    
    # Returns a list of cards the given player can play.
    def can_play(self, player_idx):
        playable_cards = list(filter(lambda x: min(x[0], 10) + self.played_total <= 31, self.players[player_idx].get_hand()))
        playable_cards.sort(key = lambda x: x[0])
        #print("Current hand", self.players[player_idx].get_hand())
        #print("Total played", self.played_total)
        #print("Playable cards", playable_cards)
        return playable_cards

    # Returns the cut card for the current hand.
    def get_cut_card(self):
        return self.cut_card
    
    # Checks to see if the cut card is a jack. 
    def check_nibs(self):
        if (self.cut_card[0] == 11):
            self.score[self.crib_index] += 2

    # Returns the current list of cards that have been played this hand.
    def get_cards_played(self):
        return self.cards_played

    # Adds a recently played card to the pile of cards that have been played. 
    def update_cards_played(self, card):
        self.cards_played += [card]
        self.played_total += min(card[0], 10)

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
        self.toggle_go()

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

    # Scores the hand of the given player as well as the crib if it's theirs.
    def score_hand(self, player_index):
        hand_score = cs.score_hand(self.players[player_index].get_hand_for_scoring(), self.cut_card, False)
        crib_score = 0
        if player_index == self.crib_index:
            crib_score = cs.score_hand(self.crib, self.cut_card, True)
        return hand_score + crib_score

    # Returns the current score of the game
    def get_score(self):
        return self.score

    # Resets the hand played if the total is 31 
    def check_thirty_one(self):
        if self.played_total == 31:
            #print("in check thirty one")
            self.reset_cards_played()
            return True
        return False

    # Gives the current crib to the next player. 
    def update_crib_index(self):
        self.crib_index = (self.crib_index + 1) % len(self.players)

    # Adds 1 to the current player's score if the other player called go
    # and the current player can't make 31. 
    def score_go(self):
        self.score[(self.turn_index + 1) % len(self.players)] += 1

    # Resets the go called boolean to 0.
    def reset_go(self):
        self.go = False

    # Sets the starting turn index. 
    def set_initial_turn_index(self):
        self.turn_index = (self.crib_index + 1) % len(self.players)

    # Returns the game's current state for playing (includes names of cards).
    def get_state(self, turn_idx):
        return [self.cut_card, self.cards_played, self.played_total, self.can_play(turn_idx)]

    # Returns the game's current state for training.
    def get_train_state(self, turn_idx):
        zeroes = [0] * (7 - len(self.cards_played))
        played = [x[0] for x in self.cards_played]
        played = played + zeroes
        hand = [x[0] for x in self.can_play(turn_idx)]
        hand = hand + ([0] * (4 - len(hand)))
        state = tuple(played + hand + [self.cut_card[0]])
        return state
        
    # Returns the (signed) score differential from the point of view of the given player.
    def get_score_diff(self, turn_idx):
        return self.get_score()[turn_idx] - self.get_score()[(turn_idx + 1) % len(self.players)]    
        

