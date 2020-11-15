# abs358@drexel.edu

from connect3 import State, Action
from game import Player

class HumanPlayer(Player):
    def choose_action(self, state: State = None) -> Action:
        if state:
            print("Choose your action")
            actions = state.actions(self.character)
            for a in enumerate(actions):
                print(str(a[0]) + ":", a[1])
            choice = input("Please choose an action (0-"+str(len(actions)-1)+"): ")
            while choice == "" or not (0 <= int(choice) < len(actions)):
                choice = input("Please choose an action (0-"+str(len(actions)-1)+"): ")
            choice = int(choice)
            return actions[choice]

