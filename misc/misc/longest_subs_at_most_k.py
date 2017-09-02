# 340. Longest Substring with At Most K Distinct Characters
'''
Given a string, find the length of the longest substring T
that contains at most k distinct characters.
'''
import collections
class Solution():
    def lengthOfLongestSubstringKDistinct(self, s, k):
        l = 0
        i = j = 0
        chars = collections.defaultdict(int)
        count = k
        ans = ""
        while j < len(s):
            if chars[s[j]] == 0:
                count -= 1
            chars[s[j]] += 1
            j += 1
            while count < 0 and i < len(s):
                if j - i > l:
                    l, ans = j - i - 1, s[i:j-1]
                if chars[s[i]] == 1: count += 1
                chars[s[i]] -= 1
                i += 1
        return len(s[i:j]) if l < len(s[i:j]) else l


class Solution2(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        count = i = l = 0
        d = collections.defaultdict(int)
        for j in range(len(s)):
            if d[s[j]] == 0: count += 1
            d[s[j]] += 1
            while count > k:
                d[s[i]] -= 1
                if d[s[i]] == 0: count -= 1
                i += 1
            l = max(l, j - i + 1)
        return l


class Solution3(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        index = {}
        res = low = 0
        for i, x in enumerate(s):
            index[x] = i
            if len(index) > k:
                low = min(index.values())
                del index[s[low]]
                low += 1
            res = max(i - low + 1, res)
        return res


atMostK = Solution()
ans = atMostK.lengthOfLongestSubstringKDistinct("eceba", 2)
print ans
