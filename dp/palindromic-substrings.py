class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        if not s:
            return 0
        index_of_pal = defaultdict(list)
        # build of index of pal
        for index, c in enumerate(s):
            index_of_pal[index] = [index]
        count = len(s) # all single char strings
        for index in range(1, len(s)):
            c = s[index]
            prev = s[index-1]
            # print index, c, ' prev ', prev 
            if prev == c:
                count = count + 1
                # if prev char is equal to current
                index_of_pal[index].append(index-1)
            # find char to match index
            match_indexes = index_of_pal[index-1]
            # print 'matches ', match_indexes
            for match_index in match_indexes:
                if match_index - 1 >= 0:
                    match_char = s[match_index - 1]
                    if match_char == c:
                        count += 1
                        index_of_pal[index].append(match_index - 1)
            # print index_of_pal
        return count

print Solution().countSubstrings('aaa')
print Solution().countSubstrings('babab')
print Solution().countSubstrings('abccba')