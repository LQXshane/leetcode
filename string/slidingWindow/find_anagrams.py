class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """        
        ans = []
        chars = [0 for _ in xrange(26)]
        for x in p: chars[ord(x) - ord('a')] += 1
        start, end, cnt = 0, 0, 0

        while end < len(s):
            if chars[ord(s[end]) - ord('a')] >= 1:
                cnt += 1
            chars[ord(s[end]) - ord('a')] -= 1
            end += 1
            
            if cnt == len(p): ans += start,
                
            if end - start == len(p):
                if chars[ord(s[start]) - ord('a')] >= 0:
                    cnt -= 1
                chars[ord(s[start]) - ord('a')] += 1
                start += 1

        return ans
