import time

class Node:
    def __init__(self, id, graph):
        self.id=id
        self.neighbours=self.findNeighbours(graph)
        self.cache = []
        self.timeout = 10

    def findNeighbours(self, graph):
        neighbors = []
        for node in graph.nodes(data=True):
            #print(node[0])
            if graph.adj[self.id].__contains__(node[0]):
                neighbors.append(node[0])
        return neighbors

    def printNeighbors(self):
        print(f"{self.id}: {self.neighbours}")

    def addPath(self, path):
        self.cache.append((path, time.time()))

    def checkCacheTimeout(self):
        t = time.time()
        for path, pathTime in self.cache:
            if t - pathTime > self.timeout:
                self.cache.remove(path)
