# 127. Word Ladder

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList: return 0
        front, back = [beginWord], [endWord]
        n, length = len(beginWord), 1
        while front and back:
            # print front, back
            if len(front) > len(back):
                front, back = back, front
            search = []
            for cur in front:
                for i in range(n):
                    for x in range(97, 123):
                        next = cur[:i] + chr(x) + cur[i+1:]
                        if next in wordList and next not in front:
                            # wordList.remove(next)
                            if next not in back:
                                search += next,
                            else:
                                return length + 1
            # print wordList
            # print search
            if not search: return 0
            for x in search:
                if x not in front: front += x,
            length += 1
