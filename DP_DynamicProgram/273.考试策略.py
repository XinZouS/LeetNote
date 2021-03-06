'''
ð273 Â· èè¯ç­ç¥
ä¸­ç­  https://www.lintcode.com/problem/273/
ä½ æä¸åºèè¯ï¼èè¯æ¶é´ä¸ºÂ 120 åéãèè¯æå¤éé¢ç®ï¼ä½ çä½ç­é¡ºåºä¸åéå¶ãå¯¹äºç¬¬Â iÂ éé¢ç®ï¼ä½ æä¸ç§ä¸åçç­ç¥å¯ä»¥éæ©ï¼
	1. ç´æ¥è·³è¿è¿éé¢ç®ï¼ä¸è±è´¹æ¶é´ï¼æ¬é¢å¾ 0 åã
	2. åªåè¿éé¢ç®ä¸é¨åï¼è±è´¹Â p[i]Â åéçæ¶é´ï¼æ¬é¢å¯ä»¥å¾å°Â part[i]Â åã
	3. åå®æ´éé¢ç®ï¼è±è´¹Â f[i]Â åéçæ¶é´ï¼æ¬é¢å¯ä»¥å¾å°Â full[i]Â åã
ä¾æ¬¡ç»å® 4 ä¸ªæ°ç»ï¼pï¼partï¼fï¼fullï¼è¯·ä½ è®¡ç®åºä½ æå¤è½å¾å°å¤å°åã
1 â¤ èè¯é¢ç®æ°é â¤ 200
æ¯éé¢ç®çè±è´¹æ¶é´ï¼1 â¤Â p[i]Â â¤Â f[i]Â â¤ 120
æ¯éé¢ç®çåæ°ï¼1 â¤Â part[i]Â â¤Â full[i]Â â¤ 100
æä»¬å°è¿è¡ä½ çä»£ç 20æ¬¡ï¼è¯·ç¡®è®¤ä¸è¦å¨å½æ°åæ¹ååæ°
æ ·ä¾1ï¼
è¾å¥æ ·ä¾ï¼p=[20,50,100,5], part=[20,30,60,3], f=[100,80,110,10], full=[60,55,88,6]
è¾åºæ ·ä¾ï¼94
æ ·ä¾è§£éï¼å¨ææåé¢éæ©ä¸­ï¼éæ©å®ææ´éç¬¬ 3 é¢åæ´éç¬¬ 4 é¢çå¾åæé«ãæ´éç¬¬ 3 é¢èæ¶ 110 åéå¾å° 88 åï¼æ´éç¬¬ 4 é¢èæ¶ 10 åéå¾å° 6 åï¼æ»å±èæ¶ 120 åéå¾å° 94 åã
æ ·ä¾2ï¼
è¾å¥æ ·ä¾ï¼p=[60,60], part=[30,30], f=[100,120], full=[40,60]
è¾åºæ ·ä¾ï¼60
æ ·ä¾è§£éï¼2 éé¢ç®é½åä¸é¨åååå®æ´éç¬¬ 2 é¢ï¼é½è½å¨èæ¶ 120 åéä¸å¾å°æé«ç 60 åã
'''

class Solution:
    """
    @param p: The time you choose to do part of the problem.
    @param part: The points you choose to do part of the problem.
    @param f: The time you choose to do the whole problem.
    @param full: The points you choose to do the whole problem.
    @return: Return the maximum number of points you can get.
    """
    def exam(self, p, part, f, full):
        n = len(p)
        if n < 1:
            return 0
        maxTime = 120
        # 1. dp[i][j] = ååiéé¢å¨jåéæ¶å¾åï¼dpä¸­ï¼ä¸å®ç¨å®¹éå jï¼ç¨ç©åå iï¼ä¸ç¶éè¯¯ç­æ¡ï¼
        dp = [[0 for j in range(maxTime + 1)] for i in range(n + 1)]

        # 2. init dp, å¶å®è¿ä¸ç¨ï¼ä¸é¢å·²å¨0äºï¼åè¿æéèªå·±è¦èèdpåå§ç¶æ
        for i in range(n):
            dp[i][0] = 0 # å0ä¸ªé¢å¾0å
        for j in range(maxTime + 1):
            dp[0][j] = 0 # è±0åéå¾0å

        # 3. search
        for i in range(1, n + 1):
            for j in range(1, maxTime + 1):
                dp[i][j] = dp[i - 1][j] # 3.1 skip current score

                if j < p[i - 1]: # 3.2 try do part
                    continue
                doPart = dp[i - 1][j - p[i - 1]] + part[i - 1]
                dp[i][j] = max(dp[i][j], doPart)
                if j < f[i - 1]: # 3.2 try do full
                    continue
                doFull = dp[i - 1][j - f[i - 1]] + full[i - 1]
                dp[i][j] = max(dp[i][j], doFull)
        return dp[n][120]


# python key æ»å¨æ°ç»ä¼åï¼ç´æ¥æ dpç i % 2 ï¼åç©åç i ä¸æ¨¡ï¼ä¸ç¶åéï¼
class Solution:
    """
    @param p: The time you choose to do part of the problem.
    @param part: The points you choose to do part of the problem.
    @param f: The time you choose to do the whole problem.
    @param full: The points you choose to do the whole problem.
    @return: Return the maximum number of points you can get.
    """
    def exam(self, p, part, f, full):
        n = len(p)
        if n < 1:
            return 0
        maxTime = 120
        dp = [[0 for j in range(maxTime + 1)] for i in range(2)]

        for i in range(1, n + 1):
            for j in range(1, maxTime + 1):
                dp[i % 2][j] = dp[(i - 1) % 2][j] # skip, so same score as i-1
                if j < p[i - 1]:
                    continue
                dp[i % 2][j] = max(dp[i % 2][j], dp[(i - 1) % 2][j - p[i - 1]] + part[i - 1])

                if j < f[i - 1]:
                    continue
                dp[i % 2][j] = max(dp[i % 2][j], dp[(i - 1) % 2][j - f[i - 1]] + full[i - 1])

        return dp[n % 2][maxTime]


