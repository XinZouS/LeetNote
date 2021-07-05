'''
🍎207 · 区间求和 II (线段树)
困难  https://www.lintcode.com/problem/207/
在类的构造函数中给一个整数数组, 实现两个方法 query(start, end) 和 modify(index, value):
	• 对于 query(start, end), 返回数组中下标 start 到 end 的 和。
	• 对于 modify(index, value),把数组中下标为 index 的数改为 value.
在做此题前，建议先完成以下三题：线段树的构造， 线段树的查询，以及线段树的修改。

样例1
输入:
[1,2,7,8,5]
[query(0,2),modify(0,4),query(0,1),modify(2,1),query(2,4)]
输出: [10,6,14]
说明:
给定数组 A = [1,2,7,8,5].
在query(0, 2)后, 1 + 2 + 7 = 10,
在modify(0, 4)后, 将 A[0] 修改为 4， A = [4,2,7,8,5].
在query(0, 1)后, 4 + 2 = 6.
在modify(2, 1)后, 将 A[2] 修改为 1，A = [4,2,1,8,5].
After query(2, 4), 1 + 8 + 5 = 14.

样例2
输入:
[1,2,3,4,5]
[query(0,0),query(1,2),quert(3,4)]
输出: [1,5,9]
说明:
1 = 1
2 + 3 = 5
4 + 5 = 9
挑战: query 和 modify的时间复杂度需要为O(logN).
'''

class Solution:
    #
    class TreeNode:
        def __init__(self, start, end, value = 0):
            self.start = start
            self.end = end
            self.value = value
            self.left = None
            self.right = None
    def buildTree(self, A, start, end):
        if start > end:
            return None
        if start == end:
            return Solution.TreeNode(start, end, A[start])
        mid = start + ((end - start) >> 1)
        root = Solution.TreeNode(start, end)
        root.left = self.buildTree(A, start, mid)
        root.right = self.buildTree(A, mid + 1, end)
        root.value += root.left.value if root.left else 0
        root.value += root.right.value if root.right else 0
        return root

    """
    @param: A: An integer array
    """
    def __init__(self, A):
        self.n = len(A)
        self.root = self.buildTree(A, 0, self.n - 1)

    """
    @param: start: An integer
    @param: end: An integer
    @return: The sum from start to end
    """
    def query(self, start, end):
        if start > end or not (0 <= start < self.n and 0 <= end < self.n):
            return 0
        return self.find(self.root, start, end)
    def find(self, root, start, end):
        if not root or start > end:
            return 0
        if root.start == start and root.end == end:
            return root.value
        #
        if root.left and root.left.start <= start and root.left.end >= end:
            return self.find(root.left, start, end)
        if root.right and root.right.start <= start and root.right.end >= end:
            return self.find(root.right, start, end)
        #
        sumL = self.find(root.left, start, root.left.end)
        sumR = self.find(root.right, root.right.start, end)
        return sumL + sumR
        
    """
    @param: index: An integer
    @param: value: An integer
    @return: nothing
    """
    def modify(self, index, value):
        if not (0 <= index < self.n):
            return
        self.root.value += self.modifyIn(self.root, index, value)
    
    # return the diff after modify
    def modifyIn(self, root, index, value) -> int:
        if not root:
            return 0
        if root.start == index and root.end == index:
            diff = value - root.value
            root.value = value
            return diff
        if root.left and root.left.start <= index <= root.left.end:
            diff = self.modifyIn(root.left, index, value)
            root.value += diff
            return diff
        if root.right and root.right.start <= index <= root.right.end:
            diff = self.modifyIn(root.right, index, value)
            root.value += diff
            return diff
        return 0
