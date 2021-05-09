'''
🍊1314. Matrix Block Sum
Medium  https://leetcode.com/problems/matrix-block-sum/
Given a m x n matrix mat and an integer k, return a matrix answer where each answer[i][j] is the sum of all elements mat[r][c] for:
	• i - k <= r <= i + k,
	• j - k <= c <= j + k, and
	• (r, c) is a valid position in the matrix.
 
Example 1:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]

Example 2:
Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]

Constraints:
	• m == mat.length
	• n == mat[i].length
	• 1 <= m, n, k <= 100
	• 1 <= mat[i][j] <= 100
'''

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        if not mat or len(mat) == 0 or len(mat[0]) == 0:
            return []
        lenY, lenX = len(mat), len(mat[0])
        res = [[0 for x in range(lenX)] for y in range(lenY)]
        sumM = [[0 for x in range(lenX + 1)] for y in range(lenY + 1)]
        # +1 是为了rangeSum计算时使用y-1和x-1的格子，左边和上边的初始化为0，即可直接for来使用:
        for y in range(1, lenY + 1):
            for x in range(1, lenX + 1):
                sumM[y][x] = sumM[y-1][x] + sumM[y][x-1] - sumM[y-1][x-1] + mat[y-1][x-1]
        for y in range(lenY):
            for x in range(lenX):
                x1, y1 = max(0, x - k), max(0, y - k)
                x2, y2 = min(x + k + 1, lenX), min(y + k + 1, lenY) # MUST +1, and lenXY do NOT -1, bcz x1y1x2y2 are for matSum
                res[y][x] = sumM[y2][x2] - sumM[y2][x1] - sumM[y1][x2] + sumM[y1][x1]
        return res
        

