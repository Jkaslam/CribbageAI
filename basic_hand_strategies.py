import itertools
import random
import cribbage_hand_scorer as chs

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = ['s', 'c', 'h', 'd']

deck = list(itertools.product(vals, suits))

# Chooses which four cards to keep based on the maximum
# expected value of the hand given that the 5th card has
# not been flipped
def maximum_expected_value_hand(hand):
    left_over_cards = deck.copy()
    for card in hand:
        left_over_cards.remove(card)
    all_combinations = list(itertools.combinations(hand, 4))
    expected_values = list()
    for four_card_hand in all_combinations:
        expected_value = 0
        for card in left_over_cards:
            expected_value += chs.score_hand(list(four_card_hand), card, False)
        expected_value /= 46
        expected_values.append(expected_value)

    return all_combinations[expected_values.index(max(expected_values))]

test_hand = [(5, 's'), (5, 'c'), (5, 'h'), (5, 'd'), (2, 's'), (3, 's')]

print(maximum_expected_value_hand(test_hand))
                
            
                
                
            
    
