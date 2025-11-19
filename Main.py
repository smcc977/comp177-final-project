import networkx as nx
import matplotlib.pyplot as plt
from Node import Node
from collections import deque


G = nx.Graph()
G.add_edges_from([
    (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (3, 6), (4, 6), (5, 6), (5, 7), (6, 7), (7, 8), 
    (6, 8), (8, 9), (7, 9), (9, 10), (8, 10), (10, 11), (9, 11), (11, 12), (10, 12), (12, 6),                
])

pos = nx.spring_layout(G)  # Using a spring layout
# Or define manually:
# pos = {1: (0, 0), 2: (1, 1), 3: (1, 0), 4: (2, 1), 5: (2, 0)}

n1 = Node(1, G)
n2 = Node(2, G)
n3 = Node(3, G)
n4 = Node(4, G)
n5 = Node(5, G)
n6 = Node(6, G)
n7 = Node(7, G)
n8 = Node(8, G)
n9 = Node(9, G)
n10 = Node(10, G)
n11 = Node(11, G)
n12 = Node(12, G)

Nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12]
"""n1.printNeighbors()
n2.printNeighbors()
n3.printNeighbors()
n4.printNeighbors()
n5.printNeighbors()"""

#[Transmit/Error, Start, End]
testingSequence = [[0, 1, 10], [0, 1, 10], [1, 6, 8, 1], [0, 1, 10], [0, 3, 10]]


def bfs(graph, startNode, goalNode):
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

'''
start = 1 # Start Node
goal = 10 # Goal Node

path = bfs(G, start, goal) # Path from start to goal

n6.printCache()
n3.printCache()
print(n3.getPath(10))

G.remove_edge(6, 8)
for node in Nodes:
    node.updateNeighbours(G)

for node in n6.getPath(start):
    Nodes[node-1].errorPath([6,8])

n6.printCache()
n3.printCache()
print(n3.getPath(10))

path = bfs(G, start, goal) # Path from start to goal

n6.printCache()
n3.printCache()
print(n3.getPath(10))

if path != None and len(path) == 0:
    print("No path found")
else:
    print(f"Path from {start} to {goal}:", path)

'''
for instr in testingSequence:
    if instr[0] == 0:
        path = Nodes[instr[1]-1].getPath(instr[2])
        if path is None:
            path = bfs(G, instr[1], instr[2])
        if path != None and len(path) == 0:
            print("No path found")
        else:
            print(f"Path from {instr[1]} to {instr[2]}:", path)
    else:
        G.remove_edge(instr[1], instr[2])
        for node in Nodes:
            node.updateNeighbours(G)

        for node in Nodes[instr[1]-1].getPath(instr[3]):
            Nodes[node - 1].errorPath([instr[1],instr[2]])

        print("Removed link", instr[1], "to", instr[2], "add updated caches.")


nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=10, font_weight='bold')
plt.title("My NetworkX Graph")
plt.axis('off')  # Hides the Matplotlib axes
plt.show()
