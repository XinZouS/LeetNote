'''
5. Longest Palindromic Substring
Medium

Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: s = "cbbd"
Output: "bb"

Example 3:
Input: s = "a"
Output: "a"

Example 4:
Input: s = "ac"
Output: "a"

Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters (lower-case and/or upper-case),

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.n = len(s)
        if self.n < 2:
            return s
        res = ''
        self.s = s
        for i in range(1, self.n):
            s1 = self.find(i, i)
            s2 = self.find(i-1, i)
            if len(s1) > len(res):
                res = s1
            if len(s2) > len(res):
                res = s2
        return res
    
    def find(self, a, b) -> str:
        while a >= 0 and b < self.n and self.s[a] == self.s[b]:
            a -= 1
            b += 1
        return self.s[a+1:b]
        
        

