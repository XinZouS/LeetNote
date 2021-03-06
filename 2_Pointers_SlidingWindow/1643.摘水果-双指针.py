'''
ð1643 Â· ææ°´æ(åæé)

Thursday, July 1, 2021
3:16 PM

ä¸­ç­  https://www.lintcode.com/problem/1643/
å°çº¢å»æå­éæ°´æãæ2ä¸ªç¯®å­ï¼å¯ä»¥è£æ æ°ä¸ªæ°´æï¼ä½æ¯åªè½è£ä¸ç§æ°´æãä»ä»»æä½ç½®çæ å¼å§ï¼å¾å³éãéå°2ç§æåµéåºï¼1. éå°ç¬¬ä¸ç§æ°´æï¼æ²¡æç¯®å­å¯ä»¥æ¾äºï¼2. å°å¤´äºãè¿åå¯ä»¥éæçæå¤çæ°´æä¸ªæ°ãæ°´ææ°ç»ç¨arrè¡¨ç¤ºã
æ°ç»é¿åº¦ä¸è¶è¿100,000
æ ·ä¾ 1:
è¾å¥ï¼[1,2,1,3,4,3,5,1,2]
è¾åºï¼3
è§£éï¼
éæ©[1, 2, 1] æ [3, 4, 3]ã é¿åº¦æ¯3ã

æ ·ä¾ 2:
è¾å¥ï¼[1,2,1,2,1,2,1]
è¾åºï¼7
è§£éï¼
éæ© [1, 2, 1, 2, 1, 2, 1]ãé¿åº¦æ¯ 7ã
'''


class Solution:
    """
    @param arr: the arr
    @return: the length of the longset subarray
    """
    def pickFruits(self, arr):
        n = len(arr)
        if n < 3:
            return n
        l, r = 0, 0
        maxLen = 0
        have = dict()
        for r in range(n):
            have[arr[r]] = have.get(arr[r], 0) + 1
            while len(have) > 2 and l <= r and arr[l] in have:
                have[arr[l]] -= 1
                if have[arr[l]] == 0: # MUST del the 0 items for len compute
                    del have[arr[l]]
                l += 1
            if r - l + 1 > maxLen:
                maxLen = r - l + 1
                
        return maxLen


