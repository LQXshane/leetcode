class Solution:
    # @param {string} s  an expression includes numbers, letters and brackets
    # @return {string} a string
    def expressionExpand(self, s):
        # Write your code here
        stack = []
        i = len(s) - 1
        tmp = ''
        while i >= 0:
            stack.append(s[i])
            if s[i] == '[':
                stack.pop()
                while stack[-1] != ']':
                    tmp += stack.pop()
                stack.pop()
            if s[i].isdigit():
                stack.pop()
                j = i
                while s[j].isdigit():
                    j -= 1
                num = int(s[j+1:i+1])
                tmp = tmp * num
                stack.append(tmp)
                tmp = ''
                i = j + 1
            # print stack
            i -= 1
            
        return ''.join(x for x in stack[::-1])
                
