'''
105. Construct Binary Tree from Preorder and Inorder Traversal
Medium  https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
讲解： https://mp.weixin.qq.com/s?__biz=MzAxODQxMDM0Mw==&mid=2247487270&idx=1&sn=2f7ad74aabc88b53d94012ceccbe51be
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.
Example 1:	
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]

Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]
 
Constraints:
	• 1 <= preorder.length <= 3000
	• inorder.length == preorder.length
	• -3000 <= preorder[i], inorder[i] <= 3000
	• preorder and inorder consist of unique values.
	• Each value of inorder also appears in preorder.
	• preorder is guaranteed to be the preorder traversal of the tree.
	• inorder is guaranteed to be the inorder traversal of the tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder or len(preorder) == 0 or len(inorder) == 0:
            return None
        pLen, iLen = len(preorder), len(inorder)
        return self.build(preorder, 0, pLen - 1, inorder, 0, iLen - 1)
    
    def build(self, preorder, pStart, pEnd, inorder, iStart, iEnd) -> TreeNode:
        if pStart > pEnd or iStart > iEnd:
            return None
        rootVal = preorder[pStart]
        rootIdx = 0
        for i in range(iStart, iEnd + 1):
            if inorder[i] == rootVal:
                rootIdx = i
                break
        leftLen = rootIdx - iStart
        root = TreeNode(rootVal)
        root.left = self.build(preorder, pStart + 1, pStart + leftLen, inorder, iStart, rootIdx - 1)
        root.right = self.build(preorder, pStart + leftLen + 1, pEnd, inorder, rootIdx + 1, iEnd)
        return root
        
        

