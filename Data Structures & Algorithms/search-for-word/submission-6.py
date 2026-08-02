class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.n = len(board)
        self.m = len(board[0])
        self.word = word
        self.board = board
        self.exist = False
        for i in range(self.n):
            for j in range(self.m):
                self.dfs(self.board[i][j], i, j, set())
        return self.exist

    def dfs(self, subset, i, j, seen):
        if (i,j) in seen or subset != self.word[:len(subset)] or self.exist:
            return

        if subset == self.word:
            self.exist = True
            return

        seen.add((i,j))
        if i > 0:
            self.dfs(subset + self.board[i-1][j], i-1, j, seen)
        
        if j > 0:
            self.dfs(subset + self.board[i][j-1], i, j-1, seen)

        if i < self.n-1:
            self.dfs(subset + self.board[i+1][j], i+1, j, seen)
        
        if j < self.m-1:
            self.dfs(subset + self.board[i][j+1], i, j+1, seen)
        
        seen.remove((i,j))
        