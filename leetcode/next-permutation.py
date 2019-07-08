class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        prev = nums[-1]
        current = []
        current.append(prev)
        pos = None
        for i in range(n-2, -1, -1):
            num = nums[i]
            current.append(num)
            if num < prev:
                # need to make switch on this position
                pos = i
                print nums, 'requires action at pos ', pos
                break
            prev = num
        # from pos, update the number which next biggest in remaining array
        if pos is None:
            return
        if pos == 0:
            nums = nums[::-1]
        rem = sorted(nums[pos:])
        # find next number which is bigger or equal than pivot
        next_elements = [item for item in rem[1:] if item > num]
        if not next_elements:
            return
        next_num = min(next_elements)
        rem.remove(next_num)
        nums[pos] = next_num
        # pop everything after pos and append rem
        # nums = nums[:pos+1]
        for i in range(len(rem)):
            nums[pos+i+1] = rem[i]
        # nums.extend(rem)
        return nums

print Solution().nextPermutation([1, 2, 3, 4]) == [1, 2, 4, 3]
print Solution().nextPermutation([1, 2, 4, 3]) == [1, 3, 2, 4]
print Solution().nextPermutation([1, 3, 2, 4]) == [1, 3, 4, 2]
print Solution().nextPermutation([1, 3, 4, 2]) == [1, 4, 2, 3]
print Solution().nextPermutation([1, 4, 2, 3]) == [1, 4, 3, 2]
print Solution().nextPermutation([1, 4, 3, 2]) == [2, 1, 3, 4]
print Solution().nextPermutation([2, 1, 3, 4]) == [2, 1, 4, 3]
print Solution().nextPermutation([2, 1, 4, 3]) == [2, 3, 1, 4]
print Solution().nextPermutation([2, 3, 1, 4]) == [2, 3, 4, 1]
print Solution().nextPermutation([2, 3, 4, 1]) == [2, 4, 1, 3]
print Solution().nextPermutation([2, 4, 1, 3]) == [2, 4, 3, 1]
print Solution().nextPermutation([2, 4, 3, 1]) == [3, 1, 2, 4]
print Solution().nextPermutation([3, 1, 2, 4]) == [3, 1, 4, 2]
print Solution().nextPermutation([3, 1, 4, 2]) == [3, 2, 1, 4]
print Solution().nextPermutation([3, 2, 1, 4]) == [3, 2, 4, 1]
print Solution().nextPermutation([1,2,3])
print Solution().nextPermutation([3,2,1])