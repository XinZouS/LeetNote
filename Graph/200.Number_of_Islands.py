'''
🍊200. Number of Islands

Medium  https://leetcode.com/problems/number-of-islands/
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

'''

#python key: BFS flood island  140 ms, faster than 69.57%
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        if len(grid) == 0 or len(grid[0]) == 0:
            return self.res
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == '1':
                    self.res += 1
                    self.flood(y, x, grid)
        return self.res
    
    def flood(self, y: int, x: int, grid: List[List[str]]):
        if y < 0 or x < 0 or y >= len(grid) or x >= len(grid[y]):
            return
        if grid[y][x] != '1':
            return
        grid[y][x] = '0'
        self.flood(y - 1, x, grid)
        self.flood(y, x - 1, grid)
        self.flood(y + 1, x, grid)
        self.flood(y, x + 1, grid)


###########################################################################


class Solution_2:
    
    # not good: 340 ms, faster than 5.34%
    
    #========================================================================
    class UnionFind:
        # O(n)
        def __init__(self, n: int):
            self.count = n
            self.parent = [i for i in range(n)]
            self.treeSize = [1 for _ in range(n)]
            
        # O(1)
        def union(self, a: int, b: int):
            pA = self._find(a)
            pB = self._find(b)
            if pA == pB:
                return
            # 小树接到大树下面，较平衡
            if self.treeSize[pA] < self.treeSize[pB]:
                self.parent[pA] = pB
                self.treeSize[pB] += self.treeSize[pA]
            else:
                self.parent[pB] = pA
                self.treeSize[pA] += self.treeSize[pB]
            self.count -= 1
        
        # O(1)
        def _find(self, x: int) -> int:
            while x != self.parent[x]:
                self.parent[x] = self.parent[self.parent[x]] # path zip!
                x = self.parent[x]
            return x
        
        # O(1)
        def isConnected(self, a, b) -> bool:
            pA = self._find(a)
            pB = self._find(b)
            return pA == pB
        
    #========================================================================
        
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        water = 0
        self.lenY, self.lenX = len(grid), len(grid[0])
        self.gridSize = self.lenY * self.lenX
        self.directions = [(1,0), (-1,0), (0,1), (0,-1)]
        self.uf = self.UnionFind(self.gridSize)
        self.grid = grid
        for y in range(self.lenY):
            for x in range(self.lenX):
                if grid[y][x] == '1':
                    land = y * self.lenX + x
                    for d in self.directions:
                        self.dfs(y + d[0], x + d[1], land)
                else:
                    water += 1
        return self.uf.count - water
        
    def dfs(self, y: int, x: int, land: int):
        if y < 0 or x < 0 or y >= self.lenY or x >= self.lenX:
            return
        cur = y * self.lenX + x
        if cur == land or self.grid[y][x] != '1' or self.uf.isConnected(cur, land):
            return
        self.uf.union(cur, land)
        for d in self.directions:
            self.dfs(y + d[0], x + d[1], land)
        
        