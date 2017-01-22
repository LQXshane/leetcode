# Idea from discussion board


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        m, len_of_path = 0, {0: 0}  # dictionary
        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)
            if '.' in name:
                m = max(m, len_of_path[depth] + len(name))
            else:
                # DP
                len_of_path[depth + 1] = len_of_path[depth] + len(name) + 1

        return m