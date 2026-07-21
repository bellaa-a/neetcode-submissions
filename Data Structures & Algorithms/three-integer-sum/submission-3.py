class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        targets = [0] * len(nums)
        result = []
        prev_target = float('inf')
        prev_l = float('inf')
        prev_r = float('inf')
        for i in range(len(nums)):
            targets[i] = -nums[i]

        for i in range(len(nums)):
            target = targets[i]
            if target == prev_target:
                continue
            prev_target = target
            needs = [-1000] * len(nums)
            l = i+1
            r = len(nums)-1
            while l < r:
                val = nums[l] + nums[r]
                if val < target:
                    l += 1
                elif val > target:
                    r -= 1
                else:
                    if nums[l] != prev_l or nums[r] != prev_r:
                        result.append([-target, nums[l], nums[r]])
                        prev_l = nums[l]
                        prev_r = nums[r]
                    l += 1
                    r -= 1  
        return result
        