import player 
import Game
import re

player1 = player.Player()
player2 = player.Player()

players = [player1, player2]

game = Game.Game(players)

while game.check_win() == -1:
    print("Dealing.")
    game.deal()

    # Discard to the crib
    for i in range(len(players)):
        curr_player = game.get_players()[i]
        print("It's player ", i, "s turn.", sep = "")
        hand = ""
        for card in curr_player.get_hand():
            hand += str(card[0]) + card[1] + " "
        print("Your hand is", hand)
        card1, card2 = input("Please choose 2 cards to discard to the crib.").split()
        card1 = (int(re.findall("\d+", card1)[0]), re.findall("\D+", card1)[0])
        card2 = (int(re.findall("\d+", card2)[0]), re.findall("\D+", card2)[0])

        game.discard_to_crib([card1, card2])
        hand = ""
        for card in curr_player.get_hand():
            hand += str(card[0]) + card[1] + " "
        print("Your hand is", hand)

    # Cut the deck, choose the cut card and check for nibs.
    print("The cut card is", game.get_cut_card())

    
    game.check_nibs()
    winner = game.check_win()

    if winner != -1:
        break

    game.set_initial_turn_index()
    
    # Continue while at least one of the players has cards left in their hand. 
    while sum(map(lambda x: len(x.get_hand()), game.get_players())) > 0:
        if winner != -1:
            break

        # Gameplay for a single turn as long as at least one player still has cards to play. 
        while len(game.can_play(0)) + len(game.can_play(1)) != 0:
            print("It's player", game.get_turn_index(), "turn")
            print("The cards played are", game.get_cards_played(), "and their total sum is", game.get_played_total())
            message = "Choose a card to play from" + str(game.can_play(game.get_turn_index()))
            card = input(message)
            card = (int(re.findall("\d+", card)[0]), re.findall("\D+", card)[0])
            print(card)
            game.update_cards_played(players[game.get_turn_index()].play(card))
            game.update_score()
            game.check_thirty_one()
            print("The current score is: ", game.get_score())
                
            winner = game.check_win()

            if winner != -1:
                break
            if not(game.check_go()):
               game.next_turn()
               
            if (len(game.can_play(game.get_turn_index())) == 0 and not(game.check_go())):
                print("Go!")
                game.call_go()

        if game.check_go():
            game.toggle_go()
            if game.get_played_total() != 31:
                game.score_go()
            game.next_turn()
            
        print("Resetting cards")
        game.reset_cards_played()
        
    # Scores the players' hands after a round of cribbage. 
    for i in range(len(game.get_players())):
        game.score_hand(i)
        winner = game.check_win()
        if winner != -1:
            break
    game.update_crib_index()
    print("End of hand")
print("The winner is player", winner, "with a score of", game.get_score())
