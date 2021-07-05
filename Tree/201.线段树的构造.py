'''
🍊201 · 线段树的构造
中等  https://www.lintcode.com/problem/201/
线段树是一棵二叉树，他的每个节点包含了两个额外的属性start和end用于表示该节点所代表的区间。start和end都是整数，并按照如下的方式赋值:
	• 根节点的 start 和 end 由 build 方法所给出。
	• 对于节点 A 的左儿子，有 start=A.start, end=(A.start + A.end) / 2。
	• 对于节点 A 的右儿子，有 start=(A.start + A.end) / 2 + 1, end=A.end。
	• 如果 start 等于 end, 那么该节点是叶子节点，不再有左右儿子。
实现一个 build 方法，接受 start 和 end 作为参数, 然后构造一个代表区间 [start, end] 的线段树，返回这棵线段树的根。
线段树(又称区间树), 是一种高级数据结构，他可以支持这样的一些操作:
	• 查找给定的点包含在了哪些区间内
	• 查找给定的区间包含了哪些点
见百科：
线段树
区间树

样例 1:
输入：[1,4]
输出："[1,4][1,2][3,4][1,1][2,2][3,3][4,4]"
解释：
	               [1,  4]
	             /        \
	      [1,  2]           [3, 4]
	      /     \           /     \
	   [1, 1]  [2, 2]     [3, 3]  [4, 4]

样例 2:
输入：[1,6]
输出："[1,6][1,3][4,6][1,2][3,3][4,5][6,6][1,1][2,2][4,4][5,5]"
解释：
	       [1,  6]
             /        \
      [1,  3]           [4,  6]
      /     \           /     \
   [1, 2]  [3,3]     [4, 5]   [6,6]
   /    \           /     \
[1,1]   [2,2]     [4,4]   [5,5]

'''


"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = start, end
        self.left, self.right = None, None
"""

class Solution:
    """
    @param: start: start value.
    @param: end: end value.
    @return: The root of Segment Tree.
    """
    def build(self, start, end):
        if start > end:
            return None
        if start == end:
            return SegmentTreeNode(start, end)
        mid = start + ((end - start) >> 1)
        root = SegmentTreeNode(start, end)
        root.left = self.build(start, mid)
        root.right = self.build(mid + 1, end)
        return root

