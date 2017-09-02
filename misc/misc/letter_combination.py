# 17. Letter Combinations of a Phone Number
class Solution(object):
    def letterCombinations(self, digits):

        m = {0:" ", 1:"*", 2:"abc", 3:"def", 4:"ghi", 5:"jkl", \
                 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        if not digits: return []
        ans = [""]
        for i in range(len(digits)):
            x = int(digits[i])
            while len(ans[0]) == i:
                last = ans.pop(0)
                for char in m[x]:
                    ans.append(last + char)
        return ans


class Solution(object):
    def letterCombinations(self, digits):
        '''
        2: "abc"
        3: "def"

        "ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"'''

        if not digits: return []
        def dfs(result, s, i):
            if len(s) == len(digits):
                result.append(s)
                return
            try:
                cur = int(digits[i])
                for l in m[cur]:
                    dfs(result, s + l, i + 1)
            except ValueError:
                raise Exception("Input must be digits!")



        m = {0:" ", 1:"*", 2:"abc", 3:"def", 4:"ghi", 5:"jkl", \
                 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        res = []
        dfs(res, "", 0)

        return res
