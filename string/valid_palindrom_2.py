# 680. Valid Palindrom 2

class Solution(object):
    def validPalindrome(self, s):

        def dfs(start, end, count):
            if count > 1: return False
            while start < end:
                if s[start] != s[end]:
                    return dfs(start + 1, end, count + 1) or dfs(start, end - 1, count + 1)
                start += 1
                end -= 1
            return True

        return dfs(0, len(s) - 1, 0)

# O(n) since each letter is checked excatly once
# O(1) since recursion depth is maximum 2
