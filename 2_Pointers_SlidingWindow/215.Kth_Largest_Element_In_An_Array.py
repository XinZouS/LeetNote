'''
215. Kth Largest Element in an Array
Medium  https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.
Note that it is the kth largest element in the sorted order, not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

class Solution:
	# using Quick select
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) < k or k < 1:
            return -1
        n = len(nums)
        left, right = 0, n - 1
        target, curr = n - k, -1
        while target != curr:
            l, r = left, right
            p, pv = r, nums[r]
            while l < r:
                while l < r and nums[l] <= pv: l += 1
                while l < r and nums[r] >= pv: r -= 1
                if nums[l] > nums[r]: 
                    nums[l], nums[r] = nums[r], nums[l]
            curr = l
            if nums[l] > nums[p]:
                nums[l], nums[p] = nums[p], nums[l]
            if l < target:
                left = l
            if r > target:
                right = r - 1
        return nums[curr]
        

