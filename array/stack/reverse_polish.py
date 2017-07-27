# 150. Reverse Polish Notation
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens: return 0
        stack = []
        a, b = 0, 0
        for x in tokens:
            stack.append(x)
            if stack[-1] in ["+", "-", "*", "/"]:
                op = stack.pop()
                a = int(stack.pop())
                b = int(stack.pop())
                if op == "+":
                    stack.append(b + a)
                elif op == "-":
                    stack.append(b - a)
                elif op == "*":
                    stack.append(b * a)
                else:
                    if b * a < 0 and b % a != 0:
                        stack.append(b / a + 1)
                    else:
                        stack.append(b / a)
            # print stack
        return int(stack.pop())
