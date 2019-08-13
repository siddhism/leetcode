class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        next = 0
        scanned = 0
        count = 1
        last = length - 1
        for i in range(0, length - 1):
            current = nums[i]
            # print 'i ', i, ' current ', current
            if current in nums[:i]:
                # this number is already seen, no movement required
                # print 'current is already seen ', current
                continue
            for j in range(i+1, length):
                if nums[j] in nums[:j]:
                    continue
                # print (j, nums[j], current)
                if nums[j] != current:
                    # move this after i
                    for k in range(i+2, j):
                        nums[k] = nums[k+1]
                    nums[i+1] = nums[j]
                    # print ('after movement ', nums)
                    count += 1
                    break
            # print ('after i ', i, ' nums ', nums)
        return count

print Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
