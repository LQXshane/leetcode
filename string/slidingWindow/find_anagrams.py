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

# Similarly, use the approach by awice, we can do straightforward window sliding by,

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        A = [ord(x) - ord('a') for x in p]
        B = [ord(x) - ord('a') for x in s]

        target = [0] * 26
        for x in A:
            target[x] += 1
        ans = []
        
        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                ans += i - len(p) + 1,
        return ans 
