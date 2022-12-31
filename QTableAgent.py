from player import Player
import itertools
import random
import cribbage_scoring as cs
import pickle
import math

class QTableAgent(Player):
    def __init__(self):
        super().__init__()
        
        # Dictionary with a state-action tuple as key (state, action). 
        #  A state is a tuple of length 12.
        # The first 7 elements are the values of the cards played.
        # The next 4 elements are the playable cards in a player's hand,
        # sorted by value. The last is the current cut card.
        # An action is a value from 0 - 3 representing the card played.   
        self.q_table = {}
        
        # Training hyperparameters
        self.learning_rate = 0.7
        self.discount_factor = .95
        self.max_epsilon = 1.0
        self.min_epsilon = 0.05
        # Negative since it's a decay rate
        self.decay_rate = -0.0005
    
    # Finds the currently highest rated state-action pair if any. Otherwise it returns a random playable
    # action.
    def find_best_action(self, state, num_action_options):
        q_vals = [self.q_table.get(tuple(list(state)+[x]), 0) for x in range(num_action_options)]
        max_q_val = max(q_vals)
        if max_q_val == 0:
            return random.choice(list(range(num_action_options)))
        else:
            return q_vals.index(max_q_val)
                   
    # Epsilon percent of the time exploit the current best estimated action and
    # 1 - epsilon percent of the time explore new actions if possible. 
    def e_greedy_policy(self, state, epsilon):
        num_non_zero = sum(x > 0 for x in state[7:11])
        if (num_non_zero == 1):
            return 0
        rand_num = random.uniform(0, 1)

        if rand_num > epsilon:
            action = self.find_best_action(state, num_non_zero)
        else:
            num_non_zero = sum(x > 0 for x in state[7:11])
            action =  random.choice(list(range(num_non_zero)))
        return action
    
    # Choose's the agent's action in the training phase. 
    def train_action(self, state, episode_num):
        epsilon = self.min_epsilon + (self.max_epsilon - self.min_epsilon) * math.exp(self.decay_rate * episode_num)
        action = self.e_greedy_policy(state, epsilon)
        return action

    # Updates the Q-table after a training step.
    def train_update(self, old_state, action, new_state, reward):
        #print("old_state", old_state)
        old_state_action_pair = tuple(list(old_state) + [action])
        q_val_cur = self.q_table.get(old_state_action_pair, 0)
        q_vals_new = [self.q_table.get(tuple(list(new_state)+ [x]), 0) for x in range(4)]
        max_q_val_new = max(q_vals_new)
        
        self.q_table[old_state_action_pair] = q_val_cur + self.learning_rate * (reward + self.discount_factor * max_q_val_new - q_val_cur) 
    
    # Plays a card for the QAgent during training.
    def train_play(self, playable_cards, action):
        card = playable_cards[action]
        self.hand.remove(card)
        return card      
        
        
        
    # Plays a legally playable card according to the Q-table. 
    def play(self, state):
        playable_cards = state[3]
        num_pos_actions = len(playable_cards)

        # If there is a choice of actions, choose the best.
        if num_pos_actions > 1:
            cut_card = state[0]
            cards_played = state[1]
            zeroes = [0] * (7 - len(cards_played))
            played = [x[0] for x in cards_played]
            played = played + zeroes
            hand = [x[0] for x in playable_cards]
            hand = hand + ([0] * (4 - len(hand)))
            state = tuple(played + hand + [cut_card[0]]) 
            action = self.find_best_action(state, num_pos_actions)
        else:
            action = 0
         
        card = playable_cards[action]
        self.hand.remove(card) 
        return card

    # Randomly discards two cards to the crib.
    def discard(self, state):
        rand_cards = random.sample(self.hand, 2)
        #print("I'm discarding", rand_cards)
        for card in rand_cards:
            self.hand.remove(card)
        return rand_cards
    
    # Returns the q_table, for use after training the agent.
    def get_q_table(self):
        return self.q_table

    # Saves the q_table to a file.
    def save_q_table(self):
        with open("saved_agents/q_table.pkl", "wb") as f:
            pickle.dump(self.q_table, f)
    
   # Loads the q_table from a file.
    def load_q_table(self):
        with open("saved_agents/q_table.pkl", "rb") as f:
            self.q_table = pickle.load(f) 

 
