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

    def addPath(self, path):
        if not path[0] == self.id:
            self.cache.append((path[::-1], time.time()))
        else:
            self.cache.append((path, time.time()))

    def getPath(self, node):
        for path, t in self.cache:
            if node in path:
                return path[:path.index(node) + 1]
        return None

    def errorPath(self, link):#link should be an array of the two nodes the connection is between ex. [1, 2]
        for path, t in self.cache:
            for i in range(len(path[:-1])):
                if [path[i], path[i+1]] == link or [path[i+1], path[i]] == link:
                    self.cache.remove(self.cache[path])

    def checkCacheTimeout(self):
        t = time.time()
        for path, pathTime in self.cache:
            if t - pathTime > self.timeout:
                self.cache.remove(path)

    def printNeighbors(self):
        print(f"Node {self.id} neighbours: {self.neighbours}")

    def printCache(self):
        print(f"Node {self.id} cache: {self.cache}")