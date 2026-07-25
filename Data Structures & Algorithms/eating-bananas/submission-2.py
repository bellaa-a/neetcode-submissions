class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = 0
        l = 1
        r = max(piles)
        
        while l <= r:
            m = l + int((r-l)/2)
            hours = 0
            for p in piles:
                hours += int((p-1)/m)+1
            if hours <= h:
                res = m
                r = m-1
            else:
                l = m+1
        
        return res