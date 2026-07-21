class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        cur_max = -float("inf")
        while l < r:
            min_h = min(heights[l], heights[r])
            area = (r-l) * min_h
            cur_max = max(cur_max, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return cur_max
        