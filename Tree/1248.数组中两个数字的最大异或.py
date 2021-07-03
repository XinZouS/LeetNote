'''
🍊1248 · 数组中两个数字的最大异或

中等  https://www.lintcode.com/problem/1248/
给定一个非空数组，a0，a1，a2，…，an-1，其中 0 ≤ ai < 2^31。
找出 ai XOR aj的最大结果，其中 0 ≤ i, j < n。

样例1
输入：[3, 10, 5, 25, 2, 8]
输出：28
说明：最大的结果为 5 ^ 25 = 28

样例2
输入：[2,4]
输出：6

挑战: 你能在 O(n) 时间内解决吗？
'''

class Solution:
    class TreeNode:
        def __init__(self):
            self.sons = [None, None]
            self.isNum = False
            self.num = 0
        def insert(self, num):
            node = self
            for i in range(30, -1, -1):
                bit = (num >> i) & 1
                if not node.sons[bit]:
                    node.sons[bit] = Solution.TreeNode()
                node = node.sons[bit]
            node.isNum = True
            node.num = num
        def get_nearest_num(self, num):
            node = self
            for i in range(30, -1, -1):
                bit = (num >> i) & 1
                if node.sons[1 - bit]:
                    node = node.sons[1 - bit]
                else:
                    node = node.sons[bit]
            return node.num
            
    """
    @param nums: 
    @return: the maximum result of ai XOR aj, where 0 ≤ i, j < n
    """
    def findMaximumXOR(self, nums):
        root = self.TreeNode()
        for num in nums:
            root.insert(num)
        max_xor = 0
        for num in nums:
            tmp = root.get_nearest_num(num)
            max_xor = max(max_xor, num ^ tmp)
        return max_xor

