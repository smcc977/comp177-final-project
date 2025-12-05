from collections import deque
from Node import Node
import matplotlib.pyplot as plt
import networkx as nx
import time

# BFS is used to simulate a Route Request
def bfs(graph, Nodes, startNode, goalNode):
    visited = set()
    queue = deque([(startNode, [startNode])])

    while queue:
        current, path = queue.popleft()

        if current == goalNode: # Found path
            Nodes[current-1].addPath(path)
            for node in path:
                Nodes[node-1].addPath(path[path.index(node):])
            return path

        if current not in visited: # Add to path
            visited.add(current)
            Nodes[current-1].addPath(path)
            for neighbor in graph.neighbors(current):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None  # No path found

# Simulator will follow the testing sequence to simulate the behavior of DSR
def simulator (G, Nodes, testingSequence):
    count_searches = 0 #count number of route discoveries performed
    count_routes = 0 #count number of routes used
    count_dropped = 0 #count number of edges dropped
    count_display = 0 #count number of graphs created

    # Loop through testing sequence
    for instr in testingSequence:
        # If there is no instruction display the current graph
        if len(instr) == 0:
            print()
            count_display += 1
            nx.draw_networkx(G, nx.spring_layout(G), with_labels=True, node_color='skyblue', node_size=1000, font_size=10, font_weight='bold')
            plt.title(f"Graph #{count_display}")
            plt.axis('off')  # Hides the Matplotlib axes
            plt.savefig(f"{count_display}Graph.png") # saves graph
            plt.show(block=False) # doesn't block program
            plt.clf() # clears figure

        #Instruction to find path
        elif instr[0] == 0:
            print("Finding path from ", instr[1], "to ", instr[2])
            start_time = time.time()
            path = Nodes[instr[1]-1].getPath(instr[2])
            if path is None:
                print("Route Not Cached: Using Route Discovery")
                path = bfs(G, Nodes, instr[1], instr[2])
                count_searches += 1
            else:
                print("Route found in Cache")

            if path != None and len(path) == 0:
                print("No path found")
            else:
                print(f"Path from {instr[1]} to {instr[2]}:", path)
                count_routes += 1
            print("Took ", round((time.time() - start_time) * 1000000, 3), " ms")

        elif instr[0] == 1:
            start_time = time.time()
            G.remove_edge(instr[1], instr[2])
            count_dropped += 1
            for node in Nodes:
                node.updateNeighbours(G)
            for node in Nodes[instr[1]-1].getPath(instr[3]):
                Nodes[node - 1].errorPath([instr[1],instr[2]])
            print("Removed link", instr[1], "to", instr[2], "add updated caches in nodes", Nodes[instr[1]-1].getPath(instr[3]))
            print("Took ", round((time.time() - start_time) * 1000000, 3), " ms")

    print(f"Number of searches: {count_searches}")
    print(f"Number of routes: {count_routes}")
    print(f"Number of dropped: {count_dropped}")