'''
🍊1643 · 摘水果(双指针)

Thursday, July 1, 2021
3:16 PM

中等  https://www.lintcode.com/problem/1643/
小红去果园采水果。有2个篮子，可以装无数个水果，但是只能装一种水果。从任意位置的树开始，往右采。遇到2种情况退出，1. 遇到第三种水果，没有篮子可以放了，2. 到头了。返回可以采摘的最多的水果个数。水果数组用arr表示。
数组长度不超过100,000
样例 1:
输入：[1,2,1,3,4,3,5,1,2]
输出：3
解释：
选择[1, 2, 1] 或 [3, 4, 3]。 长度是3。

样例 2:
输入：[1,2,1,2,1,2,1]
输出：7
解释：
选择 [1, 2, 1, 2, 1, 2, 1]。长度是 7。
'''


class Solution:
    """
    @param arr: the arr
    @return: the length of the longset subarray
    """
    def pickFruits(self, arr):
        n = len(arr)
        if n < 3:
            return n
        l, r = 0, 0
        maxLen = 0
        have = dict()
        for r in range(n):
            have[arr[r]] = have.get(arr[r], 0) + 1
            while len(have) > 2 and l <= r and arr[l] in have:
                have[arr[l]] -= 1
                if have[arr[l]] == 0: # MUST del the 0 items for len compute
                    del have[arr[l]]
                l += 1
            if r - l + 1 > maxLen:
                maxLen = r - l + 1
                
        return maxLen


