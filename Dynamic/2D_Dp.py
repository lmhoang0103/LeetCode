class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # SubSeq = original delete character
        # Length 

        # dp[i][j] = LCS of text1[0:i] and text2[0:j]
        # If text1[i-1] == text2[j-1] => dp[i][j] = dp[i-1][j-1]+1
        # else dp[i][j] = max()

        m, n = len(text1), len(text2)
        dp = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] +1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # Subseq is the same
        # Need characters that is NOT in subseq for both str
        m, n = len(str1), len(str2)

        # LCS DP
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Reconstruct SCS
        i, j = m, n
        res = []

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] >= dp[i][j - 1]:
                res.append(str1[i - 1])
                i -= 1
            else:
                res.append(str2[j - 1])
                j -= 1

        # Remaining characters
        while i > 0:
            res.append(str1[i - 1])
            i -= 1
        while j > 0:
            res.append(str2[j - 1])
            j -= 1

        return "".join(reversed(res))
    
    class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # dp[i][j] numbers of ways s[:i] can form t[:j]
        # answer is dp[m][n]
        # if s[i] = t[j] -> dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        # if not: dp[i][j] = dp[i-1][j]
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            dp[i][0] = 1

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]

        return dp[m][n]
