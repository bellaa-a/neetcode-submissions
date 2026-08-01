class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.candidates = sorted(candidates)
        self.target = target
        self.dfs([], 0, 0)
        return self.res

    def dfs(self, subset, subset_sum, start):
        for i in range(start, len(self.candidates)):
            n = self.candidates[i]
            if i > start and n == self.candidates[i-1]:
                continue
            
            if subset_sum + n == self.target:
                self.res.append(subset + [n])
            elif subset_sum + n < self.target:
                self.dfs(subset + [n], subset_sum + n, i+1)
            else:
                continue