'''
🍊476. 石子归并
中等  https://www.lintcode.com/problem/476/description
有一个石子归并的游戏。最开始的时候，有n堆石子排成一列，目标是要将所有的石子合并成一堆。合并规则如下：
	1. 每一次可以合并相邻位置的两堆石子
	2. 每次合并的代价为所合并的两堆石子的重量之和
求出最小的合并代价。

样例 1:
输入: [3, 4, 3]
输出: 17

样例 2:
输入: [4, 1, 1, 4]
输出: 18
解释: 
  1. 合并第二堆和第三堆 => [4, 2, 4], score = 2
  2. 合并前两堆 => [6, 4]，score = 8
  3. 合并剩余的两堆 => [10], score = 18
'''

# python key:
class Solution:
    """
    @param A: An integer array
    @return: An integer
    最后合并的是[i,j]里的两堆（因为里面其他堆都已合并），以k为分隔，则枚举k，看看最后合并这
    两堆[i,k][k+1,j]时k要放什么位置，使得合并总分数(dp[i][j] + sums[i][j])最小；
    """
    def stoneGame(self, A):
        if not A or len(A) < 2:
            return 0
        n = len(A)
        dp = [[0 for j in range(n)] for i in range(n)]
        sums = [[0 for j in range(n)] for i in range(n)]
        for i in range(n - 1):
            for j in range(i, n):
                sums[i][j] = sums[i][j-1] + A[j]
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = float('inf')
                for k in range(i, j):
                    dp[i][j] = min(
                        dp[i][j],
                        dp[i][k] + dp[k+1][j] + sums[i][j]
                    )
        return dp[0][n-1]
