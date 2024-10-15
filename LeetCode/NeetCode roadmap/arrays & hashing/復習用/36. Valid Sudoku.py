class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [[] for _ in range(9)]
        col = [[] for _ in range(9)]
        box = [[[] for _ in range(3)] for _ in range(3)]
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in row[r]) or (board[r][c] in col[c]) or (board[r][c] in box[r // 3][c // 3]):
                    return False
                row[r].append(board[r][c])
                col[c].append(board[r][c])
                box[r // 3][c // 3].append(board[r][c])
        return True