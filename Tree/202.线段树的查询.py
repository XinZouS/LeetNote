'''
🍊202 · 线段树的查询
中等  https://www.lintcode.com/problem/202/
对于一个有n个数的整数数组，在对应的线段树中, 根节点所代表的区间为0-n-1, 每个节点有一个额外的属性max，值为该节点所代表的数组区间start到end内的最大值。
为SegmentTree设计一个 query 的方法，接受3个参数root, start和end，根据给定的线段树根，找出区间[start，end]中的最大值。
在做此题之前，请先完成 线段树构造 这道题目。

样例 1:
输入："[0,3,max=4][0,1,max=4][2,3,max=3][0,0,max=1][1,1,max=4][2,2,max=2][3,3,max=3]",1,2
输出：4
解释：
对于数组 [1, 4, 2, 3], 对应的线段树为 :
                         [0, 3, max=4]
	                 /             \
	          [0,1,max=4]        [2,3,max=3]
	          /         \        /         \
         [0,0,max=1] [1,1,max=4] [2,2,max=2], [3,3,max=3]
[1,2]区间最大值为4

样例 2:
输入："[0,3,max=4][0,1,max=4][2,3,max=3][0,0,max=1][1,1,max=4][2,2,max=2][3,3,max=3]",2,3
输出：3
解释：
对于数组 [1, 4, 2, 3], 对应的线段树为 :
                         [0, 3, max=4]
	                 /             \
	          [0,1,max=4]        [2,3,max=3]
	          /         \        /         \
	   [0,0,max=1] [1,1,max=4] [2,2,max=2], [3,3,max=3]
[2,3]区间最大值为3
'''


"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of segment tree.
    @param start: start value.
    @param end: end value.
    @return: The maximum number in the interval [start, end]
    """
    def query(self, root, start, end):
        if start > end or root == None:
            return -float('inf')
        #
        if root.start == start and root.end == end:
            return root.max
        #
        if root.left and end <= root.left.end:
            return self.query(root.left, start, end)
        if root.right and root.right.start <= start:
            return self.query(root.right, start, end)
        #
        l = self.query(root.left, start, root.left.end)
        r = self.query(root.right, root.right.start, end)
        return max(l, r)

