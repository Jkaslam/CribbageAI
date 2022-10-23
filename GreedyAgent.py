# Discard
# Calculate whichever 4 cards have the highest expected value.
# Discard the other two.

import player
import itertools
import random
import cribbage_scoring as cs

class GreedyAgent(Player):
    
     def __init__(self):
        super().__init__(number)

     #  Play the card that would give the maximum immediate score.
     def play(self, state):
         playable_cards = state[1]
         
         max_card = playable_cards[0]
         max_score = 0
         for card in playable_cards:
             # state[0] = current cards
             curr_score = cs.peg(state[0] + [card])
             if curr_score > max_score:
                 max_card = card
                 max_score = curr_score
         self.hand.remove(max_card)
         return max_card

    def discard(self, state):
        
        
