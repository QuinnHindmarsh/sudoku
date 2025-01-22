import csv
import time


def make_board(s):
    b = [['.'] * 9 for _ in range(9)]
    i = j = k = 0

    for i in range(9):
        for j in range(9):
            if s[k] != '0':
                b[i][j] = s[k]
            k += 1
    return b


processedBoards = []


start_time = time.time()
with open('dev tools\\SudokuProcessing\\sudoku.csv', 'r') as boards:
    boards = csv.reader(boards)
    i = 0
    # Skips first line
    next(boards)

    for line in boards:
        processedBoards.append(make_board(line[0]))
print("Process finished --- %s seconds ---" % (time.time() - start_time))

with open('formatedBoards.py', 'w') as formated:
    formated.write(str(processedBoards))


print("Process finished --- %s seconds ---" % (time.time() - start_time))
