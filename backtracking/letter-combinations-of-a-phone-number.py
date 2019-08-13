class Solution(object):
    mapping = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'i'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w', 'x', 'y', 'z']
    }


    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        if len(digits) == 1:
            result = self.mapping[digits[0]]
            return result
        prev = self.letterCombinations(digits[1:])
        # append it with current digit
        result = []
        curr = digits[0]
        for c in self.mapping[curr]:
            x = [c + ''.join(item) for item in prev]
            result.extend(x)
        return result

print Solution().letterCombinations('23')
y = Solution().letterCombinations('234')
x = ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]
print y
print y == x
