
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        T = [False] * (len(s)+1)
        T[0] = True
        
        for i in range(len(s)+1):
            for j in range(i):
                if T[j] and s[j:i] in wordDict:
                    T[i] = True
                    break
        # print T, i
        return T[len(s)]
