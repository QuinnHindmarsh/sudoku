from time import time
from copy import deepcopy
from pprint import pp
# Edits board in memory
class Solver:
    def solveSudoku(self, board, maxTime=float('inf')) -> None:
        self.solved = False
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.sqr = [[set() for _ in range(3)] for _ in range(3)]
        self.sol = None
        self.board = board
        # I will use for timeouts later
        self.startTime = time()
        self.maxTime = maxTime

        # Populates sets
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n == '.':
                    continue

                if n in self.rows[i] or n in self.cols[j] or n in self.sqr[i//3][j//3]:
                    return (False, None, False)

                self.rows[i].add(n)
                self.cols[j].add(n)
                self.sqr[i//3][j//3].add(n)

        return self.backtrack()

    def candidates(self, i, j):
        cand = []
        for k in range(1, 10):
            s = str(k)
            if s not in self.rows[i] and s not in self.cols[j] and s not in self.sqr[i//3][j//3]:
                cand.append(s)

        return cand
    
    def check_solved(self):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == '.':
                    return False
        return True

    def backtrack(self, i=0, j=0):
        if time() - self.startTime > self.maxTime:
            return (False, self.sol)

        while i < 9 and self.board[i][j] != '.':
            j += 1
            if j == 9:
                j = 0
                i += 1

        if i == 9:
            if self.solved:
                return False
            self.sol = deepcopy(self.board)
            self.solved = True
            return (True, self.board)

        cand = self.candidates(i, j)
        for c in cand:
            self.board[i][j] = c
            self.rows[i].add(c)
            self.cols[j].add(c)
            self.sqr[i//3][j//3].add(c)

            if not self.backtrack(i, j):
                return (False, self.sol)

            self.board[i][j] = '.'
            self.rows[i].remove(c)
            self.cols[j].remove(c)
            self.sqr[i//3][j//3].remove(c)
        return (self.solved, self.sol)


# solver = Solver()
# start_time = time()


# b =  [
#             ['.', '.', '.',     '.', '.', '.',    '.', '1', '2'],
#             ['.', '.', '.',     '.', '3', '5',    '.', '.', '.'],
#             ['.', '.', '.',     '6', '.', '.',    '.', '7', '.'],

#             ['7', '.', '.',     '.', '.', '.',    '3', '.', '.'],
#             ['.', '.', '.',     '4', '.', '.',    '8', '.', '.'],
#             ['1', '.', '.',     '.', '.', '.',    '.', '.', '.'],

#             ['.', '.', '.',     '1', '2', '.',    '.', '.', '.'],
#             ['.', '8', '.',     '.', '.', '.',    '.', '4', '.'],
#             ['.', '5', '.',     '.', '.', '.',    '6', '.', '.']
#         ]

# b = [['.', '.', '1', '9', '.', '.', '.', '.', '.'],
#  ['.', '.', '.', '.', '.', '.', '5', '.', '7'],
#  ['3', '.', '8', '.', '.', '.', '.', '.', '.'],
#  ['.', '.', '.', '.', '9', '.', '.', '.', '4'],
#  ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#  ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#  ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
#  ['.', '.', '.', '.', '5', '.', '.', '.', '.'],
#  ['7', '.', '.', '.', '.', '.', '.', '4', '.']]




# pp(solver.solveSudoku(b,maxTime=30))
# print("Process finished --- %s seconds ---" % (time() - start_time))

# #TODO 
# Optimise? switch to str

