# adinbsolomon@gmail.com

import random
import heapq

from rgb import *

class Node:
    def __init__(self, parent, state):
        self.parent = parent
        self.state = state
    def __str__(self):
        return self.state.__str__()
    def depth(self):
        return 0 if self.parent == None else 1 + self.parent.depth()
    def path_to(self):
        return ( [] if self.parent == None else self.parent.path_to() ) + [self.state]

def node_depth(n):
    return 0 if n == None else n.depth()

class Agent:

    def random_walk(self, state, n=8):
        node = Node(parent=None, state=state)
        while (n := n - 1) > 0:
            node = Node(parent=node, state=node.state.clone().execute(random.choice(node.state.actions())))
        return node.path_to()

    def _search(self, state, func):
        #@total_ordering
        class _struct:
            def __init__(self, node: Node, score):
                self.node = n
                self.score = score
            # custom class comparisons
            # 

        this_node = Node(parent=None, state=state)
        this_score = func(this_node)
        nodes_found = 0 # this is a tie-breaker for scoring and is decremented bc of minheap
        this_struct = [this_score, nodes_found, this_node]
        
        OPEN = [this_struct] # this holds structs
        heapq.heapify(OPEN) # it's also a heap
        CLOSED = [] # this is a regular list and will also hold structs
        while len(OPEN) > 0:
            this_struct = heapq.heappop(OPEN)
            this_score = this_struct[0]
            this_node = this_struct[2]
            if this_node.state.is_goal():
                break
            util.pprint(this_node.path_to())
            this_next_states = [this_node.state.clone().execute(action) for action in this_node.state.actions()]
            for next_state in this_next_states:
                state_in_open = False
                for open_struct in OPEN:
                    open_node = open_struct[2]
                    if open_node.state == next_state:
                        this_node_depth = node_depth(this_node)
                        open_node_parent_depth = node_depth(open_node.parent)
                        if this_node_depth < open_node_parent_depth: # lower score is better bc of heap
                            open_node.parent = this_node
                            open_struct[0] = func(open_node)
                            heapq.heapify(OPEN) # node's score changed -> re-heapify
                        state_in_open = True
                        break
                if state_in_open:
                    continue
                state_in_closed = False
                for closed_struct in CLOSED:
                    closed_node = closed_struct[2]
                    if closed_node.state == next_state:
                        this_node_depth = node_depth(this_node)
                        closed_node_parent_depth = node_depth(closed_node.parent)
                        if this_node_depth < closed_node_parent_depth: # lower score is better bc of heap
                            closed_node.parent = this_node
                            closed_struct[0] = func(closed_node)
                            # re-evaluate all descendants (this could be done a lot better...)
                            changed_parent = this_node
                            while changed_parent != None:
                                print("OOOOOOF")
                                exit()
                                for _open_struct in OPEN:
                                    if _open_struct[2].parent == changed_parent:
                                        _open_struct[0] = func(_open_struct[2])
                                        changed_parent = _open_struct[2]
                                        break
                                for _closed_struct in CLOSED:
                                    if _closed_struct[2].parent == changed_parent:
                                        _closed_struct[0] = func(_closed_struct[2])
                                        changed_parent = _closed_struct[2]
                                        break
                            heapq.heapify(CLOSED) # re-heapify bc of changes
                        state_in_closed = True
                        break
                if state_in_closed:
                    continue
                else: # state is not in open nor in closed
                    nodes_found -= 1 # this is so that the heap takes the correct next node (at least in dfs for DEFAULT_STATE), but decrementing isn't necessary
                    new_node = Node(parent=this_node, state=next_state)
                    new_struct = [func(new_node), nodes_found, new_node]
                    heapq.heappush(OPEN, new_struct)
            # done expanding this_node
            CLOSED.append(this_struct)
        # this_node now stores the goal state
        print("Done exploring! Took", len(CLOSED)+1, "iterations. Preparing path:")
        return this_node.path_to()

    def bfs_func(self, node): # lower score is better bc of heap
        return node_depth(node)
    def bfs(self, state):
        return self._search(state, self.bfs_func)
    
    def dfs_func(self, node): # lower score is better bc of heap
        return -1 * node_depth(node)
    def dfs(self, state):
        return self._search(state, self.dfs_func)

    # a_star_func is passed into a_star and is declared in main
    #   because the heuristic is dependent on the state class
    def a_star(self, state, heuristic):
        return self._search(state, heuristic)
