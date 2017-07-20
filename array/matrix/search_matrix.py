
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]: return False
        row = 0
        col = len(matrix[0])-1
 
        while row< len(matrix) and col>=0:
            if target == matrix[row][col]:
                return True
            elif matrix[row][col]<target:
                row += 1
            else:
                col -= 1
        return False
        
