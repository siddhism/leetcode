class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = sorted(nums)
        negatives = []
        positives = []
        zeroes = []
        for item in a:
            if item < 0:
                negatives.append(item)
            elif item == 0:
                zeroes.append(item)
            else:
                positives.append(item)
        if len(negatives) == 0:
            if len(positives) > 2:
                a, b, c = positives[-1], positives[-2], positives[-3]
                return a * b * c
            else:
                return 0
        elif len(negatives) >= 2:
            if len(positives) > 2:
                a, b, c = positives[-1], positives[-2], positives[-3]
                d, e = abs(negatives[0]), abs(negatives[1])
                return max(a*b*c, a*d*e)
            else:
                # 0 or 1 positive
                if len(positives) == 1:
                    return positives[0] * abs(negatives[0]) * abs(negatives[1])
                else:
                    # zero positives to take away
                    if len(zeroes) > 0:
                        return 0
                    else:
                        # return min 3 negative product
                        return negatives[-1] * negatives[-2] * negatives[-3]
        # only 1 choice of negative numbers left
        elif len(negatives) == 1:
            if len(positives) > 2:
                # return top 3 positive
                return positives[-1] * positives[-2] * positives[-3]
            else:
                if len(zeroes):
                    return 0
                elif len(positives) == 2: # makes total 3 numbers
                    return positives[0] * positives[1]* negatives[0]
                # no other combo left for total 3 numbers
