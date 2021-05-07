'''
🍊684. Redundant Connection

Medium  https://leetcode.com/problems/redundant-connection/
In this problem, a tree is an undirected graph that is connected and has no cycles.
You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.
Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

Example 1:
Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]

Example 2:
Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]

'''
class Solution:
    
    class UnionFind:
        def __init__(self, n: int):
            self.parent = [i for i in range(n)]
            self.treeSize = [1 for _ in range(n)]
            self.count = n
        
        def union(self, a: int, b: int):
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
        
        def isConnected(self, a: int, b: int) -> bool:
            a = self.find(a)
            b = self.find(b)
            return a == b
        
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        uf = self.UnionFind(n + 1)
        for edge in edges:
            a, b = edge[0], edge[1]
            if uf.isConnected(a, b):
                return edge
            uf.union(a, b)
        return None
