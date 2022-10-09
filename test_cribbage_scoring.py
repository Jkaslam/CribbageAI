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

    
if __name__ == "__main__":
    test_peg_pairs()
    test_peg_runs()
    print("Everything passed")


                
            
                
                
            
    
