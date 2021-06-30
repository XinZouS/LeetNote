'''
🍊1444 · 染色问题
中等  https://www.lintcode.com/problem/1444/
有一个圆形，分成n个扇形，用m种颜色给每个扇形染色，相邻扇形颜色不能相同。求方案总数。
	• 不考虑对称性。
	• 由于这个数可能很大，因此只需返回方案数模1e9 + 7。
	• 1 ≤ n ≤ 105
	• 1 ≤ m ≤ 105
样例1：
输入：n = 2，m = 3
输出：6
解释：一个圆划分为 2 个扇形，用 3 种颜色上色方案有“黑红，黑白，白红，白黑，红白，红黑”6 种。

样例 2：
输入：n = 3，m = 2
输出：0
解释：一个圆划分为 3 个扇形，用 2 种颜色上色，无论怎么上色，都没法保证相邻的颜色不同。  
'''

class Solution:
    """
    @param n: the number of sectors
    @param m: the number of colors
    @return: The total number of plans.
    """
    def getCount(self, n, m):
        if 0 <= n <= 1:
            return 0 if n == 0 else m
        MOD = 10 ** 9 + 7 # 1e9 + 7
        # 前n个格子在m种颜色下的方案总数
        dp = [0 for i in range(n + 3)] ###
        dp[1] = m
        dp[2] = m * (m - 1) % MOD
        dp[3] = m * (m - 1) * (m - 2) % MOD
        for i in range(4, n + 1):
            dp[i] += dp[i-1] * (m - 2)
            dp[i] %= MOD
            dp[i] += dp[i-2] * (m - 1)
            dp[i] %= MOD
        return dp[n]
