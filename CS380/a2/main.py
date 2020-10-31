# adinbsolomon@gmail.com

from agent import *

def a_star_heuristic1(node):
    h = 0
    # copied from rgb.py > State > is_goal() because I don't really understand the is_legal() function
    s = node.state
    for x in range(s.size):
            for y in range(s.size):
                c = s.get(x, y)
                if c != Cell.EMPTY:
                    deltas = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
                    for dx, dy in deltas:
                        x2, y2 = x+dx, y+dy
                        c2 = s.get(x2, y2)
                        if c == c2:
                            h += 1
    return node.depth() + h

def a_star_heuristic2(node):
    pass

cmd = util.get_arg(1)
if cmd:
    s = State(util.get_arg(2))
    a = Agent()
    if cmd == 'random':
        util.pprint(a.random_walk(s))
    if cmd == 'bfs':
        util.pprint(a.bfs(s))
    if cmd == 'dfs':
        util.pprint(a.dfs(s))
    if cmd == 'a_star':
        util.pprint(a.a_star(s, a_star_heuristic1))