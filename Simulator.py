from collections import deque
from Node import Node
import matplotlib.pyplot as plt
import networkx as nx
import os
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
def simulator (G, Nodes, testingSequence, name):
    # If it doesn't exist, create a folder for the simulation
    if not os.path.exists(name):
        os.mkdir(name)
    # Switch to simulation directory to ensure graphs are saved in organized way
    os.chdir(name)
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
            plt.savefig(f"{count_display}{name}Graph.png") # saves graph
            plt.show(block=False) # doesn't block program
            plt.clf() # clears figure

        #Instruction to find path
        elif instr[0] == 0:
            # Looks for path
            print("Finding path from ", instr[1], "to ", instr[2])
            start_time = time.time() # Starts timing
            # Check the cache in starting node for an existing path
            path = Nodes[instr[1]-1].getPath(instr[2])
            # If no path in cache
            if path is None:
                print("Route Not Cached: Using Route Discovery")
                # Simulate Route Request with BFS search
                path = bfs(G, Nodes, instr[1], instr[2])
                count_searches += 1 #increament count searches
                # Output time search took
                print("BFS Took ", round((time.time() - start_time) * 1000, 6), " ms")
            # If route found in cache
            else:
                # Output time cache route took
                print("Route found in Cache")
                print("Cache Lookup Took ", round((time.time() - start_time) * 1000, 6), " ms")

            # If path has no length
            if path != None and len(path) == 0:
                # Path was not found
                print("No path found")
            # If path has a route
            else:
                # Output first and last node
                print(f"Path from {instr[1]} to {instr[2]}:", path)
                count_routes += 1 #increment count routes

        # If instruction to remove edge
        elif instr[0] == 1:
            # Remove edge from graph
            G.remove_edge(instr[1], instr[2])
            count_dropped += 1 #increment count dropped
            for node in Nodes: # For all nodes
                node.updateNeighbors(G) # Update awareness of neighbors to remove missing connection
            if Nodes[instr[1]-1].getPath(instr[3]) is not None: # If a path to the start node exists
                for node in Nodes[instr[1]-1].getPath(instr[3]): # For every node in that path
                    Nodes[node - 1].errorPath([instr[1],instr[2]]) # Remove the missing edge from cache
            #Output results of link removal
            print("Removed link", instr[1], "to", instr[2], "add updated caches in nodes", Nodes[instr[1]-1].getPath(instr[3]))

    #Display stats gathered during simulation
    print(f"Number of searches: {count_searches}")
    print(f"Number of routes: {count_routes}")
    print(f"Number of dropped: {count_dropped}")
    os.chdir('..')