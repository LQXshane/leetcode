
class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        
        self.trie = collections.defaultdict(list) # build a trie using words
        self.length, self.ans = len(words[0]), []
        for word in words:
            prefix = ""
            for letter in word:
                prefix += letter
                self.trie[prefix].append(word) # may be multiple word with same prefix
                # even there were only 1, using = would disjoin the letters 
        for word in words:
            self.dfs([word])
        
        return self.ans
        
    
    def dfs(self, square):
        '''
        :type square: [[str]]
        '''
        
        if len(square) == self.length: 
            self.ans.append(square)
            return

        checker = ''.join(zip(*square)[len(square)])
        for x in self.trie[checker]:
            self.dfs(square + [x])
        
