'''
🍎76. Minimum Window Substring

Hard  https://leetcode.com/problems/minimum-window-substring/
讲解： https://mp.weixin.qq.com/s/nJHIxQ2BbqhDv5jZ9NgXrQ
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".
Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.
 
Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:
Input: s = "a", t = "a"
Output: "a"

Constraints:
	• 1 <= s.length, t.length <= 105
	• s and t consist of English letters.
 
Follow up: Could you find an algorithm that runs in O(n) time?
'''

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ''
        minLen, minStart = float('inf'), 0
        window, need = dict(), dict()
        for c in t:
            need[c] = need.get(c, 0) + 1
        match = 0
        l, r = 0, 0
        while r < len(s):
            c1 = s[r]
            if c1 in need:
                window[c1] = window.get(c1, 0) + 1
                if window[c1] == need[c1]:
                    match += 1
            r += 1
            
            while match == len(need):
                if r - l < minLen:
                    minLen, minStart = r - l, l
                c2 = s[l]
                if c2 in window:
                    window[c2] -= 1
                    if window[c2] < need[c2]:
                        match -= 1
                l += 1
        return '' if minLen == float('inf') else s[minStart:minStart+minLen]
        
