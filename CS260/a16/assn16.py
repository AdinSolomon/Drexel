# abs358@drexel.edu

from heapq import *

def display(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def dijkstra(matrix, start):
    # initialize distances
    Distances = [float("inf") for x in range(nodes)]
    Distances[start] = 0
    # initialize edge heap
    Heap = []
    for node in range(len(Distances)):
        if Distances[node] != float("inf"):
            heappush(Heap, (Distances[node], node))
    while True:
        try:
            u = heappop(Heap)[1]
            # get the nodes adjacent to u
            adjacent_nodes = []
            for d in range(nodes):
                if d != u and matrix[u][d] != float("inf"):
                    adjacent_nodes.append(d)
            # do the thing
            for v in adjacent_nodes:
                if Distances[v] > Distances[u] + matrix[u][v]:
                    Distances[v] = Distances[u] + matrix[u][v]
                    # fix the heap - add the new adjacent bois
                    for d in range(nodes):
                        if d != u and matrix[u][d] != float("inf"):
                            heappush(Heap, (matrix[u][d], d))
        except IndexError:
            break
    print("Distances =", Distances)

if __name__ == "__main__":
    # get the filename
    filename = input("File containing graph: ")
    # load in the adjacency matrix
    with open(filename, "r") as f:
        nodes = int(f.readline().strip()[0])
        # love me some concise adjacency matrix initialization
        matrix = [[(0 if a == b else float("inf")) for a in range(nodes)] for b in range(nodes)]
        while ("" != (edge := f.readline())):
            edge = edge.split()
            matrix[int(edge[0])][int(edge[1])] = float(edge[2])
        display(matrix)
    print()
    # start the cmdline interface
    menu = "Possible Commands are:\n" + \
        "dijkstra x - Runs Dijkstra starting at node X. X must be an integer\n" + \
        "help - prints this menu\n" + \
        "exit or ctrl-D - Exits the program"
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
        if argv[0] != "dijkstra":
            print("\tNot a valid command - try again...")
            print(menu)
        else:
            if ((start := int(argv[1])) >= nodes):
                print("\tNot a valid start node - must be a number less that", nodes)
            else:
                dijkstra(matrix, start)