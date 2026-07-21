class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        start = {}
        for n in nums:
            if n-1 not in nums:
                start[n] = 1
        
        for key in start.keys():
            i = 1
            while key+i in nums:
                start[key] += 1
                i += 1
        max_length = 0
        for length in start.values():
            if length > max_length:
                max_length = length
        return max_length


        