# 71. simplify path


class Solution(object):
    def simplifyPath(self, path):
        folders = [x for x in path.split("/") if x != "." and x != ""]
        stack = []
        for x in folders:
            if x == "..": # to the previous folder
                if stack: stack.pop()
            else:
                stack.append(x)
        # print stack
        return "/" + "/".join(stack)
