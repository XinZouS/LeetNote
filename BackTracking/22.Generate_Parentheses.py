'''
22. Generate Parentheses

Medium  https://leetcode.com/problems/generate-parentheses/
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses. 

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:
Input: n = 1
Output: ["()"]
 
Constraints:
1 <= n <= 8

'''

# python using n-1: 24 ms, faster than 99.09s

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        if n < 1:
            return self.res
        self.find(n, n, '')
        return self.res
    
    def find(self, l: int, r: int, cur: str):
        if l < 0: return
        if r == 0:
            self.res.append(cur)
            return
        if l > 0:
            self.find(l-1, r, cur + '(')
        if r > l:
            self.find(l, r-1, cur + ')')

