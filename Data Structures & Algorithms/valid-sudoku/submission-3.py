class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                elif board[i][j] != ".":
                    s.add(board[i][j])
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != ".":
                    s.add(item)
        for row in range(0,9,3):
            for col in range(0,9,3):
                s = set()
                for i in range(3):
                    
                    for j in range(3):
                        item = board[row+i][col+j]
                        if item in s:
                            return False
                        elif item != '.':
                            s.add(item)
        return True
