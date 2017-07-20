
# charater freq sort: Counter, dict


from collections import Counter # this is a very nice built-in for counting duplicates 
class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # freq = {}
        
        # # s = list(s)
        
        # for _, l in enumerate(s):
        #     if l in freq:
        #         freq[l] += 1 
        #     else:
        #         freq[l] = 1
            
        # return ''.join(str(x) for x in sorted(s, key = freq.__getitem__, reverse=True))
        
        # couldn't do it because can't ensure letters of the same frequency appears in the right order: e.g. lele (freq are 2)
        
        freq, checker = Counter(s), {}
        
        for l, n in freq.items():
            
            checker.setdefault(n, []).append(l*n)
            
        # print checker  #{1: [u'r', u't'], 2: [u'ee']}
        
        return ''.join(''.join(checker[i]) for i in xrange(len(s), 0, -1) if i in checker)
