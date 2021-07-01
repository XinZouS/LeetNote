'''
🍊75 · 寻找峰值(二分法)
中等  https://www.lintcode.com/problem/75
给定一个整数数组(size为n)，其具有以下特点：
	• 相邻位置的数字是不同的
	• A[0] < A[1] 并且 A[n - 2] > A[n - 1]
假定P是峰值的位置则满足A[P] > A[P-1]且A[P] > A[P+1]，返回数组中任意一个峰值的位置。
	• 数组保证至少存在一个峰
	• 如果数组存在多个峰，返回其中任意一个就行
	• 数组至少包含 3 个数

样例 1：
输入：A = [1, 2, 1, 3, 4, 5, 7, 6]
输出：1
解释：返回任意一个峰顶元素的下标，6也同样正确。

样例 2：
输入：A = [1,2,3,4,1]
输出：3
解释：返回峰顶元素的下标。
挑战
时间复杂度O (logN)O(logN)
'''

class Solution:
    """
    @param A: An integers array.
    @return: return any of peek positions.
    """
    def findPeak(self, A):
        n = len(A)
        l, r = 0, n - 1
        while l < r:
            m = l + ((r - l) >> 1)
            left, mid, right = A[m - 1], A[m], A[m + 1]
            if left < mid and right < mid:
                return m
            elif left > mid and right > mid:
                l = m + 1
            elif left < mid < right:
                l = m
            elif left > mid > right:
                r = m
        return l

