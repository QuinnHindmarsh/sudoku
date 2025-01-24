from solve import Solver
from random import randint, choice
from time import time
from copy import deepcopy
# Place a certain amount of random numbers in grid
# Solve
# Remove 4 at a time from the start, then closer to the end only 2 at a time. check for more then one solution after each set of removal
# If ever more then one solution, undo move
# Before checking the solution count check if it conforms to certain rules. at least 8 unique nums. + distabuition rules

# If it gets to 27 with these rules being correct, return this



class GenerateBoard:
    def __init__(self):
        self.solver = Solver()



    def digging(self,h,n=11, maxTime=30):
        self.board = self.base_solution(n)
        startTime = time()
        rem = 81

        if h < 17:
            return False

        while rem > h:
            i = 0
            tempBoard = deepcopy(self.board)    
            # Remove 4 this itteration
            if rem > 40:
                remove = min(4, rem-h)
            else:
                remove = min(2, rem-h)

            while i < remove:
                x,y = randint(0,8), randint(0,8)

                while tempBoard[x][y] != '.':
                    x,y = randint(0,8), randint(0,8)
                
                tempBoard[x][y] = '.'

                i += 1
            
            tempBoard2 = deepcopy(tempBoard)
            if self.solver.solveSudoku(tempBoard2)[0]:
                self.board = deepcopy(tempBoard)
                rem -= remove

        return self.board



            # Remove 2 this itteration

        
    def candidates(self, i, j):
        cand = []
        for k in range(1, 10):
            s = str(k)
            if s not in self.__rows[i] and s not in self.__cols[j] and s not in self.__sqr[i//3][j//3]:
                cand.append(s)

        return cand

    
    def base_solution(self,n):
        # This will be inacurate after recursion
        self.__board = [['.'] * 9 for _ in range(9)]
        self.__rows = [set() for _ in range(9)]
        self.__cols = [set() for _ in range(9)]
        self.__sqr = [[set() for _ in range(3)] for _ in range(3)]
        #Populate start of board
        i = 0

        while i < n:
            x,y = randint(0,8), randint(0,8)

            if self.__board[x][y] == '.':
                i += 1
                cand = self.candidates(x,y)

                if len(cand) == 0:
                    return self.base_solution(n)

                rand = choice(cand)
                self.__rows[x].add(rand)
                self.__cols[y].add(rand)
                self.__sqr[x//3][y//3].add(rand)
                self.__board[x][y] = str(rand)

        # If the board has no solution then it will call recurisvly 
        # Edits board in memory so completed board is returned 
        if not self.solver.solveSudoku(self.__board,maxTime=2)[1]:
            return self.base_solution(n)
        
        return self.__board





boardGen = GenerateBoard()




start_time = time()
borad = boardGen.digging(30)
print("Process finished --- %s seconds ---" % (time() - start_time))
print(borad)

# TODO 
# create method for digging 
# Singleton pattern