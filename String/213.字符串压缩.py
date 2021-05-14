'''
🍏213.字符串压缩
https://www.lintcode.com/problem/213/

设计一种方法，通过给重复字符计数来进行基本的字符串压缩。
例如，字符串 aabcccccaaa 可压缩为 a2b1c5a3 。而如果压缩后的字符数不小于原始的字符数，则返回原始的字符串。
可以假设字符串仅包括 a-z 的大/小写字母。
样例
Example 1:
Input: str = "aabcccccaaa"
Output: "a2b1c5a3"
Example 2:
Input: str = "aabbcc"
Output: "aabbcc"
'''
class Solution:

    def compress(self, originalString):
        n = len(originalString)
        if n < 3:
            return originalString
        l, r = 0, 0
        newStr = ''
        oldStr = originalString
        while r < n:
            while r < n and oldStr[l] == oldStr[r]:
                r += 1
            curLen = r - l
            newStr += '%s%i' % (oldStr[l], curLen)
            l = r
        return newStr if len(newStr) < len(oldStr) else oldStr

