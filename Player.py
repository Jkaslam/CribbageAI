class Player():
    def __init__(self):
        self.hand = []
        self.hand_for_scoring = []

    def play(self, card):
        if card in self.hand:
            self.hand.remove(card)
            return card
        
    def discard(self, cards):
        discarded_cards = []
        for card in cards:
            if card in self.hand:
                self.hand.remove(card)
                discarded_cards += [card]
        return discarded_cards

    def get_hand(self):
        return self.hand

    def set_hand(self, new_hand):
            self.hand = new_hand

    def set_hand_for_scoring(self, new_hand):
        self.hand_for_scoring = new_hand

    def get_hand_for_scoring(self):
        return self.hand_for_scoring
