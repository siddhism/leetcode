class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return
        row = len(matrix) - 1
        col = len(matrix[0]) - 1
        result = []
        l = 0
        r = col
        t = 0
        b = row
        # print 'row col ', row, col
        # result.append(matrix[0][0])
        while l <= r or t <= b:
            # print 'starting loop again ', l, r, t, b
            for j in range(l, r+1):
                # print 'left to right'
                # print t, j, matrix[t][j]
                result.append(matrix[t][j])
            t = t + 1
            for j in range(t, b+1):
                # print 'top to bottom'
                # print j, r, matrix[j][r]
                result.append(matrix[j][r])
            r = r - 1
            if t <= b:
                for j in range(r, l-1, -1):
                    # print 'righ to left'
                    result.append(matrix[b][j])
            b = b - 1
            if l <= r:
                for j in range(b, t-1, -1):
                    # print 'bottom to top'
                    result.append(matrix[j][l])
                    b = b - 1
            l = l + 1
        return result        

# print Solution().spiralOrder(
#     [
#      [ 1, 2, 3 ],
#      [ 4, 5, 6 ],
#      [ 7, 8, 9 ]
#     ]
# )
# print Solution().spiralOrder(
#     [
#       [1, 2, 3, 4],
#       [5, 6, 7, 8],
#       [9,10,11,12]
#     ]
# )