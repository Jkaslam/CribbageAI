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
        curr_player = players[i]
        print("It's player ", i, "s turn.", sep = "")
        hand = ""
        for card in curr_player.get_hand():
            hand += str(card[0]) + card[1] + " "
        print("Your hand is", hand)
        card1, card2 = input("Please choose 2 cards to discard to the crib.").split()
        card1 = (int(card1[0]), card1[1])
        card2 = (int(card2[0]), card2[1])

        game.discard_to_crib([card1, card2])
        hand = ""
        for card in player1.get_hand():
            hand += str(card[0]) + card[1] + " "
        print("Your hand is", hand)

    # Cut the deck, choose the cut card and check for nibs.
    print("The cut card is", game.get_cut_card()) 
    game.check_nibs()
    winner = game.check_win()

    if winner != -1:
        break

    # Gameplay
    while len(game.can_play(0)) != 0 or len(game.can_play(1)) != 0:
        print("The cards played are", game.get_cards_played(), "and their total sum is", game.comp_played_total())
        message = "Choose a card to play from" + str(game.can_play())
        card = input(message)
        card = (int(card[0]), card[1])
        game.update_cards_played(players[game.get_turn_index()].play(card))
        
        game.score()
