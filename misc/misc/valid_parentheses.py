# class Solution(object):
#     def isValid(self, s):
#         close = {"]": "[", "}": "{", ")": "("}
#         if not s: return True
#         stack = []
#         for char in s:
#             if char in close and stack and close[char] == stack[-1]:
#                 stack.pop()
#             else:
#                 stack.append(char)
#             # print stack
#         return not stack

# 32. Longest Valid Parentheses

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i, p in enumerate(s):
            if p == ")" and stack and s[stack[-1]] == "(":
                stack.pop()
            else:
                stack.append(i)
        # print stack
        if not stack: return len(s)
        end = len(s)
        ans = 0
        while stack:
            start = stack.pop()
            ans = max(ans, end - start - 1)
            end = start
        ans = max(ans, end)
        return ans

# 301. Remove Invalid Parentheses
'''BFS'''
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """

        def isValid(string):
            count = 0
            for char in string:
                if char == "(": count += 1
                if char == ")":
                    count -= 1
                    if count < 0: return False
            return count == 0
        q = [s]
        res = []
        found = False
        t = ""
        visited = set()
        visited.add(s)
        while q:
            cur = q.pop(0)
            if isValid(cur):
                res.append(cur)
                found = True
            if found: continue
            for i in range(len(cur)):
                if cur[i] not in "()":
                    continue
                t = cur[:i] + cur[i+1:]
                if t not in visited:
                    visited.add(t)
                    q.append(t)
            # print res, q
        return res or [""]

'''DFS'''
class Solution(object):

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.remove(s, ans, 0, 0, "()")
        return ans

    def remove(self, string, res, last_i, last_j, pair):
        count = 0
        for i in range(last_i, len(string)):
            if string[i] == pair[0]: count += 1
            if string[i] == pair[1]: count -= 1
            if count >= 0:
                continue
            for j in range(last_j, i + 1):
                if string[j] == pair[1] and (j == last_j or string[j-1] != pair[1]):
                    self.remove(string[:j] + string[j+1:], res, i, j, pair)
            return
        reversed = string[::-1]
        if pair == "()":
            self.remove(reversed, res, 0, 0, ")(")
        else:
            res.append(reversed)
