from solve import Solver
from random import randint, choice
from time import time
from copy import deepcopy
from pprint import pp

class Generator:
    def __init__(self):
        self.solver = Solver()


    # Uses "digging" technique to generate a board with a single solution containing h clues
    def generate(self,h,n=11, maxTime=30):
        self.board = self.base_solution(n)
        startTime = time()
        rem = 81

        # Not possible to have unique solutions with less then 17 clues
        if h < 17:
            return False

        while rem > h:
            if time() - startTime > maxTime:
                return self.generate(h,n,maxTime)
            
            
            i = 0
            tempBoard = deepcopy(self.board)    
            # Remove 4 this itteration
            if rem > 40:
                remove = min(4, rem-h)
            else:
            # Remove 2 this itteration
                remove = min(2, rem-h)

            while i < remove:

                x,y = randint(0,8), randint(0,8)

                while tempBoard[x][y] == '.':
                    x,y = randint(0,8), randint(0,8)
                
                tempBoard[x][y] = '.'
                i += 1
            
            tempBoard2 = deepcopy(tempBoard)
            if self.solver.solveSudoku(tempBoard2)[0]:
                self.board = deepcopy(tempBoard)
                rem -= remove

        return self.board



        

        
    def candidates(self, i, j):
        cand = []
        for k in range(1, 10):
            s = str(k)
            if s not in self.__rows[i] and s not in self.__cols[j] and s not in self.__sqr[i//3][j//3]:
                cand.append(s)

        return cand

    
    def base_solution(self,n):
        if n > 25 or n <= -1:
            return [[]]

        
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
                # print(cand)

                if len(cand) == 0:
                    return self.base_solution(n)

                rand = choice(cand)
                self.__rows[x].add(rand)
                self.__cols[y].add(rand)
                self.__sqr[x//3][y//3].add(rand)
                self.__board[x][y] = str(rand)
        # If the board has no solution then it will call recurisvly 
        # Edits board in memory so completed board is returned 

        res = self.solver.solveSudoku(self.__board)[1]
        if res:
            return res
        return self.base_solution(n)


        



boardGen = Generator()





# start_time = time()
# board = boardGen.base_solution(25)
# print("Process finished --- %s seconds ---" % (time() - start_time))
# pp(board)

