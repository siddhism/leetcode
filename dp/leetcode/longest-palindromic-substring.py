class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)  # get length of input string

        # table[i][j] will be false if substring
        # str[i..j] is not palindrome. Else
        # table[i][j] will be true
        table = [[0 for x in range(n)] for y in range(n)]
        # All substrings of length 1 are
        # palindromes
        start = 0
        max_length = 1
        i = 0
        while i < n:
            table[i][i] = True
            i = i + 1

        # check for sub-string of length 2.
        i = 0
        while i < n - 1:
            if (s[i] == s[i + 1]):
                table[i][i + 1] = True
                start = i
                max_length = 2
            i = i + 1

        # Check for lengths greater than 2.
        # k is length of substring
        k = 3
        while k <= n:
            # Fix the starting index
            i = 0
            while i < (n - k + 1):

                # Get the ending index of
                # substring from starting
                # index i and length k
                j = i + k - 1
                # print i, j
                # checking for sub-string from
                # ith index to jth index iff
                # st[i+1] to st[(j-1)] is a
                # palindrome
                if table[i + 1][j - 1] and s[i] == s[j]:
                    table[i][j] = True
                    if k > max_length:
                        start = i
                        max_length = k
                i = i + 1
            k = k + 1
        return s[start:start+max_length]


print Solution().longestPalindrome("cbbd")
print Solution().longestPalindrome("babab")
print Solution().longestPalindrome("babad")
print Solution().longestPalindrome("bab")
print Solution().longestPalindrome("a")
print Solution().longestPalindrome("ccc")
print Solution().longestPalindrome("abadd")
