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
    edges = []
    MSTs = [[i] for i in range(len(matrix))]
    


def prim(matrix, start):
    edges = []
    nodes = [start]
    print("\tStarting Node:", start)
    while len(nodes) < len(matrix):
        # find the smallest edge that connects a node in nodes to a node not in nodes
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
            kruskal(matrix)
        if argv[0] == "prim":
            if len(argv) < 2 or ((start := int(argv[1])) >= nodes):
                print("\tPlease include the integer argument less than", nodes)
            else:
                prim(matrix, start)