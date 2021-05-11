'''
🍏167. Two Sum II - Input array is sorted

Easy  https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
Given an array of integers numbers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
Return the indices of the two numbers (1-indexed) as an integer array answer of size 2, where 1 <= answer[0] < answer[1] <= numbers.length.
You may assume that each input would have exactly one solution and you may not use the same element twice. 
Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

Example 2:
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Example 3:
Input: numbers = [-1,0], target = -1
Output: [1,2]
Constraints:
	• 2 <= numbers.length <= 3 * 104
	• -1000 <= numbers[i] <= 1000
	• numbers is sorted in increasing order.
	• -1000 <= target <= 1000
Only one valid answer exists.
'''

# python:  binary search
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n):
            need = target - numbers[i]
            t = self.find(need, i + 1, numbers)
            if t >= 0:
                return [i + 1, t + 1]
        return []
    
    def find(self, target: int, start: int, numbers) -> int:
        l, r = start, len(numbers) - 1
        while l <= r:
            m = l + ((r - l) >> 1)
            if numbers[m] == target:
                return m
            if numbers[m] < target:
                l = m + 1
            else:
                r = m - 1
        return -1


# python keys:  2-pointer, dict, binary search
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/discuss/51249/Python-different-solutions-(two-pointer-dictionary-binary-search).

	# two-pointer
	def twoSum1(self, numbers, target):
	    l, r = 0, len(numbers)-1
	    while l < r:
	        s = numbers[l] + numbers[r]
	        if s == target:
	            return [l+1, r+1]
	        elif s < target:
	            l += 1
	        else:
	            r -= 1
	 
	# dictionary           
	def twoSum2(self, numbers, target):
	    dic = {}
	    for i, num in enumerate(numbers):
	        if target-num in dic:
	            return [dic[target-num]+1, i+1]
	        dic[num] = i
	 
	# binary search        
	def twoSum(self, numbers, target):
	    for i in xrange(len(numbers)):
	        l, r = i+1, len(numbers)-1
	        tmp = target - numbers[i]
	        while l <= r:
	            mid = l + (r-l)//2
	            if numbers[mid] == tmp:
	                return [i+1, mid+1]
	            elif numbers[mid] < tmp:
	                l = mid+1
	            else:
	                r = mid-1


