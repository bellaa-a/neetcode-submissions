class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for num in nums:
            if num in counts.keys():
                return True
            counts[num] = 1
                
        return False
