import cribbage_hand_scorer as chs
import itertools
import matplotlib
from matplotlib import pyplot as plt
from collections import Counter

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = ['s', 'c', 'h', 'd']

deck = list(itertools.product(vals, suits))

# All possible 5 card hands, has size 52 choose 5
all_combinations = list(itertools.combinations(deck, 5))

all_scores = list()
# Need to distinguish which card is in the crib
for i in range(len(all_combinations)):
    if i % 10000 == 0:
        print(i)
    curr_combo = all_combinations[i]
    for j in range(5):
        curr_hand = [card for index, card in enumerate(curr_combo) if index != j]
        cut_card = curr_combo[j]
        curr_hand_score = chs.score_hand(curr_hand, cut_card, False)
        all_scores.append(curr_hand_score)

print(Counter(all_scores))

plt.hist(all_scores, bins=29)
plt.xlabel("Scores")
plt.ylabel("Number of hands with given score")
plt.title("Cribbage hand score distribution")
plt.show()
