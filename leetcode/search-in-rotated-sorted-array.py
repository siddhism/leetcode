class Solution(object):
    def get_pivot_index(self, nums):
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l + r) / 2
            if nums[mid] > nums[mid+1]:
                return mid
            if nums[mid] > nums[l]:
                # left side is in sorted order, we need to look right
                l = mid + 1
            else:
                r = mid 
        return - 1

    def binary_search(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) / 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return - 1


    def search(self, nums, target):
        pivot = self.get_pivot_index(nums)
        if pivot == -1:
            return self.binary_search(nums, target)
        else:
            result = self.binary_search(nums[:pivot+1], target)
            if result != -1:
                return result
            result = self.binary_search(nums[pivot+1:], target)
            if result == -1:
                # if not found return
                return result
            # since it's on right side of pivot, add pivot in result index
            result = pivot + 1 + result
            return result

print Solution().search([1,2,3,4,5], 3)
print Solution().search([2,3,4,5,1], 3)
print Solution().search([3,4,5,1,2], 3)
print Solution().search([4,5,1,2,3], 3)
print Solution().search([5,1,2,3,4], 3)
print Solution().search([3, 1], 3)
print Solution().search([4,5,6,7,0,1,2], 3)