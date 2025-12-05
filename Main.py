import networkx as nx
from Node import Node
from Simulator import simulator


G = nx.Graph()
G.add_edges_from([
    (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (3, 6), (4, 6), (5, 6), (5, 7), (6, 7), (7, 8), 
    (6, 8), (8, 9), (7, 9), (9, 10), (8, 10), (10, 11), (9, 11), (11, 12), (10, 12), (12, 6),                
])

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

#[Transmit/Error, Start, End, Origin(if error)]
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

simulator(G, Nodes, testingSequence)