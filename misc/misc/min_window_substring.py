# 76. Minimum Window Substring(Hard)

'''
Given a string S and a string T, find the minimum window
in S which will contain all the characters in T in complexity O(n).
'''
# S = "ADOBECODEBANC"
# T = "ABC"
# Minimum window is "BANC".
import collections

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        cntr = len(t)
        i = j = 0
        d = collections.Counter(t)
        window = float("inf")
        ans = ""
        while j < len(s):
            if d[s[j]] > 0: cntr -= 1
            d[s[j]] -= 1
            j += 1
            while cntr == 0:
                if j - i < window:
                    window = j - i
                    ans = s[i:j]
                if d[s[i]] == 0:
                    cntr += 1 # move the left window
                d[s[i]] += 1
                i += 1
        return ans or ""

windowString = Solution()
ans = windowString.minWindow("ADOBECODEBANC", "ABC"); print ans
