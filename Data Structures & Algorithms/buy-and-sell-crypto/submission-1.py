class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_min = prices[0]
        OPT = [0] * len(prices)

        for i in range(1, len(prices)):
            OPT[i] = max(prices[i] - cur_min, OPT[i-1])
            cur_min = min(cur_min, prices[i])
        
        return max(OPT)