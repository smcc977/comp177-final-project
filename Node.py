class Node:
    def __init__(self, id, graph ):
        self.id=id
        self.neighbours=self.findNeighbours(graph)

    def findNeighbours(self, graph):
        neighbors = []
        for node in graph.nodes(data=True):
            #print(node[0])
            if graph.adj[self.id].__contains__(node[0]):
                neighbors.append(node[0])
        return neighbors

    def printNeighbors(self):
        print(f"{self.id}: {self.neighbours}")