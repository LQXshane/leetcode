# 348. Deisgn Tic-Tac-Toe

class TicTacToe(object):



    def __init__(self, n):
        """
        Initialize your data structure here.
        :type n: int
        """
        self.rows = [0 for _ in xrange(n)]
        self.cols = [0 for _ in xrange(n)]
        self.n = n
        self.diagonal, self.antidiagonal = 0, 0



    def move(self, row, col, player):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        if player == 1:
            add = 1
        else:
            add = -1
        self.rows[row] += add
        self.cols[col] += add
        if row == col:
            self.diagonal += add
        if row + col == self.n - 1:
            self.antidiagonal += add
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or \
            abs(self.diagonal) == self.n or abs(self.antidiagonal) == self.n:
                # print self.rows, self.cols, self.diagonal, self.antidiagonal
                return player
        return 0
