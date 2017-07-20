class Solution(object):
    def validTree(self, n, edges):
        parent = range(n)
        def find(x):
            return x if parent[x] == x else find(parent[x])
        for e in edges:
            x, y = map(find, e)
            if x == y: # that is before we connect the two nodes
            # if they share the same rep. it means when you connect them, you'll create a cycle
                return False
            parent[x] = y
        return len(edges) == n - 1
        
