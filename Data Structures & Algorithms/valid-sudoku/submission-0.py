class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = defaultdict(set)
        col_set = defaultdict(set)
        square_set = defaultdict(set)
        for i in range(9):
            seen = set()
            for j in range(9):
                print(seen)
                val = board[i][j]
                if val == ".":
                    continue
                if val in row_set[i] or val in col_set[j] or val in square_set[3*int(i/3) + int(j/3)]:
                    return False
                row_set[i].add(val)
                col_set[j].add(val)
                square_set[3*int(i/3) + int(j/3)].add(val)
        
        return True
        