from solve import Solver
from random import randint
import time
# Place a certain amount of random numbers in grid
# Solve
# Remove 4 at a time from the start, then closer to the end only 2 at a time. check for more then one solution after each set of removal
# If ever more then one solution, undo move
# Before checking the solution count check if it conforms to certain rules. at least 8 unique nums. + distabuition rules

# If it gets to 27 with these rules being correct, return this



class GenerateBoard:
    def __init__(self):
        self.solver = Solver()
    
    def base_solution(self,n):
        self.board = [['.'] * 9 for _ in range(9)]
        #Populate start of board
        i = 0
        while i < n:
            x,y,rand = randint(0,8), randint(0,8), randint(0,8)

            i += 1 if self.board[x][y] == '.' else 0
            self.board[x][y] = str(rand)

        start_time = time.time()
        print(n)
        print(self.solver.solveSudoku(self.board))
        print("Process finished --- %s seconds ---" % (time.time() - start_time))


boardGen = GenerateBoard()

boardGen.base_solution(28)