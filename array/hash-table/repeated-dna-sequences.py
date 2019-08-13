class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        from collections import defaultdict
        import operator
        dna = defaultdict(int)
        n = len(s)
        result = []
        for i in range(n-9):
            snippet = s[i:i+10]
            dna[snippet] += 1
        return [k for k, v in dna.items() if v > 1]

print Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
print Solution().findRepeatedDnaSequences("AAAAAAAAAAAA")
print Solution().findRepeatedDnaSequences("AAAAAAAAAAA")
        
        