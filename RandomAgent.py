import player
import itertools
import random
import cribbage_scoring as cs

class GreedyAgent(Player):
    def __init__(self):
        super().__init__(number)
    #  Plays a legally playable card at random.
    def play(self, state):
        playable_cards = state[1]
        rand_card = random.sample(playable_cards, 1)
        self.hand.remove(rand_card)
        return rand_card

    def discard(self, state):
        rand_cards = random.sample(self.hand, 2)
        for card in rand_cards:
            self.hand.remove(card)
        return rand_cards
