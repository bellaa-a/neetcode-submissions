class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.s = s
        self.dfs(0, [])
        return self.res


    def dfs(self, start, subset):

        if start >= len(self.s):
            self.res.append(subset.copy())
            return
        
        for i in range(start, len(self.s)):
            palidrome = True
            l = start
            r = i
            while l <= r:
                if self.s[l] != self.s[r]:
                    palidrome = False
                l+=1
                r-=1
            if palidrome:
                subset.append(self.s[start:i+1])
                self.dfs(i+1, subset)
                subset.pop()
        
        