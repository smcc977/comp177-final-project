import networkx as nx
import matplotlib.pyplot as plt
from Node import Node

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
n1.printNeighbors()
n2.printNeighbors()
n3.printNeighbors()
n4.printNeighbors()
n5.printNeighbors()

nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=10, font_weight='bold')

plt.title("My NetworkX Graph")
plt.axis('off')  # Hides the Matplotlib axes
plt.show()
