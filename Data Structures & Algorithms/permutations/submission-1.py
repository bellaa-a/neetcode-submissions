class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.nums = nums
        self.dfs([], set())
        return self.res
        
    def dfs(self, subset, seen):
        for i in range(len(self.nums)):
            n = self.nums[i]
            
            if seen and n in seen:
                continue

            if len(subset) >= len(self.nums)-1:
                self.res.append(subset+[n])
            else:
                seen.add(n)
                self.dfs(subset+[n], seen)
                seen.remove(n)
            