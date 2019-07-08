class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def is_live(n):
            return n == 1
        
        def is_dead(n):
            return n == 0
        
        def get_state(i, j, n, m):
            """
            check if ith element should live or die
            returns:
                new state of element
            """
            count_live = 0
            count_dead = 0
            a,b,c,d,e,f,g,h = None,None,None,None,None, None, None,None
            if i-1 >= 0 and j-1>=0:
                a = copy_board[i-1][j-1]
            if i-1>=0:
                b = copy_board[i-1][j] 
            if i-1 >= 0 and j+1<m:
                c = copy_board[i-1][j+1]
            if j-1 >= 0:
                d = copy_board[i][j-1]  
            if j+1 < m:
                e = copy_board[i][j+1]  
            if i+1 < n and j-1>=0:
                f = copy_board[i+1][j-1]
            if i+1 < n:
                g = copy_board[i+1][j]  
            if i+1 < n and j+1<m:
                h = copy_board[i+1][j+1]  
            val = [a,b,c,d,e,f,g,h]
            for item in val:
                if item == 1:
                    count_live += 1
                elif item == 0:
                    count_dead += 1
            state = copy_board[i][j]
            if copy_board[i][j] == 1:
                if count_live < 2 or count_live > 3:
                    state = 0
            else:
                if count_live == 3:
                    state = 1
            # print 'For ', i, j, ' element ', board[i][j], ' returning ', state, ' because count live ', count_live, ' count dead ', count_dead
            return state
    
        
        if not board:
            return None
        n = len(board)
        m = len(board[0])
        copy_board = [[board[i][j] for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                # print get_state(i, j, n, m)
                board[i][j] = get_state(i, j, n, m)
        print board
        print copy_board
        return board