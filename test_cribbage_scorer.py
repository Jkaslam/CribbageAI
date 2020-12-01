import itertools
import random
import cribbage_hand_scorer as chs

vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = ['s', 'c', 'h', 'd']

deck = list(itertools.product(vals, suits))

def test_count_pairs():
    hand1 = [(1, 's'), (1, 'd'), (1, 'c'), (2, 's'), (2, 'd')]
    assert chs.count_pairs(hand1) == 4, "Should be 4"

    hand2 = [(1, 's'), (1, 'd'), (3, 'c'), (4, 'c'), (5, 'c')]
    assert chs.count_pairs(hand2) == 1, "Should be 1"

    hand3 = [(1, 's'), (1, 'd'), (1, 'c'), (1, 'h'), (2, 'd')]
    assert chs.count_pairs(hand3) == 6, "Should be 6"

    hand4 = [(8, 's'), (8, 'd'), (8, 'c'), (2, 's'), (3, 'd')]
    assert chs.count_pairs(hand4) == 3, "Should be 3"

    hand5 = [(1, 's'), (2, 'd'), (3, 'c'), (4, 's'), (5, 'd')]
    assert chs.count_pairs(hand5) == 0, "Should be 0"

    hand6 = [(8, 's'), (8, 'd'), (8, 'c'), (2, 's'), (3, 'd')]
    random.shuffle(hand6)
    assert chs.count_pairs(hand6) == 3, "Should be 3"

def test_count_fifteens():
    hand1 = [(6, 'c'), (10, 'd'), (5, 'h'), (4, 's'), (5, 'd')]
    assert chs.count_fifteens(hand1) == 4, "Should be 4"

    hand2 = [(11, 'h'), (5, 'd'), (5, 'c'), (5, 's'), (5, 'h')]
    assert chs.count_fifteens(hand2) == 8, "Should be 8"

    hand3 = [(3, 'h'), (3, 's'), (4, 's'), (4, 'd'), (1, 'c')]
    assert chs.count_fifteens(hand3) == 1, "Should be 1"
    
if __name__ == "__main__":
    test_count_pairs()
    test_count_fifteens()
    print("Everything passed")


                
            
                
                
            
    
