class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ans, self.target = [], target
        for i in range(1, len(num) + 1):
            if i == 1 or (i > 1 and num[0] != '0'):
                self.helper(num[i:], num[:i], int(num[:i]), int(num[:i]), ans)
        return ans


    def helper(self, num, tmp, cur, last, res):
        """
        :type tmp: str, current string
        """
        if not num and self.target == cur:
            res.append(tmp)
            return 
        
        for i in range(1, len(num) + 1):
            # print len(num), i 
            if i == 1 or ( i > 1 and num[0] != '0'):
                self.helper(num[i:], tmp + "+" + num[:i], cur + int(num[:i]), int(num[:i]), res)
                self.helper(num[i:], tmp + "-" + num[:i], cur - int(num[:i]), - int(num[:i]), res)
                self.helper(num[i:], tmp + "*" + num[:i], cur - last + last * int(num[:i]) , last * int(num[:i]), res)
