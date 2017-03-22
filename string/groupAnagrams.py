

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        hashmap = {}
        for word in strs:
            
            key = 1
            
            for l in word:
                
                key *= prime[ord(l) - ord('a')]
            
            if not hashmap.has_key(key):
                
                hashmap[key] = []
                
            hashmap[key].append(word)
            
        return hashmap.values()

