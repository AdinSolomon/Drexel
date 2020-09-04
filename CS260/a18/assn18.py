# abs358@drexel.edu

from heapq import *

def display(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def kruskal(matrix):
    # sort the edges
    H = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j and matrix[i][j] != float("inf"):
                heappush(H, (matrix[i][j], min([i,j]), max([i,j])))
    # make the MST
    edges = []
    MSTs = [[i] for i in range(len(matrix))]
    while len(H) > 0:
        edge = heappop(H)
        if not (True in [(edge[1] in MSTs[i] and edge[2] in MSTs[i]) for i in range(len(MSTs))]):
            print("\tSelected edge: [" + str(edge[1]) + ", " + str(edge[2]) + ", " + str(edge[0]) + "]")
            edges.append(edge)
            # merge the two MSTs containing the nodes in the edge
            # sorry this is kinda gross
            done = False
            for i in range(len(MSTs)):
                if done:
                    break
                for j in range(len(MSTs)):
                    if edge[1] in MSTs[i] and edge[2] in MSTs[j]:
                        MSTs[i].extend(MSTs[j])
                        MSTs.pop(j)
                        done = True
                        break
                        
def prim(matrix, start):
    edges = []
    nodes = [start]
    print("\tStarting Node:", start)
    while len(nodes) < len(matrix):
        e = ["bigger", "than", float("inf")]
        [[(e := ([min([n, i]), max([n, i]), matrix[n][i]] if (i not in nodes and matrix[n][i] < e[2]) else e)) for i in range(len(matrix))] for n in nodes]
        edges.append(e)
        nodes.append(e[0] if e[0] not in nodes else e[1])
        print("\tAdded node", nodes[-1], "using edge", e)

if __name__ == "__main__":
    print("Welcome to Minimum Spanning Tree Finder")
    # get the filename
    filename = input("File containing graph: ")
    # load in the adjacency matrix
    with open(filename, "r") as f:
        nodes = int(f.readline().strip()[0])
        # love me some concise adjacency matrix initialization
        matrix = [[(0 if a == b else float("inf")) for a in range(nodes)] for b in range(nodes)]
        while ((edge := f.readline()) != ""):
            edge = edge.split()
            matrix[int(edge[0])][int(edge[1])] = float(edge[2])
            matrix[int(edge[1])][int(edge[0])] = float(edge[2]) # undirected graph
    display(matrix)
    print()
    # start the cmdline interface
    menu = "Commands are:\n" + \
        "exit or ctrl-d - quits the program\n" + \
        "help - prints this menu\n" + \
        "prim integer_value - runs Prim's algorithm starting at node given\n" + \
        "kruskal - runs Kruskal's algorithm"
    print(menu)
    while True:
        try:
            argv = input("\nEnter command: ").split()
        except:
            print("\nBye")
            break
        if len(argv) == 0 or argv[0] == "exit":
            print("Bye")
            break
        if argv[0] == "help":
            print(menu)
            continue
        if argv[0] == "kruskal":
            print("\tRunning Kruskal's Algorithm")
            kruskal(matrix)
        if argv[0] == "prim":
            if len(argv) < 2 or ((start := int(argv[1])) >= nodes):
                print("\tPlease include the integer argument less than", nodes)
            else:
                print("\tRunning Prim's Algorithm")
                prim(matrix, start)