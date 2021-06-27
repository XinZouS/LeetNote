'''
🍊1840 · 矩阵还原
中等  https://www.lintcode.com/problem/1840/
现有一个nn行mm列的矩阵beforebefore，对于before里的每一个元素before[i][j]before[i][j]，我们会使用以下算法将其转化为after[i][j]after[i][j]。现给定afterafter矩阵，请还原出原有的矩阵beforebefore。
s = 0
for i1: 0 -> i
    for j1: 0 -> j
        s = s + before[i1][j1]
after[i][j] = s
1≤n, m≤1000

样例1：
输入:
2
2
[[1,3],[4,10]]
输出: 
[[1,2],[3,4]]
解释:
before:
1 2
3 4
after:
1 3
4 10
'''

# python
class Solution:
    """
    @param n: the row of the matrix
    @param m: the column of the matrix
    @param after: the matrix
    @return: restore the matrix
    """
    def matrixRestoration(self, n, m, after):
        if m < 2 and n < 2:
            return after
        lenY, lenX = n, m
        before = [[0 for x in range(lenX)] for y in range(lenY)]
        before[0][0] = after[0][0]
        for y in range(lenY - 1, 0, -1):
            before[y][0] = after[y][0] - after[y - 1][0]
        for x in range(lenX - 1, 0, -1):
            before[0][x] = after[0][x] - after[0][x - 1]
        for y in range(lenY - 1, 0, -1):
            for x in range(lenX - 1, 0, -1):
                before[y][x] = after[y][x] - after[y - 1][x] - after[y][x - 1] + after[y - 1][x - 1] 
        return before

