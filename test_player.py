import player

player = player.Player()

def test_play():
    hand = [(1, 's'), (1, 'd'), (1, 'c')]
    player.set_hand(hand)
    hand_test = player.get_hand()
    for i in range(len(hand_test)):
        assert hand_test[i] == hand[i]

def test_discard():
    hand = [(1, 's'), (1, 'd'), (1, 'c')]
    player.set_hand(hand)
    print(player.get_hand())
    player.discard([(1, 's')])
    print(player.get_hand())
    
if __name__ == "__main__":
    test_play()
    test_discard()
    print("Everything passed")
