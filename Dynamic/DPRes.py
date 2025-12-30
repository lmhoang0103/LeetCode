class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Dynamic Programming the target itself
        # dp[x] = how many ways to make x

        
        dp = defaultdict(int)
        # Before using any number, there are exactly 1 ways to have 0
        dp[0] = 1

        for num in nums:
            nxt = defaultdict(int)
            # Have to have nxt, otherwise will mutate dictionary while loop through it
            for s, cnt in dp.items():
                nxt[s + num] += cnt
                nxt[s - num] += cnt
            dp = nxt

        return dp[target]
    

    class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # dp[x]  = number of ways to make sum x using the coins so far been processed
        dp = [0] * (amount+1)
        dp[0] = 1

        for coin in coins:
            # Count what sum can be made using this coin
            # Low -> high => Can use a coin multiple times
            for x in range(coin, amount+1):
                dp[x] += dp[x-coin]

        return dp[amount]