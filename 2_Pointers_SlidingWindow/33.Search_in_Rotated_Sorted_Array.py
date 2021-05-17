'''
🍊33. Search in Rotated Sorted Array 在旋转后有序数组中找目标值
Medium  https://leetcode.com/problems/search-in-rotated-sorted-array/
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity. 
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''

# python key
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or len(nums) == 0:
            return -1
        l, r, t = 0, len(nums) - 1, target
        while l <= r:
            m = l + ((r - l) >> 1)
            if nums[m] == t:
                return m
            if nums[l] <= nums[m]: # left side in order
                if nums[l] <= t < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else: # right side in order
                if nums[m] < t <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return -1

