'''
🍏145. Binary Tree Postorder Traversal
Easy  https://leetcode.com/problems/binary-tree-postorder-traversal/
Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [1]
Output: [1]

Follow up: Recursive solution is trivial, could you do it iteratively?

Constraints:
	• The number of the nodes in the tree is in the range [0, 100].
	• -100 <= Node.val <= 100
'''

# python (non-recursion; iteratively)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        if not root:
            return res
        stack = [root]
        postorder = []
        while stack:
            node = stack.pop()
            postorder.append(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        while postorder:
            node = postorder.pop()
            res.append(node.val)
        return res



# python key iteratively

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        traversal, stack = [], [(root, False)]
        while stack:
            node, visited = stack.pop()
            if node:
                if visited:
                    # add to result if visited
                    traversal.append(node.val)
                else:
                    # post-order
                    stack.append((node, True))
                    stack.append((node.right, False))
                    stack.append((node.left, False))
        return traversal


# The 2nd uses modified preorder (right subtree first). Then reverse the result.
class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def postorderTraversal(self, root):
        traversal, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                # pre-order, right first
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        # reverse result
        return traversal[::-1]

