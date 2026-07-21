class Solution:
    def trap(self, height: List[int]) -> int:
        max_l = height[0]
        max_r = height[-1]
        tot_water = 0
        l = 0
        r = len(height)-1
        while l <= r:           
            if max_l <= max_r:
                tot_water += max(max_l - height[l], 0)
                max_l = max(max_l, height[l])
                l += 1
            else:
                tot_water += max(max_r - height[r],0)
                max_r = max(max_r, height[r])
                r -= 1
        
        return tot_water