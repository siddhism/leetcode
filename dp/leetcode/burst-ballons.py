class Solution(object):

    def helper(self, a, b, c, nums):
        """
        Gets three indexes and computes the multiplication of them
        """
        # print 'helper called for ', a, b, c
        # check in cache here
        result = 1
        n = len(nums)
        if -1 <= a < n:
            result *= nums[a]
        if -1 <= b < n:
            result *= nums[b] 
        if -1 <= c < n:
            result *= nums[c]
        # put in cache here
        return result

    def get_cache_key(self, nums):
        idx = [v for k, v in enumerate(nums)]
        # idx.pop(skip_index)
        key = '-'.join(map(str, idx))
        return key

    def maxCoinsExcludeIndex(self, nums, skip_index):
        """
        find max in list excluding index i
        :type nums: List[int]
        :rtype: int
        """
        # print '-> -> called max coins helper with nums ', nums, skip_index
        if 0 <= skip_index < len(nums):
            nums.pop(skip_index)
        cache_key = self.get_cache_key(nums)
        cache_val = self.cache.get(cache_key)
        if cache_val:
            return cache_val

        n = len(nums) # original length
        if n <= 2:
            return max(nums)
        dp = [1 for i in range(n+1)]
        for i in range(n-1):
            # print '******-> callling max coin helper for ', nums, i
            burst_val = self.helper(i-1, i, i+1, nums)
            c_nums = nums[:]
            b = self.maxCoinsExcludeIndex(c_nums, i)
            max_at_i = burst_val +  b
            # print 'burst val ', burst_val, ' b ', b, ' max_at_i ', max_at_i
            dp[i] = max_at_i
        # print 'dp array                   ', dp
        result = max(dp)
        self.cache[cache_key] = result
        return result
    
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # print 'called max coins with nums ', nums
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        self.orig_nums = nums
        self.cache = {}
        n = len(nums) # original length
        nums.append(1) # extra padding to get nums[n] and nums[-1]
        dp = [1 for i in range(n+1)]
        for i in range(n-1):
            burst_val = self.helper(i-1, i, i+1, nums)
            c_nums = nums[:]
            b = self.maxCoinsExcludeIndex(c_nums, i)
            max_at_i = burst_val +  b
            dp[i] = max_at_i
        # print 'dp array ', dp
        # print self.cache
        return max(dp)


        
# print Solution().maxCoins([3,1,5,8])
# print Solution().maxCoins([35,16,83,87,84,59,48,41,20,54])