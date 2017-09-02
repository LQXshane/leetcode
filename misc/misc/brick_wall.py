# 554. Brick Wall
class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        d = {}
        for i in range(len(wall)):
            cur = 0
            for j in range(len(wall[i])-1):
                cur += wall[i][j]
                if cur not in d:
                    d[cur] = 0
                d[cur] += 1

        return len(wall) - max(d.values()) if d else len(wall)
