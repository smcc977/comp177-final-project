class Node:
    def __init__(self, id, graph ):
        self.id=id
        self.neighbours=self.findNeighbours(graph)

    def findNeighbours(self, graph):
        return graph.neighbors(self.id)
