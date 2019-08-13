class Solution(object):
    def get_pivot_index(self, nums):
        pivot = -1
        n = len(nums)
        if n == 0:
            return None
        l = 0
        r = n - 1
        if nums[l] < nums[r]:
            # base case : already sorted
            return 0
        # first = nums[0]
        while l <= r:
            pivot = (l + r) / 2
            if nums[pivot] > nums[pivot+1]:
                return pivot + 1
            if nums[pivot] < nums[l]:
                r = pivot - 1
            else:
                l = pivot + 1
        return -1

    def binary_search(self, A, target):
        l = 0
        r = len(A) - 1
        while l <=r:
            mid = (l + r)/2
            if A[mid] == target:
                return mid 
            elif A[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return -1


    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1
        pivot_index = self.get_pivot_index(nums)
        print 'pivot ', pivot_index
        # if array is not rotated, search in the entire array
        if rotate_index == 0:
            return self.binary_search(nums, target)
        if nums[l] < nums[r]:
            return self.binary_search(nums, target)
        elif target > nums[0]:
            return self.binary_search(nums[:pivot_index], target)    
        else:
            return self.binary_search(nums[pivot_index:], target)
