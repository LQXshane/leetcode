# 227. Basic Calculator
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack, num, sign = [], 0, "+"
        
        for i in xrange(len(s)):
            cur = s[i]
            if cur.isdigit():
                num = 10 * num + int(cur)
            if (not cur.isdigit() and not cur.isspace()) or i==len(s)-1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop()*num)
                else: # division
                    pre = stack.pop()
                    if pre//num < 0 and pre%num != 0:
                        stack.append(pre//num+1)
                    else:
                        stack.append(pre//num)
                sign = cur
                num = 0
                
        return sum(stack)
        
