# 567. Permutation in String

# Solution One: Sliding window
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        dic = [0] * 26
        for x in s1: dic[ord(x) - ord('a')] += 1
        
        start, end, cnt, n = 0, 0, 0, len(s1)
        while end < len(s2):
            if dic[ord(s2[end]) - ord('a')] >= 1:
                cnt += 1
            dic[ord(s2[end]) - ord('a')] -= 1
            end += 1
            if cnt == n: return True
            if end - start == n:
                # the dictionary has been "exhausted"
                if dic[ord(s2[start]) - ord('a')] >= 0:
                    cnt -= 1
                dic[ord(s2[start]) - ord('a')] += 1
                start += 1
        return False
# The trick is to make up the hole in your window and make sure your dictionary is not exhausted!

# Solution Two, credict awice
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in A:
            target[x] += 1

        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False
# In python, this saves a lot of time, because:
# you build the list using ord() in the very beginning, 
# takes O(n) time and space but saves time in visiting the idices later
# also, you can do straight forward window movement
# but window == target may actually take longer, depends on python's implementation.

