import networkx as nx
from Node import Node
from Simulator import simulator


print("Simulating 12 node graph")
# Initializing Graph Object
G = nx.Graph()
# Adding edges to Graph
G.add_edges_from([
    (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (3, 6), (4, 6), (5, 6), (5, 7), (6, 7), (7, 8), 
    (6, 8), (8, 9), (7, 9), (9, 10), (8, 10), (10, 11), (9, 11), (11, 12), (10, 12), (12, 6),                
])

# Initializing Nodes
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

# Adding all nodes to an array
Nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12]

# Creating the testing sequences the program will simulate
# [Transmit/Error, Start, End, Origin(if error)]
testingSequence = [[],
    [0, 1, 10],
    [0, 1, 10],
    [0, 1, 10],
    [0, 3, 10],
    [],
    [0, 3, 12],
    [0, 6, 11],
    [],
    [1, 6, 8, 1],
    [0, 1, 10],
    [],
    [0, 1, 10],
    [],
    [1, 9, 10, 1],
    [0, 1, 10],
    [1, 7, 9, 1],
    [0, 1, 10],
    [],
    [0, 1, 12],
    [0, 1, 12],
    [0, 12, 1],
    [],
    [1, 5, 6, 1],
    [0, 1, 7],
    [1, 4, 5, 1],
    [0, 1, 7],
    [],
    [0, 11, 3],
    [0, 3, 11],
    [],
    [1, 10, 11, 3],
    [1, 11, 12, 3],
    [0, 3, 12],
    [],
]

#Run simulator
simulator(G, Nodes, testingSequence, "Small")


print("Simulating 48 node graph")


# Initializing Graph Object with 48 nodes
G = nx.Graph()

# Creating a mesh-like topology with 48 nodes
# Grid-like structure with additional cross-connections for redundancy
G.add_edges_from([
    # Row 1 (nodes 1-8)
    (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8),
    # Row 2 (nodes 9-16)
    (9, 10), (10, 11), (11, 12), (12, 13), (13, 14), (14, 15), (15, 16),
    # Row 3 (nodes 17-24)
    (17, 18), (18, 19), (19, 20), (20, 21), (21, 22), (22, 23), (23, 24),
    # Row 4 (nodes 25-32)
    (25, 26), (26, 27), (27, 28), (28, 29), (29, 30), (30, 31), (31, 32),
    # Row 5 (nodes 33-40)
    (33, 34), (34, 35), (35, 36), (36, 37), (37, 38), (38, 39), (39, 40),
    # Row 6 (nodes 41-48)
    (41, 42), (42, 43), (43, 44), (44, 45), (45, 46), (46, 47), (47, 48),

    # Vertical connections between rows
    (1, 9), (2, 10), (3, 11), (4, 12), (5, 13), (6, 14), (7, 15), (8, 16),
    (9, 17), (10, 18), (11, 19), (12, 20), (13, 21), (14, 22), (15, 23), (16, 24),
    (17, 25), (18, 26), (19, 27), (20, 28), (21, 29), (22, 30), (23, 31), (24, 32),
    (25, 33), (26, 34), (27, 35), (28, 36), (29, 37), (30, 38), (31, 39), (32, 40),
    (33, 41), (34, 42), (35, 43), (36, 44), (37, 45), (38, 46), (39, 47), (40, 48),

    # Diagonal connections for redundancy
    (1, 10), (2, 11), (3, 12), (4, 13), (5, 14), (6, 15), (7, 16),
    (9, 18), (10, 19), (11, 20), (12, 21), (13, 22), (14, 23), (15, 24),
    (17, 26), (18, 27), (19, 28), (20, 29), (21, 30), (22, 31), (23, 32),
    (25, 34), (26, 35), (27, 36), (28, 37), (29, 38), (30, 39), (31, 40),
    (33, 42), (34, 43), (35, 44), (36, 45), (37, 46), (38, 47), (39, 48),

    # Additional cross-connections for alternate paths
    (2, 9), (3, 10), (6, 13), (7, 14),
    (10, 17), (11, 18), (14, 21), (15, 22),
    (18, 25), (19, 26), (22, 29), (23, 30),
    (26, 33), (27, 34), (30, 37), (31, 38),
    (34, 41), (35, 42), (38, 45), (39, 46),

    # Long-range connections for shortcuts
    (1, 17), (8, 24), (1, 25), (8, 32),
    (17, 33), (24, 40), (25, 41), (32, 48),
    (1, 48), (8, 41), (4, 28), (5, 37),
])

# Initializing all 48 Nodes
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
n13 = Node(13, G)
n14 = Node(14, G)
n15 = Node(15, G)
n16 = Node(16, G)
n17 = Node(17, G)
n18 = Node(18, G)
n19 = Node(19, G)
n20 = Node(20, G)
n21 = Node(21, G)
n22 = Node(22, G)
n23 = Node(23, G)
n24 = Node(24, G)
n25 = Node(25, G)
n26 = Node(26, G)
n27 = Node(27, G)
n28 = Node(28, G)
n29 = Node(29, G)
n30 = Node(30, G)
n31 = Node(31, G)
n32 = Node(32, G)
n33 = Node(33, G)
n34 = Node(34, G)
n35 = Node(35, G)
n36 = Node(36, G)
n37 = Node(37, G)
n38 = Node(38, G)
n39 = Node(39, G)
n40 = Node(40, G)
n41 = Node(41, G)
n42 = Node(42, G)
n43 = Node(43, G)
n44 = Node(44, G)
n45 = Node(45, G)
n46 = Node(46, G)
n47 = Node(47, G)
n48 = Node(48, G)

# Adding all nodes to an array
Nodes = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15, n16,
         n17, n18, n19, n20, n21, n22, n23, n24, n25, n26, n27, n28, n29, n30, n31, n32,
         n33, n34, n35, n36, n37, n38, n39, n40, n41, n42, n43, n44, n45, n46, n47, n48]

# Creating the testing sequences for 48-node network
# [Transmit/Error, Start, End, Origin(if error)]
testingSequence = [
    [],
    [0, 1, 48],
    [0, 1, 48],
    [0, 1, 48],
    [0, 5, 48],
    [0, 10, 40],
    [],
    [0, 1, 24],
    [0, 8, 41],
    [0, 17, 48],
    [],
    [1, 1, 48, 1],
    [0, 1, 48],
    [],
    [0, 1, 48],
    [0, 20, 45],
    [0, 30, 15],
    [],
    [1, 25, 33, 1],
    [0, 1, 48],
    [1, 27, 35, 1],
    [0, 1, 48],
    [],
    [0, 1, 32],
    [0, 1, 32],
    [0, 32, 1],
    [0, 16, 33],
    [],
    [1, 10, 18, 1],
    [0, 1, 25],
    [1, 19, 27, 1],
    [0, 1, 25],
    [1, 28, 36, 10],
    [0, 10, 40],
    [],
    [0, 48, 1],
    [0, 1, 48],
    [0, 24, 41],
    [0, 8, 33],
    [],
    [1, 17, 25, 1],
    [1, 26, 34, 1],
    [0, 1, 48],
    [0, 10, 48],
    [],
    [0, 2, 47],
    [0, 3, 46],
    [0, 4, 45],
    [0, 5, 44],
    [],
    [1, 34, 42, 2],
    [1, 35, 43, 3],
    [0, 2, 47],
    [0, 3, 46],
    [],
    [0, 15, 35],
    [0, 35, 15],
    [0, 20, 28],
    [0, 28, 20],
    [],
    [1, 1, 9, 1],
    [1, 9, 17, 1],
    [1, 2, 10, 1],
    [0, 1, 48],
    [],
    [0, 8, 1],
    [0, 16, 9],
    [0, 24, 17],
    [0, 32, 25],
    [0, 40, 33],
    [0, 48, 41],
    [],
]

# Run simulator
simulator(G, Nodes, testingSequence, "Large")