class ConnectingGraph3:

    # @param {int} n
    def __init__(self, n):
        # initialize your data structure here.
        self.father = [0 for _ in range(n+1)]
        self.edges = n
    def find(self, a):
        if self.father[a] == 0:
            return a
        self.father[a] = self.find(self.father[a])
        return self.father[a]

    # @param {int} a, b
    # return nothing
    def connect(self, a, b):
        # Write your code here
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.father[root_a] = root_b
            self.edges -= 1

    # @param {int} a
    # return {int} the number of connected component
    # in the graph
    def query(self):
        # Write your code here
        return self.edges
        
