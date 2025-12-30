class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        # dp-rc = dp-r-1c + dp-r-c-1
        # Scan for rock, if rock then dp-rc = dp-r-1c for example
        # DP[m-1][n-1] = DP[m-2][n-1] + DP[m-1][n-2]

        m = len(grid)
        n = len(grid[0])
        dp = [[0] * n for _ in range(m)]
        # For base, if  meets obstacle => can't reach
        if grid[m-1][n-1] == 1:
            return 0
        for i in range(n):
            if grid[0][i]  == 1:
                break
            dp[0][i] = 1
        
        for j in range(m):
            if grid[j][0]  == 1:
                break
            dp[j][0] = 1

        for r in range(1,m):
            for c in range(1,n):
                if grid[r][c] == 1:
                    continue
                dp[r][c] = dp[r-1][c] + dp[r][c-1]

        return dp[m-1][n-1] 