class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[i][j] in seen:
                    return False
                elif board[i][j] != '.':
                    seen.add(board[i][j])
        for i in range(9):
            seen = set()
            for j in range(9):
                if board[j][i] in seen:
                    return False
                elif board[j][i] != '.':
                    seen.add(board[j][i])
        for r in range(0,9,3):
            for c in range(0,9,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[r+i][c+j] in seen:
                            return False
                        elif board[r+i][c+j]!= '.':
                            seen.add(board[r+i][c+j])
        return True
            