# abs358@drexel.edu

from connect3 import State, util
from abc import ABCMeta, abstractmethod

class Player:
    def __init__(self, character: str = ""):
        self.character = character
    def __str__(self):
        return "Player(" + str(type(self)) + ", char=" + self.character + ")"
    # TODO add choose_action()

class Game:
    def __init__(self, state: State = State(), p1: Player = None, p2: Player = None):
        self.state = state
        self.p1 = p1
        self.p2 = p2
    
    def play(self) -> tuple:
        if (self.p1 == None or self.p2 == None):
            return tuple()
        active_player = self.p2 # toggled at each loop
        history = [self.state]
        while not(self.state.game_over()):
            # Initialize or toggle the active player
            active_player = self.p1 if (not active_player or active_player == self.p2) else self.p2
            # Display board
            util.pprint(self.state)
            # Get active player's action
            action = active_player.choose_action(self.state)
            # Update game
            self.state = self.state.clone().execute(action)
            history.append(self.state)
        util.pprint(self.state)
        return [self.state.winner()] + history

        


    