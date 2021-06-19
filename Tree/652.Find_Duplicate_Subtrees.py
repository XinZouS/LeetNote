'''
🍊652.Find Duplicate Subtrees
Medium  https://leetcode.com/problems/find-duplicate-subtrees/
Given the root of a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees, you only need to return the root node of any one of them.
Two trees are duplicate if they have the same structure with the same node values.
 
Example 1:

Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:

Input: root = [2,1,1]
Output: [[1]]
Example 3:

Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
Constraints:
        • The number of the nodes in the tree will be in the range [1, 10^4]
        • -200 <= Node.val <= 200

'''


# python key: I did 56 ms, faster than 90.91% 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        self.result = []
        if not root:
            return self.result
        self.str2root = dict()
        self.postOrder(root)
        return self.result
        
    def postOrder(self, root) -> str:
        if not root:
            return '#'
        l = self.postOrder(root.left)
        r = self.postOrder(root.right)
        curStr = '%i,%s,%s' % (root.val, l, r)
        self.str2root[curStr] = self.str2root.get(curStr, 0) + 1
        if self.str2root[curStr] == 2:
            self.result.append(root)
        return curStr

# python key 2:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root):
        def trv(root):
            if not root: return "null"
            struct = "%s,%s,%s" % (str(root.val), trv(root.left), trv(root.right))
            nodes[struct].append(root)
            return struct
        
        nodes = collections.defaultdict(list)
        trv(root)
        return [nodes[struct][0] for struct in nodes if len(nodes[struct]) > 1]        
        



