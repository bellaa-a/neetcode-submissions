class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.nums = nums
        self.target = target
        self.res = []
        self.dfs([], 0, 0)
        return self.res


    def dfs(self, subset, subset_sum, start):
        for i in range(start, len(self.nums)):
            if subset_sum + self.nums[i] == self.target:
                self.res.append(subset + [self.nums[i]])
            elif subset_sum + self.nums[i] < self.target:
                self.dfs(subset + [self.nums[i]], subset_sum + self.nums[i], i)
            else:
                continue