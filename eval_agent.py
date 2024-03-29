import player
import RandomAgent
import QTableAgent
import Game
import re

# Player 1 is the type of agent you want to train.
player1 = QTableAgent.QTableAgent()
player1.load_q_table()

# Player 2 is the type of agent you want to train against. 
player2 = RandomAgent.RandomAgent()

# The number of games you want to train your agent with. 
num_episodes = 10000

# List of the indices of the winning player for each game and the spread.
game_history = []
differential_history = []


players = [player1, player2]

for episode in range(num_episodes):
    if (episode % 1000) == 0:
        print("In episode", episode)
    game = Game.Game(players)
    
    while game.check_win() == -1:
        #print("Dealing.")
        game.deal()

        # Discard to the crib
        for i in range(len(players)):
            curr_player = game.get_players()[i]
            #print("It's player ", i, "s turn.", sep = "")
            hand = ""
            for card in curr_player.get_hand():
                hand += str(card[0]) + card[1] + " "
            #print("Your hand is", hand)

            game.discard_to_crib()
            hand = ""
            for card in curr_player.get_hand():
                hand += str(card[0]) + card[1] + " "
            #print("You discarded and your hand is now", hand)

        # Cut the deck, choose the cut card and check for nibs.
        #print("The cut card is", game.get_cut_card())


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
                winner = game.check_win()
                if winner != -1:
                    break
                
                curr_player = players[game.get_turn_index()]
                #print("It's player", game.get_turn_index(), "turn")
                #print("Player 0's hand is:", players[0].get_hand())
                #print("Player 1's hand is:", players[1].get_hand())
                #print("The current score is:", game.get_score())
                #print("The cards played are", game.get_cards_played(), "and their total sum is", game.get_played_total())
                
                # The current player can play
                if (len(game.can_play(game.get_turn_index())) > 0):
                    card = curr_player.play(game.get_state(game.get_turn_index()))
            
                    #print(card)
                    game.update_cards_played(card)
                    game.update_score()
                    
                    # Enter here if the last card played makes the score 31. 
                    game.check_thirty_one()
                        #print("We got a 31.")
                    winner = game.check_win()
                    if winner != -1:
                        break 
                
                # The current player cannot play
                elif not(game.check_go()):
                    game.toggle_go()
                    game.score_go()
                    winner = game.check_win()
                    if winner != -1:
                        break
                game.next_turn()
                    
            
            #print("Resetting cards")
            game.reset_cards_played()
            game.reset_go() 
        
        # Scores the players' hands after a round of cribbage. 
        for i in range(len(game.get_players())):
            # Disabled scoring the hand since we're only interest in training game play.
            #game.score_hand(i)
            winner = game.check_win()
            if winner != -1:
                break
        game.update_crib_index()
        #print("End of hand")
    #print("The winner is player", winner, "with a score of", game.get_score())
    game_history.append(winner)
    differential_history.append(abs(game.get_score()[0] - game.get_score()[1]))
print("The Q-table agent won", game_history.count(0), "out of", num_episodes)
print(sum(differential_history)/len(differential_history))
