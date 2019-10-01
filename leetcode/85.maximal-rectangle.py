#
# @lc app=leetcode id=85 lang=python
#
# [85] Maximal Rectangle
#
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix: return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0] * n # initialize left as the leftmost boundary possible
        right = [n] * n # initialize right as the rightmost boundary possible
        height = [0] * n

        maxarea = 0
        # print data
        for i in range(m):

            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == '1': height[j] += 1
                else: height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == '1': left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right
            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1': right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            print 'left  ', left
            print 'right ', right
            print 'height', height
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))
                # print height[j] * (right[j] - left[j])

        return maxarea

        
    def print_matrix(self, matrix):
        n = len(matrix)
        m = len(matrix[0])
        print '\n start \n'
        for i in range(n):
            for j in range(m):
                print matrix[i][j], ' ', 
            print '\n'
        print '\n Done \n'

print Solution().maximalRectangle(
    [
        ["1","0","1","0","0"],
        ["1","0","1","1","1"],
        ["1","1","1","1","1"],
        ["1","0","0","1","0"]
    ]
)

