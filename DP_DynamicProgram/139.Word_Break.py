'''
🍊139. Word Break
Medium  https://leetcode.com/problems/word-break/
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.
 
Example 1:
Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false

Constraints:
	• 1 <= s.length <= 300
	• 1 <= wordDict.length <= 1000
	• 1 <= wordDict[i].length <= 20
	• s and wordDict[i] consist of only lowercase English letters.
	• All the strings of wordDict are unique.

'''

# python key I do:
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [False for _ in range(n + 1)]
        dp[0] = True # !!!!!!
        for i in range(n):
            for j in range(i + 1, n + 1):
                if s[i:j] in words and dp[i]:
                    dp[j] = True
        return dp[n]
        
# 或换个写法：
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
         # dp[i] means s[:i+1] can be segmented into words in the wordDicts 
         dp = [False for _ in range(n + 1)]
         dp[0] = True # !!!!!!
         for i in range(n):
             for j in range(i, n):
                 if dp[i] and s[i:j+1] in words:
                     dp[j + 1] = True
         return dp[-1]


