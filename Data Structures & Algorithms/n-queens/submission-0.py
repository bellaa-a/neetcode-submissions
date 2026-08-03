class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(i, cols, diag1, diag2, queens, num_queens):
            if num_queens >= n:
                res.append(["".join(row) for row in queens])
                return

            for j in range(n):
                if j in cols or (i-j) in diag1 or (i+j) in diag2:
                    continue

                cols.add(j)
                diag1.add(i-j)
                diag2.add(i+j)
                queens[i][j] = "Q"
                dfs(i+1, cols, diag1, diag2, queens, num_queens+1)
                cols.remove(j)
                diag1.remove(i-j) 
                diag2.remove(i+j)
                queens[i][j] = "."

        dfs(0, set(), set(), set(), [["."] * n for _ in range(n)], 0)

        return res