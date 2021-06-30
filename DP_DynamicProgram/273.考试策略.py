'''
🍊273 · 考试策略
中等  https://www.lintcode.com/problem/273/
你有一场考试，考试时间为 120 分钟。考试有多道题目，你的作答顺序不受限制。对于第 i 道题目，你有三种不同的策略可以选择：
	1. 直接跳过这道题目，不花费时间，本题得 0 分。
	2. 只做这道题目一部分，花费 p[i] 分钟的时间，本题可以得到 part[i] 分。
	3. 做完整道题目，花费 f[i] 分钟的时间，本题可以得到 full[i] 分。
依次给定 4 个数组：p，part，f，full，请你计算出你最多能得到多少分。
1 ≤ 考试题目数量 ≤ 200
每道题目的花费时间：1 ≤ p[i] ≤ f[i] ≤ 120
每道题目的分数：1 ≤ part[i] ≤ full[i] ≤ 100
我们将运行你的代码20次，请确认不要在函数内改变参数
样例1：
输入样例：p=[20,50,100,5], part=[20,30,60,3], f=[100,80,110,10], full=[60,55,88,6]
输出样例：94
样例解释：在所有做题选择中，选择完成整道第 3 题和整道第 4 题的得分最高。整道第 3 题耗时 110 分钟得到 88 分，整道第 4 题耗时 10 分钟得到 6 分，总共耗时 120 分钟得到 94 分。
样例2：
输入样例：p=[60,60], part=[30,30], f=[100,120], full=[40,60]
输出样例：60
样例解释：2 道题目都做一部分和做完整道第 2 题，都能在耗时 120 分钟下得到最高的 60 分。
'''

class Solution:
    """
    @param p: The time you choose to do part of the problem.
    @param part: The points you choose to do part of the problem.
    @param f: The time you choose to do the whole problem.
    @param full: The points you choose to do the whole problem.
    @return: Return the maximum number of points you can get.
    """
    def exam(self, p, part, f, full):
        n = len(p)
        if n < 1:
            return 0
        maxTime = 120
        # 1. dp[i][j] = 做前i道题在j分钟时得分（dp中，一定用容量做 j，用物品做 i，不然错误答案）
        dp = [[0 for j in range(maxTime + 1)] for i in range(n + 1)]

        # 2. init dp, 其实这不用，上面已全0了，写这提醒自己要考虑dp初始状态
        for i in range(n):
            dp[i][0] = 0 # 做0个题得0分
        for j in range(maxTime + 1):
            dp[0][j] = 0 # 花0分钟得0分

        # 3. search
        for i in range(1, n + 1):
            for j in range(1, maxTime + 1):
                dp[i][j] = dp[i - 1][j] # 3.1 skip current score

                if j < p[i - 1]: # 3.2 try do part
                    continue
                doPart = dp[i - 1][j - p[i - 1]] + part[i - 1]
                dp[i][j] = max(dp[i][j], doPart)
                if j < f[i - 1]: # 3.2 try do full
                    continue
                doFull = dp[i - 1][j - f[i - 1]] + full[i - 1]
                dp[i][j] = max(dp[i][j], doFull)
        return dp[n][120]


# python key 滚动数组优化：直接把 dp的 i % 2 （取物品的 i 不模！不然取错）
class Solution:
    """
    @param p: The time you choose to do part of the problem.
    @param part: The points you choose to do part of the problem.
    @param f: The time you choose to do the whole problem.
    @param full: The points you choose to do the whole problem.
    @return: Return the maximum number of points you can get.
    """
    def exam(self, p, part, f, full):
        n = len(p)
        if n < 1:
            return 0
        maxTime = 120
        dp = [[0 for j in range(maxTime + 1)] for i in range(2)]

        for i in range(1, n + 1):
            for j in range(1, maxTime + 1):
                dp[i % 2][j] = dp[(i - 1) % 2][j] # skip, so same score as i-1
                if j < p[i - 1]:
                    continue
                dp[i % 2][j] = max(dp[i % 2][j], dp[(i - 1) % 2][j - p[i - 1]] + part[i - 1])

                if j < f[i - 1]:
                    continue
                dp[i % 2][j] = max(dp[i % 2][j], dp[(i - 1) % 2][j - f[i - 1]] + full[i - 1])

        return dp[n % 2][maxTime]


