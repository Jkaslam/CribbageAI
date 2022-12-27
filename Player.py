from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self):
        self.hand = []
        self.hand_for_scoring = []

    # Plays the given card if it's in the player's hand.
    @abstractmethod
    def play(self, state):
        pass

    # Discards the given cards. 
    def discard(self, cards):
        discarded_cards = []
        for card in cards:
            if card in self.hand:
                self.hand.remove(card)
                discarded_cards += [card]
        return discarded_cards

    # Returns the player's current hand. 
    def get_hand(self):
        return self.hand

    # Sets a players hand for updating a hand after cards are played or discarded. 
    def set_hand(self, new_hand):
        self.hand = new_hand

    # Sets the player's original full hand before any cards
    # are played or discarded. 
    def set_hand_for_scoring(self, new_hand):
        self.hand_for_scoring = new_hand

    # Returns all the cards the player originally had in their hand during
    # a turn. 
    def get_hand_for_scoring(self):
        return self.hand_for_scoring
