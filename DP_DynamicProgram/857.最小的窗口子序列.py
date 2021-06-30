'''
🍎857 · 最小的窗口子序列
困难  https://www.lintcode.com/problem/857/
给定字符串S和T，在字符串S中找到最小(连续的)子字符串W（窗口），使得T是W的子序列。
如果S中没有包含T中的所有字符的窗口，则返回空字符串""。如果有多个这样的最小长度窗口，则返回一个起点编号最小的。
	• 输入中的所有字符串只包含小写字母。
	• S的长度范围在[1, 20000]。
	• T的长度范围在[1, 100]。
样例 1:
输入：S="jmeqksfrsdcmsiwvaovztaqenprpvnbstl"，T="u"
输出：""
解释： 无法匹配

样例 2:
输入：S = "abcdebdde"， T = "bde"
输出："bcde"
解释："bcde"是答案，"deb"不是一个较小的窗口，因为窗口中的T元素必须按顺序发生。
'''

class Solution:
    """
    @param S: a string
    @param T: a string
    @return: the minimum substring of S
    """
    def minWindow(self, S, T):
        lenS, lenT = len(S), len(T)
        if lenS == 0 or lenT == 0:
            return 0
        dp = [[0 for j in range(lenT +1)] for i in range(lenS + 1)]
        minStart, minLen = lenS, lenS

        for i in range(1, lenS + 1):
            for j in range(1, lenT + 1):
                if S[i - 1] == T[j - 1]:
                    if j == 1:
                        dp[i][j] = i # start of substring
                    else:
                        dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]

            # take note for the result:
            if dp[i][lenT] != 0:
                if i - dp[i][lenT] + 1 < minLen:
                    minLen = i - dp[i][lenT] + 1
                    minStart = dp[i][lenT] - 1

        return '' if minStart == lenS else S[minStart: minStart + minLen]


