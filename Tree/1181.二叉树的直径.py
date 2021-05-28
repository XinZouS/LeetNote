'''
🍏1181. 二叉树的直径
简单  https://www.lintcode.com/problem/1181/solution
给定一颗二叉树，您需要计算树的直径长度。 二叉树的直径是树中任意两个节点之间最长路径的长度。
两个节点之间的路径长度由它们之间的边数表示。
样例 1:
给定一棵二叉树 
          1
         / \
        2   3
       / \     
      4   5    
返回3, 这是路径[4,2,1,3] 或者 [5,2,1,3]的长度.
样例 2:
输入:[2,3,#,1]
输出:2
解释:
      2
    /
   3
 /
1

'''
# python key
class Solution:
    """
    @param root: a root of binary tree
    @return: return a integer
    """
    def diameterOfBinaryTree(self, root):
        self.maxPath = 0
        _ = self.dfs(root)
        return self.maxPath
    def dfs(self, root):
        if not root:
            return 0
        l = self.dfs(root.left)
        r = self.dfs(root.right)
        self.maxPath = max(self.maxPath, l + r)
        return max(l, r) + 1
