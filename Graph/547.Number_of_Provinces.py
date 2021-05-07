'''
🍊547. Number of Provinces
Medium  https://leetcode.com/problems/number-of-provinces/

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
A province is a group of directly or indirectly connected cities and no other cities outside of the group.
You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
Return the total number of provinces.
'''

class Solution:
    
    class UnionFind:
        def __init__(self, n: int):
            self.parent = [i for i in range(n)]
            self.treeSize = [1 for _ in range(n)]
            self.count = n
        
        def union(self, a: int, b: int):
            a = self._find(a)
            b = self._find(b)
            if a == b:
                return
            if self.treeSize[a] < self.treeSize[b]:
                self.parent[a] = b
                self.treeSize[b] += self.treeSize[a]
            else:
                self.parent[b] = a
                self.treeSize[a] += self.treeSize[b]
            self.count -= 1
    
        def _find(self, x: int) -> int:
            while self.parent[x] != x:
                self.parent[x] = self.parent[self.parent[x]]
                x = self.parent[x]
            return x
			
		# we don't need this func in this case, but for the consistency of the UF, still put it:
        def isConnected(self, a: int, b: int) -> bool:
            a = self._find(a)
            b = self._find(b)
            return a == b
    
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected or len(isConnected) == 0 or len(isConnected[0]) == 0:
            return 0
        lenY, lenX = len(isConnected), len(isConnected[0])
        uf = self.UnionFind(lenY)
        cities = lenY
        for y in range(lenY):
            for x in range(y + 1, lenX):
                if isConnected[y][x] == 1:
                    uf.union(y, x)
        return uf.count
