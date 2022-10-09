class Player():
    def __init__(self):
        self.hand = []

    def play(card):
        if card in hand:
            hand.remove(card)
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
        if len(self.hand) == 0:
            self.hand = new_hand
