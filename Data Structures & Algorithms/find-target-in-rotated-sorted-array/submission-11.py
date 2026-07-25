class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first = nums[0]

        l = 0
        r = len(nums)-1

        while l <= r:
            m = l + int((r-l)/2)
            if nums[m] == target:
                return m
            
            if nums[m] >= nums[l]: # left portion

                if nums[l] <= target and target < nums[m]:
                    r = m-1
                else:
                    l = m+1
            else: # right portion

                if nums[m] < target and target < nums[l]:
                    l = m+1
                else:
                    r = m-1
        
        return -1
            