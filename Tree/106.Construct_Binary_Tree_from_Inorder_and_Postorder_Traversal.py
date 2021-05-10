'''
106. Construct Binary Tree from Inorder and Postorder Traversal

Medium https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, construct and return the binary tree.
 
Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
	
Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]

Constraints:
	• 1 <= inorder.length <= 3000
	• postorder.length == inorder.length
	• -3000 <= inorder[i], postorder[i] <= 3000
	• inorder and postorder consist of unique values.
	• Each value of postorder also appears in inorder.
	• inorder is guaranteed to be the inorder traversal of the tree.
	• postorder is guaranteed to be the postorder traversal of the tree.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder or len(inorder) == 0 or len(postorder) == 0:
            return None
        iLen, pLen = len(inorder), len(postorder)
        return self.build(inorder, 0, iLen - 1, postorder, 0, pLen - 1)
    
    def build(self, inorder, iStart, iEnd, postorder, pStart, pEnd) -> TreeNode:
        if iStart > iEnd or pStart > pEnd:
            return None
        rootVal = postorder[pEnd]
        rootIdx = 0
        for i in range(iStart, iEnd + 1):
            if inorder[i] == rootVal:
                rootIdx = i
                break
        leftLen = rootIdx - iStart
        root = TreeNode(rootVal)
        root.left = self.build(inorder, iStart, rootIdx - 1, postorder, pStart, pStart + leftLen - 1)
        root.right = self.build(inorder, rootIdx + 1, iEnd, postorder, pStart + leftLen, pEnd - 1)
        return root
        
        
        
        
