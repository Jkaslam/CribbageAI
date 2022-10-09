class Player():
    def __init__(self):
        self.hand = []

    def play(card):
        if card in hand:
            hand.remove(card)
            return card
        
    def discard(cards):
        discarded_cards = []
        for card in cards:
            if card in hand:
                hand.remove(card)
                discarded_cards += [card]
        return discarded_cards

    def get_hand():
        return self.hand

    def set_hand(new_hand):
        if len(self.hand) == 0:
            self.hand = new_hand
