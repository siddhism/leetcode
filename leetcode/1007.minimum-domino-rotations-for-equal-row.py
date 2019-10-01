#
# @lc app=leetcode id=1007 lang=python
#
# [1007] Minimum Domino Rotations For Equal Row
#

# @lc code=start
class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        count = 0
        # for range 6 initialize all pos to be zero
        dp = [[False for _ in range(n)] for _ in range(2)]
        if n == 0:
            return 0
        if n == 1:
            return 0

        orig_a = A; orig_b = B
        targets = [A[0], A[1], B[0], B[1]]
        count1 = 0
        target = targets[0]
        for i in range(1, n):
            a1 = A[i-1]; a2 = A[i];b1 = B[i-1];b2 = B[i]
            if a2 == target:
                continue
            elif a2 == b1:
                t = b1
                b1 = a2
                a2 = t
                count1 += 1
            else:
                break
        A = orig_a
        B = orig_b

        count2 = 0
        target = B[0]
        # swap first two already
        A[0], B[0] = B[0], A[0]
        for i in range(1, n):
            a1 = A[i-1]; a2 = A[i];b1 = B[i-1];b2 = B[i]
            if a2 == target:
                continue
            elif a2 == b2:
                a2, b2 = b2, a2
                count2 += 1
            else:
                break
        A = orig_a
        B = orig_b

        count3 = 0
        target = A[0]
        # swap first two already
        A[0], B[0] = B[0], A[0]
        for i in range(1, n):
            a1 = A[i-1]; a2 = A[i];b1 = B[i-1];b2 = B[i]
            if b2 == target:
                continue
            elif a2 == b2:
                a2, b2 = b2, a2
                count3 += 1
            else:
                break
        A = orig_a
        B = orig_b

        count4 = 0
        target = B[0]
        # no need to swap initial two elems
        for i in range(1, n):
            a1 = A[i-1]; a2 = A[i];b1 = B[i-1];b2 = B[i]
            if b2 == target:
                continue
            elif a2 == b2:
                a2, b2 = b2, a2
                count4 += 1
            else:
                break
        A = orig_a
        B = orig_b

        print (count1, count2, count3, count4)
        return min(count1, count2, count3, count4)
            
                    
# @lc code=end

