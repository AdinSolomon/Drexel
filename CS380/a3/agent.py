# abs358@drexel.edu

from connect3 import State, Action
from game import Player

import random

class RandomPlayer(Player):
    def choose_action(self, state: State = None) -> Action:
        return random.choice(state.actions(self.character))

def heuristic(state: State = None, playerchar: str = None): # -> a number boi
    if state.game_over():
        if state.winner() == playerchar:
            return float("inf")
        elif state.winner() != None: # Opponent wins
            return -1 * float("inf")
        else:
            return 0
    score = 0
    # number of player's pieces adjacent to open spaces
    # - number of opponent's pieces adjacent to open spaces
    for col in range(4):
        for row in range(3):
            if (piece := state.get(col, row)) and piece == " ":
                deltas = [-1, 0, +1]
                for dx in deltas:
                    for dy in deltas:
                        if None == (adjacent_piece := state.get(col+dx, row+dy)):
                            continue
                        if adjacent_piece == playerchar: # player's piece
                            score += 1
                        elif adjacent_piece != " ": # opponent's piece
                            score -= 1
                        else: # empty
                            score += 0
    return score

MINIMAX_LOOKAHEAD = 8

class MinimaxPlayer(Player):
    def choose_action(self, state: State = None) -> Action:
        struct = self.minimax(state)
        action = struct[0]
        #print("Chosen action =", action)
        if struct[1] == -1 * float("inf"):
            #print("CONCESSION")
            return random.choice(state.actions(self.character))
        return action

    def minimax(self, state: State, depth = MINIMAX_LOOKAHEAD, func = heuristic):
        def _max():
            return ((MINIMAX_LOOKAHEAD - depth) % 2) == 0
        #tabs = "    "*(MINIMAX_LOOKAHEAD - depth)
        
        state = state.clone() # Don't modify the game state!
        if depth == 0:
            score = heuristic(state=state, playerchar=self.character)
            try:
                action = random.choice(state.actions(self.character))
            except:
                action = None
            #print(tabs+"score =", score)
        else:
            if _max():
                #print(tabs+"Looking for MAX")
                score = -1 * float("inf")
                action = None
                for a in state.actions(self.character):
                    #print(tabs+"- considering action", a)
                    nextState = state.clone().execute(a)
                    s = self.minimax(nextState, depth=depth-1)[1]
                    if s > score:
                        action = a
                        score = s
                #print(tabs+"MAX score =", score)
            else: # _min()
                #print(tabs+"Looking for MIN")
                score = float("inf")
                action = None
                opponent_character = "O" if self.character == "X" else "X"
                for a in state.actions(opponent_character):
                    #print(tabs+"- considering action", a)
                    nextState = state.clone().execute(a)
                    s = self.minimax(nextState, depth=depth-1)[1]
                    if s < score:
                        action = a
                        score = s
                #print(tabs+"MIN score =", score)
        score = score - depth
        return (action, score)

                
            



    
    


        
        
