class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def find_word(p, w, b, v, nr, nc, i = 1):
            if i == len(w):
                return True
           
            #right
            if p[1] < nc-1 and v[p[0]][p[1]+1] and i < len(w) and b[p[0]][p[1]+1] == w[i]:
                p[1] += 1
                v[p[0]][p[1]] = False
                i += 1
                #print('right',p[0],p[1],i)
                if find_word(p,w, b, v, nr, nc,i):
                    return True
                v[p[0]][p[1]] = True
                p[1] -= 1
                i -= 1
            
            #left
            if p[1] > 0 and v[p[0]][p[1]-1] and i < len(w) and b[p[0]][p[1]-1] == w[i]:
                p[1] -= 1
                v[p[0]][p[1]] = False
                i += 1
                #print('left',p[0],p[1],i)
                if find_word(p,w, b,v,nr,nc,i):
                    return True
                v[p[0]][p[1]] = True
                p[1] += 1
                i -= 1
            
            #up
            if p[0] > 0 and v[p[0]-1][p[1]] and i < len(w) and b[p[0]-1][p[1]] == w[i]:
                p[0] -= 1
                v[p[0]][p[1]] = False
                i += 1
                #print('up',p[0],p[1],i)
                if find_word(p,w, b,v,nr,nc, i):
                    return True
                v[p[0]][p[1]] = True
                p[0] += 1
                i -= 1

            #down
            if p[0] < nr-1 and v[p[0]+1][p[1]] and i < len(w) and b[p[0]+1][p[1]] == w[i]:
                p[0] += 1
                v[p[0]][p[1]] = False
                i += 1
                #print('down',p[0],p[1],i)
                if find_word(p, w, b, v, nr, nc, i):
                    return True
                v[p[0]][p[1]] = True
                p[0] -= 1
                i -= 1
                
            return False
            
        nrow = len(board)
        ncol = len(board[0])
        visited = [[True for x in range(ncol)] for x in range(nrow)]
        
        if len(word) == 0:
            return False
        
        point = [0,0]
        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == word[0]:
                    if visited[i][j]:
                        visited[i][j] = False
                        point[0] = i
                        point[1] = j
                        #print('start:', point[0],point[1])
                        if find_word(point, word, board, visited, nrow, ncol):
                            return True
                        visited[i][j] = True
        return False
