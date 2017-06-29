# Hard
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        return self.helper(s, wordDict, {})
        
    def helper(self, s, wordDict, memo):
        # print memo
        if s in memo: return memo[s]
        if not s: return []
        
        res = []
        for word in wordDict:
            # print word
            if not s.startswith(word):
                continue
            if len(word) == len(s):
                
                print word
                res.append(word)
            else:
                resultOfTheRest = self.helper(s[len(word):], wordDict, memo)
                for item in resultOfTheRest:
                    # print item, word
                    item = word + ' ' + item
                    res.append(item)
        memo[s] = res
        return res
