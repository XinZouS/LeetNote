'''
Medium https://www.lintcode.com/problem/591/
Given n nodes in a graph labeled from 1 to n. There is no edges in the graph at beginning.
You need to support the following method:
        1. connect(a, b), an edge to connect node a and node b
        2. query(), Returns the number of connected component in the graph
Example 1:
Input:
ConnectingGraph3(5)
query()
connect(1, 2)
query()
connect(2, 4)
query()
connect(1, 4)
query()
Output:[5,4,3,3]
Example 2:
Input:
ConnectingGraph3(6)
query()
query()
query()
query()
query()
Output:
[6,6,6,6,6]
'''

class ConnectingGraph3:
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]
        self.treeSize = [1 for _ in range(n + 1)]
        self.count = n
    
    def connect(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.treeSize[a] < self.treeSize[b]:
            self.parent[a] = b
            self.treeSize[b] += self.treeSize[a]
        else:
            self.parent[b] = a
            self.treeSize[a] += self.treeSize[b]
        self.count -= 1
        
    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    """
    @return: An integer
    """
    def query(self):
        return self.count







