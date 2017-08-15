# bfs
class Solution(object):
    def minMutation(self, start, end, bank):
        visited = [start]
        queue = [(start, 0)]
        while queue:
            cur, n = queue.pop(0) # pop from the left
            if cur == end: return n
            for i, x in enumerate(cur):
                for c in "AGCT":
                    next = cur[:i] + c + cur[i + 1:]
                    if next not in visited and next in bank:
                        visited += next,
                        queue += (next, n + 1),
        return -1


# dfs
# why doesn't it work?

class Solution(object):

    def minMutation(self, start, end, bank):
        self.bank, self.end = bank, end
        self.ans = float("inf")
        self.visited = {g: False for g in self.bank}
        self.dfs(start, 0)
        return self.ans if self.ans < float("inf") else -1

    def dfs(self, cur, n):
        if cur == self.end:
            self.ans = min(self.ans, n)
            return
        for y in "AGCT":
            for i, x in enumerate(cur):
                next = cur[:i] + y + cur[i + 1:]
                if next in self.bank and not self.visited[next]:
                    self.visited[next] = True; n += 1
                    self.dfs(next, n)
                    # rewind
                    n -= 1; self.visited[next] = False
