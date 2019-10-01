#
# @lc app=leetcode id=975 lang=python
#
# [975] Odd Even Jump
#
class Solution(object):
    def oddEvenJumps(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not A:
            return 0

        n = len(A)
        # for each index we'll check forward indexes and pick min value to be jumped
        dp = [False for _ in range(n)]
        jumps = [A[i] for i in range(n)]

        # decide jumping index for i
        # find index to jump
        i = 0
        jump_number = 1
        while i < n:
            print (' value of i ', i)
            has_jump = False
            for j in range(i+1, n):
                print (' value of j ', j)
                if jump_number % 2 == 1:
                    # odd jump
                    if A[j] >= A[i]:
                        i = j
                        has_jump = True
                        jump_number += 1
                        break
                else:
                    if A[j] <= A[i]:
                        i = j
                        has_jump = True
                        jump_number += 1
                        break
            if has_jump:
                pass
            else:
                found = False
                dp[j] = False
                i = i + 1                
        print dp

print Solution().oddEvenJumps([2,3,1,1,4])

