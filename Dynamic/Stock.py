class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Transaction fee
        if not prices:
            return 0
        
        # Best Profit when hold ONE stock
        hold = -prices[0]
        # Best profit when hold NO stock
        cash = 0

        for price in prices[1:]:
            # If currently hold => keep hold if cash - price < hold (if spent money)
            # If buy today when hold yesterday => change holding prices
            # Answer: if end today holding stock, what is the best prof
            hold = max(hold, cash - price)
            # Already in cash, and > if sell => stay the same
            # If execute the pair of buy-sell => what is the new profit
            cash = max(cash, hold + price - fee)

        return cash