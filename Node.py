import time

# Node class creates functionality for simulating every node
class Node:
    # Initialization
    def __init__(self, id, graph):
        self.id = id #number to identify node
        self.neighbors = self.findNeighbors(graph) #stores neighbors in accompanying graph
        self.cache = [] #initialize cache
        self.timeout = 1 #init timeout cutoff

    # Find Neighbors will return neighbours to the specific node
    def findNeighbors(self, graph):
        neighbors = [] # initialize arrays
        # For every node in the graph
        for node in graph.nodes(data=True):
            # If it is adjacent to self
            if graph.adj[self.id].__contains__(node[0]):
                #Append node id to array
                neighbors.append(node[0])
        # Return array of neighbors
        return neighbors

    # Update Neighbors is used to update array of neighbors when node is removed
    def updateNeighbors(self, graph):
        # Set neighbors to output of findNeighbors
        self.neighbors = self.findNeighbors(graph)

    # Add Path will add a path to the cache of a node when it is discovered
    def addPath(self, path):
        # If path doesn't originate from self
        if not path[0] == self.id:
            # Append the flipped path to the cache
            self.cache.append((path[::-1], time.time()))
        # If path does originate from self
        else:
            # Append path to the cache
            self.cache.append((path, time.time()))
        # Will remove any duplicate paths in cache, keeping the one most recently added
        for node1, t1 in self.cache:
            for node2, t2 in self.cache:
                if node1 == node2 and  t1 != t2:
                    if t2 > t1:
                        self.cache.remove((node1, t1))
                    else:
                        self.cache.remove((node2, t2))

    # Get Path will return a cached path
    def getPath(self, node):
        # check for timeout in all cache paths
        self.checkCacheTimeout()
        # for every path in cache
        for path, t in self.cache:
            # check if target node is within any path
            if node in path:
                # if it is, return path until target node
                return path[:path.index(node) + 1]
        return None #Route not cached

    # Error Path will remove paths in cache that use the failed link
    def errorPath(self, link):#link should be an array of the two nodes the connection is between ex. [1, 2]
        # for every path in cache
        for path, t in self.cache:
            # for in the length of path
            for i in range(len(path[:-1])):
                # check if error link exists within path
                if [path[i], path[i+1]] == link or [path[i+1], path[i]] == link:
                    # if it does, remove path
                    self.cache.remove((path, t))

    # Check Cache Timeout
    def checkCacheTimeout(self):
        t = time.time() #get current time
        # For all paths in cache
        for path, pathTime in self.cache:
            # If it has existed longer than timeout limit
            if t - pathTime > self.timeout:
                print(f"Node {self.id} timed out path {path} after {pathTime} seconds")
                # Remove route from cache
                self.cache.remove((path,pathTime))

    # Output neighbors
    def printNeighbors(self):
        print(f"Node {self.id} neighbours: {self.neighbors}")

    # Output Cache
    def printCache(self):
        print(f"Node {self.id} cache: {self.cache}")