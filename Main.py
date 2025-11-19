import networkx as nx
import matplotlib.pyplot as plt
from Node import Node
from collections import deque


G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])

pos = nx.spring_layout(G)  # Using a spring layout
# Or define manually:
# pos = {1: (0, 0), 2: (1, 1), 3: (1, 0), 4: (2, 1), 5: (2, 0)}

n1 = Node(1, G)
n2 = Node(2, G)
n3 = Node(3, G)
n4 = Node(4, G)
n5 = Node(5, G)
Nodes = [n1, n2, n3, n4, n5]
n1.printNeighbors()
n2.printNeighbors()
n3.printNeighbors()
n4.printNeighbors()
n5.printNeighbors()

nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=10, font_weight='bold')


def bfs(graph, startNode, goalNode):
    visited = set()
    queue = deque([(startNode, [startNode])])

    while queue:
        current, path = queue.popleft()

        if current == goalNode: # Found path
            Nodes[current-1].addPath(path)
            return path  

        if current not in visited: # Add to path
            visited.add(current)
            Nodes[current-1].addPath(path)
            for neighbor in graph.neighbors(current):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))

    return None  # No path found


start = 1 # Start Node
goal = 5 # Goal Node

path = bfs(G, start, goal) # Path from start to goal

n5.printCache()

if path != None and len(path) == 0:
    print("No path found")
else:
    print(f"Path from {start} to {goal}:", path)

plt.title("My NetworkX Graph")
plt.axis('off')  # Hides the Matplotlib axes
plt.show()
