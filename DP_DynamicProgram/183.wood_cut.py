'''
🍎183. 木材加工
困难  https://www.lintcode.com/problem/183/
有一些原木，现在想把这些木头切割成一些长度相同的小段木头，需要得到的小段的数目至少为 k。给定L和k，你需要计算能够得到的小段木头的最大长度。
木头长度的单位是厘米。原木的长度都是正整数，我们要求切割得到的小段木头的长度也要求是整数。无法切出要求至少 k 段的,则返回 0 即可。

样例 1
输入:
L = [232, 124, 456]
k = 7
输出: 114
Explanation: 我们可以把它分成114cm的7段，而115cm不可以

样例 2
输入:
L = [1, 2, 3]
k = 7
输出: 0
说明:很显然我们不能按照题目要求完成。

挑战
O(n log Len), Len为 n 段原木中最大的长度

'''

# python key
class Solution:
    def woodCut(self, L, k):
        if not L:
            return 0
        l, r = 1, max(L) + 1
        while l < r:
            m = l + ((r - l) >> 1)
            if self.nPiecesByLength(L, m) >= k:
                l = m + 1
            else:
                r = m
        l -= 1
        if l > 0 and self.nPiecesByLength(L, l) >= k:
            return l 
        return 0
        
    def nPiecesByLength(self, L, length):
        return sum(item // length for item in L)
        
    # !!! 不能用这个了，不然WA in case: [2147483644,2147483645,2147483646,2147483647] k=4
    def isCutable(self, cutLen, k, L) -> bool:
        for wood in L:
            k -= wood // cutLen
        return k <= 0

