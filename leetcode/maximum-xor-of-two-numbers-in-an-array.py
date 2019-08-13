class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        bins = []
        # create a 32 bit vector(arrary) to represent the current state
        set_bits = defaultdict(list)
        for num in nums:
            binary_num = bin(num)[2:]
            # print 'num ', num, ' binary ', binary_num
            bins.append(binary_num)
            n = len(binary_num)
            for i in range(32):
                if i <= n-1 and binary_num[n-i-1] == '1':
                    # print 'i ', i, 'binary num ', binary_num[i]
                    set_bits[i].append(num)
        # now for each of set bits we need to check if any other number can match it up
        sorted_bits = sorted(set_bits.items(), reverse=True)
        for k, v in sorted_bits:
            if not v:
                continue
            first = v
            first_index = k
        for k, v in sorted_bits[first_index:]:
            if not v:
                continue
            second = v
            second_index = k
        top = []
        # compare item with first highest set bit with the other one
        for i in first:
            for j in second:
                x = i ^ j
                top.append(x)
        return max(top)

# print Solution().findMaximumXOR([3, 10, 5, 25, 2, 8])
