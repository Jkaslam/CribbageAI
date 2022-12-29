from player import Player
import itertools
import random
import cribbage_scoring as cs

class MonteAgent(Player):
    def __init__(self):
        super().__init__()
    
    # Plays a legally playable card at random.
    def play(self, state):
        playable_cards = state[3]
        #print("playable cards", playable_cards)
        rand_card = random.sample(playable_cards, 1)[0]
        #print("I'm playing", rand_card)
        self.hand.remove(rand_card)
        return rand_card

    # Randomly discards two cards to the crib.
    def discard(self, state):
        rand_cards = random.sample(self.hand, 2)
        #print("I'm discarding", rand_cards)
        for card in rand_cards:
            self.hand.remove(card)
        return rand_cards
