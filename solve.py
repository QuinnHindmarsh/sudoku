# Do singleton. add driver code
import time
from copy import deepcopy


class Solver:
    def solveSudoku(self, board) -> None:
        self.solved = False
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.sqr = [[set() for _ in range(3)] for _ in range(3)]
        self.sol = None
        self.board = board

        # Populates sets
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n == '.':
                    continue

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
        i = j = None
        minCands = 10
        cand = []

        # Choses most constrained square
        for ii in range(8):
            for jj in range(8):
                if self.board[ii][jj] == '.':
                    temp_cand = self.candidates(ii,jj)
                    if len(temp_cand) < minCands:
                        minCands = len(temp_cand)
                        cand = temp_cand
                        # Not possible to solve
                        if minCands == 0:
                            break

                        i = ii
                        j = jj

        if i == None:
            if self.check_solved():
                if self.solved:
                    return False
                self.sol = deepcopy(self.board)
                self.solved = True
                return (True, self.board)
            return (True, self.sol)

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
# start_time = time.time()

# b = [
#     ['.', '.', '.',     '.', '.', '.',    '.', '1', '2'],
#     ['.', '.', '.',     '.', '3', '5',    '.', '.', '.'],
#     ['.', '.', '.',     '6', '.', '.',    '.', '7', '.'],

#     ['7', '.', '.',     '.', '.', '.',    '3', '.', '.'],
#     ['.', '.', '.',     '4', '.', '.',    '8', '.', '.'],
#     ['1', '.', '.',     '.', '.', '.',    '.', '.', '.'],

#     ['.', '.', '.',     '1', '2', '.',    '.', '.', '.'],
#     ['.', '8', '.',     '.', '.', '.',    '.', '4', '.'],
#     ['.', '5', '.',     '.', '.', '.',    '6', '.', '.']
# ]


# print(solver.solveSudoku(b))
# print("Process finished --- %s seconds ---" % (time.time() - start_time))
