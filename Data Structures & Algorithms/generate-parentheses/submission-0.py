class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        self.n = n
        self.dfs("", 0, 0, 0)
        return self.res


    def dfs(self, subset, left_bracket, unfinished, completed):
        if completed >= self.n:
            self.res.append(subset)
            return
        if left_bracket < self.n:
            self.dfs(subset + "(", left_bracket+1, unfinished+1, completed)
        if left_bracket > 0 and unfinished >= 1:
            self.dfs(subset + ")", left_bracket, unfinished-1, completed+1)