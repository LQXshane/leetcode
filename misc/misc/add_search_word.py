# 211. Add and search words

'''return all valid words'''
# https://leetcode.com/problems/add-and-search-word-data-structure-design/discuss/
class WordDictionary(object):

    def __init__(self):
        self.root ={}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        t = self.root
        for char in word:
            if char not in t:
                t[char] = {}
            t = t[char]
        t['#'] = '#' # marks end of word


    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def dfs(resList, curWord, trie):
            if '#' in trie:
                resList.append(curWord)
                return
            for i in range(len(self.word)):
                if self.word[i] == '.':
                    # search next level
                    for x in trie.keys():
                        dfs(resList, curWord + x, trie[x])
                else:
                    if self.word[i] in trie:
                        dfs(resList, curWord + self.word[i], trie[word[i]])
        if not word: return []
        self.word = word
        res = []
        root = self.root
        dfs(res, "", root)
        return res
