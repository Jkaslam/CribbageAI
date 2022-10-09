import itertools
import random
import cribbage_scoring as cs


vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
suits = ['s', 'c', 'h', 'd']

deck = list(itertools.product(vals, suits))

def test_peg_pairs():
    hand = [(1, 's'), (1, 'd'), (1, 'c')]
    assert cs.peg_pairs(hand) == 6, "Should be 6"

    hand = [(1, 's'), (1, 'd'), (3, 'c')]
    assert cs.peg_pairs(hand) == 0, "Should be 0"

    hand = [(1, 'c'), (3, 'd')]
    assert cs.peg_pairs(hand) == 0, "Should be 0"

    hand = [(1, 'd'), (1, 'c')]
    assert cs.peg_pairs(hand) == 2, "Should be 2"

    hand = [(1, 'c'), (3, 'd'), (1, 'd'), (1, 'c')]
    assert cs.peg_pairs(hand) == 2, "Should be 2"
    
def test_peg_runs():
    hand = [(3, 's'), (2, 'd'), (1, 'c')]
    assert cs.peg_runs(hand) == 3, "Should be 3"

    hand = [(1, 's'), (2, 'd'), (3, 'c')]
    assert cs.peg_runs(hand) == 3, "Should be 3"
    
    hand = [(1, 's'), (2, 's'), (2, 'd'), (3, 'c')]
    assert cs.peg_runs(hand) == 0, "Should be 0"

    hand = [(1, 's'), (1, 's'), (2, 'd'), (3, 'c')]
    assert cs.peg_runs(hand) == 3, "Should be 03"

    hand = [(2, 's'), (1, 'd'), (3, 'c')]
    assert cs.peg_runs(hand) == 3, "Should be 3"

def test_fift_or_thirty1():
    hand = [(10, 's'), (5, 'd')]
    assert cs.fift_or_thirty1(hand) == 2, "Should be 2"

    hand = [(11, 's'), (5, 'd')]
    assert cs.fift_or_thirty1(hand) == 2, "Should be 2"

    hand = [(11, 's'), (3, 'd'), (2, 'd')]
    assert cs.fift_or_thirty1(hand) == 2, "Should be 2"

    hand = [(10, 's'), (11, 'd'), (13, 'd'), (1, 'd')]
    assert cs.fift_or_thirty1(hand) == 2, "Should be 2"

if __name__ == "__main__":
    test_peg_pairs()
    test_peg_runs()
    test_fift_or_thirty1()
    print("Everything passed")


                
            
                
                
            
    
