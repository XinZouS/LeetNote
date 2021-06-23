'''
🍏479 · 数组第二大数
简单  https://www.lintcode.com/problem/479/
在数组中找到第二大的数。
你可以假定至少有两个数字。
第二大的数是指降序数组中第二个数字。
例1：	        例2：
输入：[1,3,2,4]	输入：[1,1,2,2]
输出：3          输出：2
'''

# python key:
class Solution:
    """
    @param nums: An integer array
    @return: The second max number in the array.
    """
    def secondMax(self, nums):
        if not nums or len(nums) < 2:
            return 0
        first, second = None, None
        for n in nums:
            if first is None or first < n:
                second = first
                first = n
            elif second is None or second < n:
                second = n
        return second

