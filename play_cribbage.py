import player 
import Game

player1 = player.Player()
player2 = player.Player()

players = [player1, player2]

game = Game.Game(players)

while game.check_win() == -1:
    game.deal()

    # Discard to the crib
    for i in range(len(players)):
        print("It's player ", i, "s turn.", sep = "")
        hand = ""
        for card in player1.get_hand():
            hand += str(card[0]) + card[1] + " "
        print("Your hand is", hand)
        card1, card2 = input("Please choose 2 cards to discard to the crib.").split()
        card1 = (int(card1[0]), card1[1])
        card2 = (int(card2[0]), card2[1])

        game.discard_to_crib([card1, card2])
        for card in player1.get_hand():
            hand += str(card[0]) + card[1] + " "
        print("Your hand is", hand)
    
