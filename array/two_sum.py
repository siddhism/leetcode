class Solution(object):
    
    def binary_search(self, array, num):
        low = 0
        high = len(array) - 1
        while low <= high:
            mid = (low + high) /2
            if array[mid] == num:
                return mid
            if array[mid] < num:
                low = mid + 1
            else:
                high = mid - 1
        return -1
            
    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        old_index = {}
        new_index = {}
        old_nums = nums
        for index, elem in enumerate(nums):
            old_index[elem] = index
        nums = sorted(nums)
        for index, elem in enumerate(nums):
            new_index[index] = elem
        for i in range(len(nums)):
            found = False
            first = nums[i]
            second = None
            comp = target - first
            has_comp = self.binary_search(nums[i:], comp)
            print 'found in binary search ', has_comp
            if has_comp != -1:
                second_index = has_comp + i
                second = nums[second_index]
                print [old_index[first], old_index[second]]
                return [old_index[first], old_index[second]]
                # return [old_index.get(first), old_index.get(second)]

Solution().twoSum([3, 3], 6)