from player import Player
import itertools
import random
import cribbage_scoring as cs
import pickle

class QTableAgent(Player):
    def __init__(self):
        super().__init__()
        
        # Dictionary with a state-action tuple as key (state, action). 
        #  A state is a tuple of length 11.
        # The first 7 elements are the values of the cards played.
        # The last 4 elements are the playable cards in a player's hand,
        # sorted by value.
        # An action is a value from 0 - 3 representing the card played.   
        q_table = {}
        
        # Training hyperparameters
        learning_rate = 0.7
        discount_rate = .95
        max_epsilon = 1.0
        min_epsilon = 0.05
        # Negative since it's a decay rate
        decay_rate = -0.0005
    
    # Finds the currently highest rated state-action pair if any. Otherwise it returns a random playable
    # action.
    def find_best_action(state, num_action_options):
        q_vals = [self.q_table.get(tuple(list(state).append(x)), 0) for x in range(num_action_options)]
        max_q_val = max(q_vals)
        if max_q_val == 0:
            return random.choice(list(range(num_action_options)))
        else:
            return q_vals.index(max_q_val)
                   
    # Epsilon percent of the time exploit the current best estimated action and
    # 1 - epsilon percent of the time explore new actions if possible. 
    def e_greedy_policy(self, state, epsilon):
        num_non_zero = sum(x > 0 for x in state[7:])
        if (num_non_zero == 1):
            return 0
        rand_num = random.uniform(0, 1)

        if rand_num > epsilon:
            action = find_best_action(state, num_non_zero)
        else:
            num_non_zero = sum(x > 0 for x in state[7:])
            action =  random.choice(list(range(num_non_zero)))
        return action
    
    # Choose's the agent's action in the training phase. 
    def train_action(self, state, episode_num):
        epsilon = min_epsilon + (max_epsilon - min_epsilon) * math.exp(self.decay_rate * episode_num)
        action = e_greedy_policy(self, state, epsilon)
    
    # Updates the Q-table after a training step.
    def train_update(self, old_state, action, new_state, reward):
        q_val_cur = self.q_table.get(tuple(list(old_state).append(action)), 0)
        q_vals_new = [self.q_table.get(tuple(list(new_state).append(x)), 0) for x in range(4)]
        max_q_val_new = max(q_vals_new)
        self.q_table[tuple(list(old_state).append(action))] = q_val_cur + self.learning_rate * (reward + self.discount_factor * max_q_val_new - q_val_cur) 
    
    # Plays a card for the QAgent during training.
    def train_play(self, playable_cards, action):
        
        
        
        
    # Plays a legally playable card at random.
    def play(self, state):
        playable_cards = state[3]
        #print("playable cards", playable_cards)
        rand_card = random.sample(playable_cards, 1)[0]
        #print("I'm playing", rand_card)
        self.hand.remove(rand_card)
        return rand_card

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
        with open("saved/agents/q_table.pkl", "wb") as f:
            self.q_table = pickle.load(f) 

 
