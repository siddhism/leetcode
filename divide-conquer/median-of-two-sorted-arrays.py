class Solution(object):
    
    def findElementAtIndex(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        ia = len(a) / 2
        ib = len(b) / 2
        ma = a[ia]
        mb = a[ib]
        # when k is bigger than the sum of a and b's median indices 
        if ia + ib < k:
            # if a's median is bigger than b's, b's first half doesn't include k
            if ma > mb:
                return self.findElementAtIndex(a, b[ib + 1:], k - ib - 1)
            else:
                return self.findElementAtIndex(a[ia + 1:], b, k - ia - 1)
        # when k is smaller than the sum of a and b's indices
        else:
            # if a's median is bigger than b's, a's second half doesn't include k
            if ma > mb:
                return self.findElementAtIndex(a[:ia], b, k)
            else:
                return self.findElementAtIndex(a, b[:ib], k)

    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1)
        m = len(nums2)
        l = n + m
        if l % 2 == 0:
            index1 = (l)/2 - 1
            index2 = (l)/2
            x = self.findElementAtIndex(nums1, nums2, index1)
            y = self.findElementAtIndex(nums1, nums2, index2)
            return x + y / 2
        else:
            index1 = index2 = (l)/2
            return self.findElementAtIndex(nums1, nums2, index1)


        # my code
        # if ma == index1:
        #     return a[index1]
        # if mb == index2:
        #     return b[index2]
        # if a[ma] < b[0]:
        #     return self.findElementAtIndex(a[n/2:], b[:m], index1-ma, index2-ma)
        # elif b[0] < a[ma] < b[mb]:
        #     a = self.findElementAtIndex(a[:n/2], b[:m/2], index1, index2)
        #     b = self.findElementAtIndex(a[n/2:], b[m/2:], index1, index2)
        #     return (a + b)  / 2
        # elif b[mb] < a[ma] < b[m-1]:
        #     a = self.findElementAtIndex(a[n/2:], b[m/2:], index1, index2)
        #     b = self.findElementAtIndex(a[:n/2], b[:m/2], index1, index2)
        #     return (a + b)  / 2
        # else:
        #     return self.findElementAtIndex(a[:n/2], b[0:m], index1-ma, index2-ma)
