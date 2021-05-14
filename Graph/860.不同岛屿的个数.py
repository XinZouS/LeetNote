'''
🍊860.不同岛屿的个数
https://www.lintcode.com/problem/860/

给定一个由0和1组成的非空的二维网格，一个岛屿是指四个方向（包括横向和纵向）都相连的一组1（1表示陆地）。你可以假设网格的四个边缘都被水包围。
找出所有不同的岛屿的个数。如果一个岛屿与另一个岛屿形状相同（不考虑旋转和翻折），我们认为这两个岛屿是相同的。
注意：
11
1
和
1
11
是不同的岛屿，因为我们不考虑旋转和翻折。
网格的每一个维度的长度都不超过50。
样例
样例 1:
输入:
[
[1,1,0,0,1],
[1,0,0,0,0],
[1,1,0,0,1],
[0,1,0,1,1]
]
输出: 3
解释:
11 1 1
1 11
11
1

样例 2:
输入:
[
[1,1,0,0,0],
[1,1,0,0,0],
[0,0,0,1,1],
[0,0,0,1,1]
]
输出: 1

'''

# python key: I do: 
class Solution:
    def numberofDistinctIslands(self, grid):
        if not grid or len(grid) == 0 or len(grid[0]) == 0:
            return 0
        self.lenY, self.lenX = len(grid), len(grid[0])
        self.directions = [(1,0), (-1,0), (0,1), (0,-1)]
        islands = set()
        for y in range(self.lenY):
            for x in range(self.lenX):
                if grid[y][x] == 1:
                    grid[y][x] = 0
                    island = self.bfs(grid, y, x)
                    islands.add(island)
        return len(islands)
        
    def bfs(self, grid, y, x) -> str:
        from collections import deque
        q = deque()
        q.append( (y, x) )
        visited = set()
        visited.add('%i%i' % (y, x))
        path = ''
        while q:
            preY, preX = q.popleft()
            path += '%i%i' % (preY - y, preX - x)
            for dy, dx in self.directions:
                ny, nx = preY + dy, preX + dx # use preY,preX, NOT y,x
                newPath = '%i%i' % (ny, nx)
                if newPath in visited:
                    continue
                if (not self.isValid(ny, nx)) or grid[ny][nx] != 1:
                    continue
                grid[ny][nx] = 0
                q.append((ny, nx))
                visited.add(newPath)
        return path
    def isValid(self, y, x) -> bool:
        return 0 <= y < self.lenY and 0 <= x < self.lenX


