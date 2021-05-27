'''
1850. 捡苹果(隔板法)

中等  https://www.lintcode.com/problem/1850/
Alice 和 Bob 在一个漂亮的果园里面工作，果园里面有N棵苹果树排成了一排，这些苹果树被标记成1 - N号。 Alice 计划收集连续的K棵苹果树上面的所有苹果，Bob 计划收集连续的L棵苹果树上面的所有苹果。 他们希望选择不相交的部分（一个由 Alice 的K树组成，另一个由鲍勃 Bob 的L树组成），以免相互干扰。你应该返回他们可以收集的最大数量的苹果。
	• N 是整数且在以下范围内：[2，600]
	• K 和 L 都是整数且在以下范围内：[1，N-1]
	• 数组A的每个元素都是以下范围内的整数：[1，500]
示例 1:
输入:
A = [6, 1, 4, 6, 3, 2, 7, 4]
K = 3
L = 2
输出: 24
解释：
因为Alice 可以选择3-5颗树然后摘到4 + 6 + 3 = 13 个苹果， Bob可以选择7-8棵树然后摘到7 + 4 = 11个苹果，因此他们可以收集到13 + 11 = 24。

示例 2:
输入:
A = [10, 19, 15]
K = 2
L = 2
输出: -1
解释：
因为对于 Alice 和 Bob 不能选择两个互不重合的区间。

'''
# python key
class Solution:
    """
    @param A: a list of integer
    @param K: a integer
    @param L: a integer
    @return: return the maximum number of apples that they can collect.
    """
    def PickApples(self, A, K, L):
        if not A:
            return 0
        n = len(A)
        if K + L > n:
            return -1
        minZone = min(K, L)
        maxSum = -1
        for i in range(minZone, n - minZone):
            left_K  = self.pick(A, 0, i, K)
            right_L = self.pick(A, i, n, L)
            left_L  = self.pick(A, 0, i, L)
            right_K = self.pick(A, i, n, K)
            if left_K > 0 and right_L > 0:
                maxSum = max(maxSum, left_K + right_L)
            if left_L > 0 and right_K > 0:
                maxSum = max(maxSum, left_L + right_K)
        return maxSum
        
    def pick(self, A, start, end, zoneLen):
        if end - start < zoneLen:
            return -1
        maxSum, curSum = 0, 0
        l, r = start, start + zoneLen
        for i in range(l, r):
            curSum += A[i]
        maxSum = curSum # MUST update maxSum before loop, bcz zoneLen may be 1 !!!
        while r < end:
            curSum -= A[l]
            curSum += A[r]
            maxSum = max(maxSum, curSum)
            l += 1
            r += 1
        return maxSum

