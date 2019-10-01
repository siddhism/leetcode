#
# @lc app=leetcode id=361 lang=python
#
# [361] Bomb Enemy
#

class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # n*m*(n+m)
        # n*m do one loop and store something and do something make it n *m * 4
        if not grid:
            return 0
        n = len(grid)
        m = len(grid[0])
        # L -> R
        dp1 = [[0 for _ in range(m)] for _ in range(n)]
        dp2 = [[0 for _ in range(m)] for _ in range(n)]
        dp3 = [[0 for _ in range(m)] for _ in range(n)]
        dp4 = [[0 for _ in range(m)] for _ in range(n)]
        dp = [[0 for _ in range(m)] for _ in range(n)]

        # def create_arr(a_start, a_end, a_step, b_start, b_end, b_step, storage):
        #     for i in range(a_start, a_end, a_step):
        #         count = 0
        #         for j in range(b_start, b_end, b_step):
        #             if grid[i][j] == 'E':
        #                 count += 1
        #             elif grid[i][j] == 'W':
        #                 count = 0
        #             else:
        #                 # for zeroes, set count
        #                 dp1[i][j] = count

            
        # iterate over grid 4  times
        # L -> R
        # for i in range(0, n):
        #     count = 0
        #     for j in range(0, m):
        #         if grid[i][j] == 'E':
        #             count += 1
        #         elif grid[i][j] == 'W':
        #             count = 0
        #         else:
        #             # for zeroes, set count
        #             dp1[i][j] = count
        # # create_arr(0, n, 1, 0, m, 1, dp1)
        # print (dp1)
        # # create_arr(n-1, 0, -1, 0, m, 1, dp2)
        # print (dp2)
        # # create_arr(0, n, 1, 0, n, 1, dp3)
        # print (dp3)
        # # create_arr(m-1, 0, -1, 0, n, 1, dp4)
        # print (dp4)
        for i in range(0, n):
            count = 0
            for j in range(0, m):
                if grid[i][j] == 'E':
                    count += 1
                elif grid[i][j] == 'W':
                    count = 0
                else:
                    # for zeroes, set count
                    dp1[i][j] = count
        # print (dp1)
        for i in range(0, n, 1):
            count = 0
            for j in range(m-1, -1, -1):
                if grid[i][j] == 'E':
                    count += 1
                elif grid[i][j] == 'W':
                    count = 0
                else:
                    # for zeroes, set count
                    dp2[i][j] = count
        # print (dp2)

        for j in range(0, m, 1):
            count = 0
            for i in range(0, n, 1):
                if grid[i][j] == 'E':
                    count += 1
                elif grid[i][j] == 'W':
                    count = 0
                else:
                    # for zeroes, set count
                    dp3[i][j] = count
        # print (dp3)

        for j in range(0, m, 1):
            count = 0
            for i in range(n-1, -1, -1):
                if grid[i][j] == 'E':
                    count += 1
                elif grid[i][j] == 'W':
                    count = 0
                else:
                    # for zeroes, set count
                    dp4[i][j] = count
        # print (dp4)

        # final answer
        max_result = 0
        for i in range(n):
            for j in range(m):
                dp[i][j] = dp1[i][j] + dp2[i][j] + dp3[i][j] + dp4[i][j]
                if dp[i][j] > max_result:
                    max_result = dp[i][j]
        # print (dp)
        return max_result

# print (Solution().maxKilledEnemies([["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]))







        
