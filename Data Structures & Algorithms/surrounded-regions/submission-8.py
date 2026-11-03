class Solution:
    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        def dfs(r,c):
            if r<0 or c<0 or r==row or c==col or board[r][c]!='O':
                return 
            board[r][c] = "#"
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for i in range(row):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][col-1] =='O':
                dfs(i,col-1)
        for j in range(col):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[row-1][j] == 'O':
                dfs(row-1,j)
        for r in range(row):
            for c in range(col):
                if board[r][c] == '#':
                    board[r][c] = "O"
                elif board[r][c] =='O':
                    board[r][c] = 'X'