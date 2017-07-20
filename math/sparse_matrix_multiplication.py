
class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        row, n, col = len(A), len(B), len(B[0])
        res = [[0 for _ in xrange(col)] for _ in xrange(row)]
        
        
        for i, r in enumerate(A):
            for k, a in enumerate(r):
                if a:
                    for j, b in enumerate(B[k]):
                        if b: res[i][j] += a * b
        return res
