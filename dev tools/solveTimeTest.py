from solve import Solver
import time
from oneHundredK import boards
solver = Solver()

start_time = time.time()
for b in boards:
    solver.solveSudoku(b)

print("Process finished --- %s seconds ---" % (time.time() - start_time))

# 80.86 seconds for 100k boards
