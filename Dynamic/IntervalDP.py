class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Burst Balloons
        # Burst balloons i => get (i-1)i(i+1) coin (out of bound == 1)
        # After burst, REMOVE the ballon

        # Interval DP
        # Which to pop last

        # Add boundary
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[l][r]: best ans when pop between range l->r
        # if k is the last to pop in range l->r => the last is nums[l] * nums[k] * nums[r]
        # Sub problem: max(dp[l][k] + dp[k][r]) for ALL k between l and r
        dp = [[0] * n for _ in range(n)]
        # Slowly extend l-r range, build bigger problem from smaller
        for length in range(2, n):              # interval size
            for l in range(0, n - length):
                r = l + length
                for k in range(l + 1, r):
                    dp[l][r] = max(
                        dp[l][r],
                        dp[l][k] + dp[k][r] + nums[l] * nums[k] * nums[r]
                    )

        return dp[0][n - 1]
    

    class Solution:
    def minCut(self, s: str) -> int:
        # Palindrom Partitioning 2
        # Build big from small
        # pal[i][j] = True if s[i][j] is palindrom
            # Smaller problem: 1 char, 2 char
            # Longer?: if INSIDE is pal and s[i] = s[j]
        
        # dp[i] = min cut for s[0:i+1]
            # if s[:i+1] pal => 0 cut
        
        n = len(s)

        # pal[i][j] = s[i:j+1] is palindrome
        pal = [[False]*n for _ in range(n)]

        for i in range(n):
            pal[i][i] = True

        for length in range(2, n+1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2 or pal[i+1][j-1]:
                        pal[i][j] = True

        dp = [float('inf')] * n

        for i in range(n):
            if pal[0][i]:
                dp[i] = 0
            else:
                for j in range(1, i+1):
                    if pal[j][i]:
                        dp[i] = min(dp[i], dp[j-1] + 1)

        return dp[-1]