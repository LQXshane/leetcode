# 22. Generate Parentheses
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.backtrack(n, res, "", 0, 0)
        return res

    def backtrack(self, num, resList, cur, open, close):
        if len(cur) == num * 2:
            resList.append(cur)
            return

        if open < num:
            self.backtrack(num, resList, cur + "(", open + 1, close)
        if close < open:
            self.backtrack(num, resList, cur + ")", open, close + 1)
