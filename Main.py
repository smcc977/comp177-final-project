import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 3), (3, 4), (4, 5)])

pos = nx.spring_layout(G)  # Using a spring layout
# Or define manually:
# pos = {1: (0, 0), 2: (1, 1), 3: (1, 0), 4: (2, 1), 5: (2, 0)}

nx.draw_networkx(G, pos, with_labels=True, node_color='skyblue', node_size=1000, font_size=10, font_weight='bold')

plt.title("My NetworkX Graph")
plt.axis('off')  # Hides the Matplotlib axes
plt.show()
