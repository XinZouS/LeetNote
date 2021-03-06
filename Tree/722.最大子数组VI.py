'''
ð722 Â· æå¤§å­æ°ç»VI (Trie)
è¶é¾  https://www.lintcode.com/problem/722/
ç»åºä¸ä¸ªæ´æ°æ°ç»ï¼æ¾åºå¼æå¼æå¤§çå­æ°ç»ã
ä»ä¹æ¯å¼æ:https://en.wikipedia.org/wiki/Exclusive_or
é¢ææ¶é´å¤æåº¦ä¸ºO(n)
ä¿è¯æ°ç»ä¸­çæ°å­ä¸è¶è¿2147483647

æ ·ä¾1
è¾å¥: [1, 2, 3, 4]
è¾åº: 7
è¯´æ:
å­æ°ç»[3, 4]ææå¤§çå¼æå¼

æ ·ä¾2
è¾å¥: [8, 1, 2, 12, 7, 6]
è¾åº: 15
è¯´æ:
å­æ°ç»[1, 2, 12]ææå¤§çå¼æå¼

æ ·ä¾3
è¾å¥: [4, 6]
è¾åº: 6
è¯´æ:
å­æ°ç»[6]ææå¤§çå¼æå¼
'''

class Solution:

    class TrieNode:
        def __init__(self):
            self.sons = [None, None]
            self.num = 0
            self.isNum = False

        def insert(self, num):
            node = self
            for i in range(30, -1, -1):
                bit = (num >> i) & 1
                if not node.sons[bit]:
                    node.sons[bit] = Solution.TrieNode()
                node = node.sons[bit]
            node.num = num
            node.isNum = True

        def findNearest(self, num):
            node = self
            for i in range(30, -1, -1):
                bit = (num >> i) & 1
                if node.sons[bit - 1]:
                    node = node.sons[bit - 1]
                else:
                    node = node.sons[bit]
            return node.num

    """
    @param nums: the array
    @return: the max xor sum of the subarray in a given array
    """
    def maxXorSubarray(self, nums):
        n = len(nums)
        root = self.TrieNode()
        preXor = [0 for _ in range(n + 1)]
        for i in range(n):
            preXor[i + 1] = preXor[i] ^ nums[i]
        maxXor = 0
        for pXor in preXor:
            root.insert(pXor)

        for pXor in preXor:
            tmp = root.findNearest(pXor)
            maxXor = max(maxXor, pXor ^ tmp)
        return maxXor


