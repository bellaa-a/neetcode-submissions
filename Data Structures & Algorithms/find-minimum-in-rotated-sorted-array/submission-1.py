class Solution:
    def findMin(self, nums: List[int]) -> int:
        first = nums[0]
        res = 0
        if first <= nums[-1]:
            return first
        
        l = 1
        r = len(nums)-1
        while l <= r:
            m = l + int((r-l)/2)
            if nums[m] > first:
                l = m+1
            else:
                res = nums[m]
                r = m-1

        return res