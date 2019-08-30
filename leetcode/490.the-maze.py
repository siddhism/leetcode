#
# @lc app=leetcode id=490 lang=python
#
# [490] The Maze
#

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        self.maze = maze
        sr, sc = start
        dr, dc = destination
        if not maze:
            return False
        nr = len(self.maze)
        nc = len(self.maze[0])
        dirs = [[-1, 0],[1, 0],[0, -1],[-1, 0]]
        queue = []
        queue.append((sr, sc))
        visited = [[False for _ in range(nr+2)] for _ in range(nc+2)]
        visited[sr][sc] == True
        while queue:
            r, c = queue.pop()
            print 'r ', r, ' c ', c
            if r == dr and c == dc:
                return True
            for dir in dirs:
                x, y = dir[0], dir[1]
                nxtr, nxtc = r + x, c + y
                while 0 <= nxtr < nr and 0 <= nxtc < nc and maze[nxtr][nxtc] == 0:
                    # move in the direction
                    nxtr, nxtc = nxtr + x, nxtc + y
                # block found without finding destination
                nxtr, nxtc = nxtr - x, nxtc - y
                if not visited[nxtr][nxtc]:
                    queue.append((nxtr, nxtc))
                    visited[nxtr][nxtc] = True
        return False



