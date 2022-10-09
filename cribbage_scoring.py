import itertools
import numpy as np
import math

########################### Functions for scoring hands ####################

# Counts the number of distinct pairs in a hand
def count_pairs(hand):
    total_pairs = 0
    for i in range(len(hand)):
        for j in range(i+1, len(hand)):
            if hand[i][0] == hand[j][0]:
                total_pairs += 1
    return total_pairs

# Counts all combinations of cards that add to 15
def count_fifteens(hand):
    total_fifteens = 0
    for i in range(1, 6):
        combinations = list(itertools.combinations(set(hand), i))
        for j in range(len(combinations)):
            currSum = 0
            for val, suit in combinations[j]:
                currSum += min(10, val)
            if currSum == 15:
                total_fifteens += 1
    return total_fifteens

# Counts the total number of maximal runs and says how long they are
def count_runs(hand):
    # The total number of runs of length 3, 4 or 5
    total_runs = 0
    run_length = 0
    for i in range(5, 2, -1):
        # We don't want to search for short runs if we've already
        # found longer ones
        if run_length != 0:
            break
        combinations = list(itertools.combinations(hand, i))
        num_runs = 0
        for j in range(len(combinations)):
            values = list()
            #print("The current combination is", combinations[j])
            for val, suit in combinations[j]:
                values.append(val)
            differences = list(np.absolute(np.diff(values)))
            #print("The differences are", differences)
            if (len(set(differences)) == 1 and differences[0] == 1):
                run_length = i
                total_runs += 1
    return [total_runs, run_length]

# Checks if the player has a jack in their hand which matches
# the suit of the cut card
def right_jack(hand, cut_card):
    for val, suit in hand:
        if val == 11 and suit == cut_card[1]:
            return True
    return False

# Checks if the player has a flush, returns the points they score from it 
def flush(hand, cut_card, crib):
    suits = list()
    for val, suit in hand:
        suits.append(suit)
    if len(set(suits)) == 1 and suits[0] == cut_card[1]:
        return 5
    if len(set(suits)) == 1 and not crib:
        return 4
    return 0
    
# Returns the total score of a cribbage hand
def score_hand(hand, cut_card, crib):
    total_score = 0

    # Right jack is worth 1
    if right_jack(hand, cut_card):
        total_score += 1

    # Flush calculates its score
    total_score += flush(hand, cut_card, crib)

    # Combine hand with cut card since for the rest of the counting
    # it doesn't matter
    hand.append(cut_card)

    #Sort the hand because that's required to count runs properly
    hand.sort(key=lambda card: card[0])
    
    # Each pair is worth 2
    total_score += 2 * count_pairs(hand)

    # Each 15 is worth 2
    total_score += 2 * count_fifteens(hand)

    # Each distinct run is worth its length
    total_runs = count_runs(hand)[0]
    run_length = count_runs(hand)[1]
    total_score += total_runs * run_length

    return total_score

 ########################## Functions for pegging #############################

# Returns 2 if the sum of cards played is 15 or 31.
def fift_or_thirty1(cards):
    total = 0
    for card in cards:
        total += card[0]
    if (total == 15 or total == 31):
        return 2
    return 0

# Returns the score from the longest run (of length 3 or greater)
# including the last card played.            
def peg_runs(cards):
    if len(cards) == 2:
        return 0
    sorted_cards = sorted(cards, key=lambda card: card[0])
    adj_vals = []
    for i in range(len(cards) - 1):
        adj_vals += [sorted_cards[i+1][0] - sorted_cards[i][0]]
    if (len(set(adj_vals)) == 1) and adj_vals[0] == 1:
        return len(cards)
    else:
        return peg_runs(cards[1:])

# Recursive helper function for the peg_pairs function. 
def peg_pairs_helper(cards, num_pairs):
    if num_pairs == 4:
        return 12
    top_val = cards[-1][0]
    cards = cards[:-1]
    if len(cards) > 0 and cards[-1][0] == top_val:
        return peg_pairs_helper(cards, num_pairs + 1)
    if num_pairs == 0:
        return 0
    else:
        return math.factorial(num_pairs + 1)/math.factorial(num_pairs-1) 
        
    
# Returns the score from pairs that the most recently placed card creates. 
def peg_pairs(cards):
    return peg_pairs_helper(cards, 0)
        
        




     
                
            
    
