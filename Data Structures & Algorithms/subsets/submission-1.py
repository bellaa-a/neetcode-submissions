class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums
        self.dfs(0, [])
        return self.res

    
    def dfs(self, i, subset):
        if i >= len(self.nums):
            self.res.append(subset)
            return
        self.dfs(i+1, subset)
        self.dfs(i+1, subset + [self.nums[i]])