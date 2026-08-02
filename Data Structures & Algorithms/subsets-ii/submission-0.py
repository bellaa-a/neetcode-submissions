class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.nums = sorted(nums)
        print(self.nums)
        self.res = []
        self.dfs(0, [])
        return self.res

    def dfs(self, i, subset):
        if i >= len(self.nums):
            self.res.append(subset)
            return
        same = 1
        while i+same < len(self.nums) and self.nums[i+same] == self.nums[i]:
            same += 1
        
        for k in range(same+1):
            self.dfs(i+same, subset + [self.nums[i]] * k)
