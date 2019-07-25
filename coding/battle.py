class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        rows = len(board)
        col = rows
        i = 0
        j = 0
        for i in range(rows):
            for j in range(col):
                if board[i][j] == 'X':
                    if i == rows-1 and board[i-1][j] == '.':
                        count += 1
                    elif j == col-1 and board[i][j-1] == '.':
                        count += 1
                    elif board[i+1][j] == '.' and board[i][j+1] == '.':
                        count += 1
                    elif board[i+1][j] == 'X':
                        count += rows
                        j += 1
                    elif board[i][j+1] == 'X':
                        count += rows
                        i += 1
        return count
    
