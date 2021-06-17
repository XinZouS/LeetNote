'''
🍎❓1507. 和至少为 K 的最短子数组
困难  https://www.lintcode.com/problem/1507
返回 A 的最短的非空连续子数组的长度，该子数组的和至少为 K 。
如果没有和至少为 K 的非空子数组，返回 -1 。
	• 1 \leq A.length \leq 500001≤A.length≤50000
	• -10 ^ 5 \leq A[i] \leq 10 ^ 5−105≤A[i]≤105
	• 1 \leq K \leq 10 ^ 91≤K≤109
样例 1:
输入：A = [1], K = 1
输出：1

样例 2:
输入：A = [1,2], K = 4
输出：-1
'''
# python key:
class Solution:
    """
    @param A: the array
    @param K: sum
    @return: the length
    """
    def shortestSubarray(self, A, K):
        if not A:
            return -1
        n, cur = len(A), 0
        res = n + 1
        q = collections.deque()
        preSum = [0 for _ in range(n + 1)]
        for i in range(n):
            preSum[i + 1] = preSum[i] + A[i]
        #
        for i, preX in enumerate(preSum):
            while q and preX <= preSum[q[-1]]:
                q.pop()
            while q and preX - preSum[q[0]] >= K:
                res = min(res, i - q[0])
                q.popleft()
            q.append(i)
        return -1 if res == n + 1 else res

