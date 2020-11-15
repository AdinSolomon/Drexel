
from connect3 import *
from game import *
from agent import *
from human import *

p1 = Player("X")
p2 = Player("O")
h1 = HumanPlayer("X")
h2 = HumanPlayer("O")
r1 = RandomPlayer("X")
r2 = RandomPlayer("O")
m1 = MinimaxPlayer("X")
m2 = MinimaxPlayer("O")

rg = Game(State(), r1, m2)
hist = rg.play()[1:]


