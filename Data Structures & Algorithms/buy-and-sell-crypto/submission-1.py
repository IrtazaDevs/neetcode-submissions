class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_prof = 0
        min_buy = prices[0]

        for sell in prices:
            max_prof = max(max_prof, sell - min_buy)
            min_buy = min(min_buy, sell)
        return max_prof