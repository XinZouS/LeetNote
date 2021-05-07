'''
287. Find the Duplicate Number
Medium  https://leetcode.com/problems/find-the-duplicate-number/

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [1,1]
Output: 1
Example 4:

Input: nums = [1,1,2]
Output: 1
'''

# python key:

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while 1:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                slow = 0
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow # MUST slow, NOT nums[slow]
        return -1


# Approach 2: Set, but space O(n) not good

class Solution_2:
    def findDuplicate(self, nums: List[int]) -> int:
        finded = set()
        for x in nums:
            if x in finded:
                return x
            finded.add(x)
        return -1

