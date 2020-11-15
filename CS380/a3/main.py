# abs358@drexel.edu

from connect3 import State, util
from game import Game
from human import HumanPlayer
from agent import RandomPlayer, MinimaxPlayer

def make_player(p: str = "", c: str = ""):
    if p[0] == "h":
        return HumanPlayer(c)
    if p[0] == "r":
        return RandomPlayer(c)
    if p[0] == "m":
        return MinimaxPlayer(c)
    print("Please enter a valid player string: [human, random, minimax]")
    exit()

p1 = util.get_arg(1)
p2 = util.get_arg(2)
print(p1, "vs.", p2)
if p1 and p2:
    p1 = make_player(p1, 'X')
    p2 = make_player(p2, 'O')
    print(p1, "vs.", p2)
    game = Game(state=State(), p1=p1, p2=p2)
    hist = game.play()
    print("Game over!", hist.pop(0), "wins!")
    util.pprint(hist)
else:
    print("Usage: python3 main.py PlayerType PlayerType")

