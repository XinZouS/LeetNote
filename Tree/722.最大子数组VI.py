'''
🍇722 · 最大子数组VI (Trie)
超难  https://www.lintcode.com/problem/722/
给出一个整数数组，找出异或值最大的子数组。
什么是异或:https://en.wikipedia.org/wiki/Exclusive_or
预期时间复杂度为O(n)
保证数组中的数字不超过2147483647

样例1
输入: [1, 2, 3, 4]
输出: 7
说明:
子数组[3, 4]有最大的异或值

样例2
输入: [8, 1, 2, 12, 7, 6]
输出: 15
说明:
子数组[1, 2, 12]有最大的异或值

样例3
输入: [4, 6]
输出: 6
说明:
子数组[6]有最大的异或值
'''

class Solution:

    class TrieNode:
        def __init__(self):
            self.sons = [None, None]
            self.num = 0
            self.isNum = False

        def insert(self, num):
            node = self
            for i in range(30, -1, -1):
                bit = (num >> i) & 1
                if not node.sons[bit]:
                    node.sons[bit] = Solution.TrieNode()
                node = node.sons[bit]
            node.num = num
            node.isNum = True

        def findNearest(self, num):
            node = self
            for i in range(30, -1, -1):
                bit = (num >> i) & 1
                if node.sons[bit - 1]:
                    node = node.sons[bit - 1]
                else:
                    node = node.sons[bit]
            return node.num

    """
    @param nums: the array
    @return: the max xor sum of the subarray in a given array
    """
    def maxXorSubarray(self, nums):
        n = len(nums)
        root = self.TrieNode()
        preXor = [0 for _ in range(n + 1)]
        for i in range(n):
            preXor[i + 1] = preXor[i] ^ nums[i]
        maxXor = 0
        for pXor in preXor:
            root.insert(pXor)

        for pXor in preXor:
            tmp = root.findNearest(pXor)
            maxXor = max(maxXor, pXor ^ tmp)
        return maxXor


