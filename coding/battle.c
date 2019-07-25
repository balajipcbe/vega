int countBattleships(char** board, int boardRowSize, int boardColSize) {
    int i,j;
    int count = 0;
    for(i = 0; i < boardRowSize; ++i) {
        for(j = 0; j < boardColSize; ++j){
            if (board[i][j] == '.') 
                continue;
            if (i == 0 || j == 0) {
                count++;
                continue;
            }
            if (board[i][j-1] != 'X' && board[i-1][j] != 'X')
                count++;
        }
    }
    return count;
}
