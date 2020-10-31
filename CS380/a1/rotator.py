# abs358@drexel.edu

import sys

# concise string indexer found online but converted to lambda for elegance
# https://stackoverflow.com/a/41752999/13747259
# I could write another but this is very neat
repl = lambda t,i,r:'%s%s%s'%(t[:i],r,t[i+1:])

DEFAULT_BLANK = " "
DEFAULT_SEPARATOR = "|"
DEFAULT_STATE = "12345" + \
                DEFAULT_SEPARATOR + \
                "1234" + DEFAULT_BLANK + \
                DEFAULT_SEPARATOR + \
                "12345"

class State:
    def __init__(self, str = DEFAULT_STATE):
        self.data = str.split(DEFAULT_SEPARATOR)
    def __str__(self):
        return DEFAULT_SEPARATOR.join(self.data)
    def __eq__(self, other):
        return self.data == other.data
    def blank_spot(self):
        for y in range(len(self.data)):
            if (x := self.data[y].find(DEFAULT_BLANK)) != -1:
                return [x, y]
        return [-1, -1]
    def clone(self):
        return State(self.__str__())
    def is_goal(self):
        for i in range(len(self.data[0])):
            s = set()
            for row in self.data:
                s.add(row[i])
            if len(s) > 1:
                if len(s) != 2 or DEFAULT_BLANK not in s:
                    return False
        return True
    def actions(self):
        actions = []
        # Rotations
        for i in range(len(self.data)):
            actions.append(Action("rotate", [i, -1]))
            actions.append(Action("rotate", [i,  1]))
        # Slides
        blank = self.blank_spot()
        if blank[1] == 0:
            actions.append(Action("slide", [blank[0], blank[1]+1, blank[0], blank[1]]))
        elif blank[1] == len(self.data)-1:
            actions.append(Action("slide", [blank[0], blank[1]-1, blank[0], blank[1]]))
        else:
            actions.append(Action("slide", [blank[0], blank[1]-1, blank[0], blank[1]]))
            actions.append(Action("slide", [blank[0], blank[1]+1, blank[0], blank[1]]))
        return actions
    def execute(self, action):
        s = self.clone()
        if action.action == "rotate":
            if action.args[1] == -1:
                s.data[action.args[0]] = \
                    s.data[action.args[0]][1:] + \
                    s.data[action.args[0]][0]
            else:
                s.data[action.args[0]] = \
                    s.data[action.args[0]][-1] + \
                    s.data[action.args[0]][:-1]
        if action.action == "slide":
            temp = s.data[action.args[1]][action.args[0]]
            s.data[action.args[1]] = repl(s.data[action.args[1]], action.args[0], DEFAULT_BLANK)
            s.data[action.args[3]] = repl(s.data[action.args[3]], action.args[2], temp)
        return s


class Action:
    def __init__(self, action = "", args = [-1,-1,-1,-1]):
        self.action = action
        self.args = args
    def __str__(self):
        if self.action == "rotate":
            return "rotate(" + str(self.args[0]) + "," + \
                                str(self.args[1]) + ")"
        if self.action == "slide":
            return "slide(" + str(self.args[0]) + "," + \
                                str(self.args[1]) + "," + \
                                str(self.args[2]) + "," + \
                                str(self.args[3]) + ")"

if __name__ == "__main__":
    try:
        command = sys.argv[1]
    except:
        exit
    try:
        s = State(sys.argv[2])
    except:
        s = State()

    if command == "print":
        print(s)
    if command == "goal":
        print(s.is_goal())
    if command == "actions":
        for action in s.actions():
            print(action)
    if command[:4] == "walk":
        visited_states = []
        while True not in [s == p for p in visited_states]:
            visited_states.append(s)
            s = s.execute(s.actions()[int(command[4])])
        for p in visited_states:
            print(p)


        