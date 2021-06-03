'''
🍊416. Partition Equal Subset Sum

Medium  https://leetcode.com/problems/partition-equal-subset-sum/
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
Example 1:	Example 2:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].	Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 Constraints:
	• 1 <= nums.length <= 200
	• 1 <= nums[i] <= 100
'''

# python key
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return True
        sums = sum(nums)
        if sums % 2 != 0: return False # 总量为奇数时，不可能分为2个相等子集
        sums = sums >> 1 # = sums // 2
        n = len(nums)
        # 用前 i 个物品，是否能装满容量 j 的空间，dp[i][j] =True/False
        dp = [[False for j in range(sums + 1)] for i in range(n + 1)]
        
        for i in range(n + 1): # 空间为0时，什么 i 物品都能ok？
            dp[i][0] = True
        
        for i in range(1, n + 1):
            for j in range(1, sums + 1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    # 第i个物品，放入or不放，取决于 i-1 时的空间 j，或 j-nums[i-1]
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]
        return dp[n][sums]

