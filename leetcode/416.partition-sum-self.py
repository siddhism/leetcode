#
# @lc app=leetcode id=416 lang=python
#
# [416] Partition Equal Subset Sum
#
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        sum = 11 # hardcoded have to make it 200 later
        nums = sorted(nums)
        dp = [[False for _ in range(sum+1)] for i in range(n)]

        # dp[i][j] depicts if sum j is possible with element i being present in the result

        # for first row (first element) calculate with just comparison
        for j in range(0, sum+1):
            if j == nums[0] or j == 0:
                dp[0][j] = True

        for i in range(1, n):
            # for each sum compute dp array
            # sum of zero is always possible
            dp[i][0] = True

            for j in range(1, sum+1):
                if  j < nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    # either it can be created by ignoring this element 
                    # or by including this element
                    # exclude current element, sum was already present
                    target = nums[i]
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-target]
                    # above two lines can be combined with or condition

        # self.print_matrix(dp)

        paths = []
        def get_path(i, sum, result=[]):
            # print i, sum
            # If we reached end and sum is non-zero. We output
            # p[] only if arr[0] is equal to sun OR dp[0][sum] 
            # is true. 
            if i == 0 and sum != 0 and dp[0][sum]:
                result.append(nums[i])
                paths.append(result)
                # print (result)
                return
            if i == 0 and sum == 0:
                # print (result)
                paths.append(result)
                return

            # accumulate paths
            if dp[i-1][sum]:
                # result came without this element, this is a new path
                new_path = []
                new_path.extend(result)
                # print ('starting a new path ', new_path)
                get_path(i-1, sum, new_path)

            # If given sum can be achieved after considering 
            # current element. 
            if sum >= nums[i] and dp[i-1][sum-nums[i]]:
                result.append(nums[i])
                get_path(i-1, sum-nums[i], result)
        
        paths = []
        paths = get_path(n-1, 11, result=[])
        print paths

    
    # def print_matrix(self, matrix):
    #     n = len(matrix)
    #     m = len(matrix[0])
    #     # print '\n start \n'
    #     for i in range(n):
    #         for j in range(m):
    #             # print matrix[i][j], ' ', 
    #         # print '\n'
    #     # print '\n Done \n'
     



# print Solution().canPartition([2,3,7,8,11])

