from tkinter import *
from PIL import ImageTk, Image
from collections import deque
from random import randint


class Board:
    def __init__(self, BOARD, SOLUTION):
        # Declares all variables + assests
        self.BOARD = BOARD
        self.SOLUTION = SOLUTION

        self.declarations()

        # Places all variables + assets on game board/root window
        self.placements()

        self.root.mainloop()

    def declarations(self):
        # Var declarations
        self.states = {}
        self.dq = deque()
        self.bg1 = "#39009C"
        self.bg2 = "#250064"
        self.readOnlyColour = "#03452a"
        self.path = "Imgs\\"

        self.root = Tk()

        # Image declarations
        self.imgUndo = ImageTk.PhotoImage(
            Image.open(self.path + 'undo.png').resize((32, 32)))
        self.imgHint = ImageTk.PhotoImage(
            Image.open(self.path + 'hint.png').resize((32, 32)))
        self.imgIcon = ImageTk.PhotoImage(
            Image.open(self.path + 'icon.jpg'))
        self.imgBack = ImageTk.PhotoImage(
            Image.open(self.path + 'back.png').resize((32, 32)))

        # Root asset declarations
        self.bUndo = Button(self.root, image=self.imgUndo,
                            anchor='e', command=self.undo)
        self.bHint = Button(self.root, image=self.imgHint, command=self.hint)
        self.bCheck = Button(self.root, text="Check",
                             command=self.check, width=35, height=2)
        self.bBack = Button(self.root, image=self.imgBack, command=self.back)
        self.bClear = Button(self.root, text="Clear",
                             command=self.clear, width=25)

        # Game board asset declaration
        self.board = LabelFrame(self.root, padx=20, pady=20)
        self.grid = self.initalise_grid()

    def placements(self):
        # Icon + title setup
        self.root.iconphoto(False, self.imgIcon)
        self.root.title('Board')

        # Root placements
        self.bUndo.grid(row=0, column=3)
        self.bHint.grid(row=0, column=4)
        self.bCheck.grid(row=2, column=1)
        self.bBack.grid(row=0, column=0)
        self.bClear.grid(row=0, column=1, columnspan=2)

        # Game board placements
        self.board.grid(row=1, column=1, padx=15, pady=15)
        # Places grid squares starting from 0,0 in the grid
        self.place_grid(0, 0)

    # Need to do algorithim before this
    def hint(self):
        board = self.get_board()
        i = randint(0, 8)
        j = randint(0, 8)

        while board[i][j] != '':
            i = randint(0, 8)
            j = randint(0, 8)

        self.grid[i][j].insert(0, self.SOLUTION[i][j])
        self.grid[i][j].config(state='readonly')

    # Need to do after main page

    def back(self):
        pass

    def clear(self):
        for i in range(9):
            for j in range(9):
                # I will need to update this to not delete letters part of the actual sudkou
                self.grid[i][j].delete(0, END)

    # Resets all game squares to origonal colour
    def colour_clear(self):
        first = True
        for i in range(9):
            for j in range(9):
                self.grid[i][j].config(bg=self.bg1 if first else self.bg2)
                first = not first

    def get_board(self):
        board = [[""]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                board[i][j] = self.grid[i][j].get()
        return board

    # Finds squares that are not valid, highlights them red
    def check(self):
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        squares = [[{} for _ in range(3)]for __ in range(3)]

        self.colour_clear()
        board = self.get_board()

        for i in range(9):
            for j in range(9):
                val = board[i][j]

                if val == "":
                    continue

                if len(val) > 1 or val not in '123456789':
                    self.grid[i][j].config(bg='red')
                    continue

                if val not in rows[i]:
                    rows[i][val] = (i, j)
                else:
                    x, y = rows[i][val]
                    self.grid[x][y].config(bg='red')
                    self.grid[i][j].config(bg='red')

                if board[i][j] not in cols[j]:
                    cols[j][val] = (i, j)
                else:
                    x, y = cols[j][val]
                    self.grid[x][y].config(bg='red')
                    self.grid[i][j].config(bg='red')

                if val not in squares[i//3][j//3]:
                    squares[i//3][j//3][val] = (i, j)
                else:
                    x, y = squares[i//3][j//3][val]
                    self.grid[x][y].config(bg='red')
                    self.grid[i][j].config(bg='red')

        if board == self.SOLUTION:
            print(1)
            # Bring popup screen with option to go back to main menue

    # Declares all grid square. Uses factory pattern to ensure all instances are unique.
    def initalise_grid(self):
        def s1():
            return Entry(self.board, font=('Helvetica', 50),
                         width=2, fg='white', bg=self.bg1, readonlybackground=self.readOnlyColour)

        def s2():
            return Entry(self.board, font=('Helvetica', 50),
                         width=2, fg='white', bg=self.bg2, readonlybackground=self.readOnlyColour)

        # # Row style 1 - [s1(), s2(), s1(), s2(), s1(), s2(), s1(), s2(), s1()]
        # # Row style 2 - [s2(), s1(), s2(), s1(), s2(), s1(), s2(), s1(), s2()]

        grid = [[None]*9 for _ in range(9)]
        first_colour = True

        # Sets up binds in a way where we get the index of the location the event was trigered
        for i in range(9):
            for j in range(9):
                grid[i][j] = s1() if first_colour else s2()
                first_colour = not first_colour

                if self.BOARD[i][j] != '.':
                    grid[i][j].insert(0, self.BOARD[i][j])
                    grid[i][j].config(state='readonly')

                else:
                    grid[i][j].bind('<Button>', lambda event,
                                    x=i, y=j: self.record_state(x, y))
                    grid[i][j].bind('<KeyRelease>', lambda event,
                                    x=i, y=j: self.maintain_stack(x, y))

        return grid

    # Records state before being altered to allow for undos
    def record_state(self, x, y):
        self.states[(x, y)] = self.grid[x][y].get()

    # Adds each move to a deqeue to allow for undos
    def maintain_stack(self, x, y):
        prev = self.states.get((x, y), "")
        self.dq.append((x, y, prev))

        # Saves memory by not storing every move ever made
        while len(self.dq) > 100:
            self.dq.popleft()

    def undo(self):
        if len(self.dq) == 0:
            return

        x, y, prev = self.dq.pop()
        self.grid[x][y].delete(0, END)
        self.grid[x][y].insert(0, prev)

    # Places the each element of the grid in the game board
    def place_grid(self, sr, sc):  # Start row, start column
        n = 9
        r, c = sr, sc
        for i in range(n):
            c = sc
            for j in range(n):
                self.grid[i][j].grid(row=r, column=c)
                c += 1
            r += 1


b = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                  ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
s = [["5", "3", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"], ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"], ["4", "2", "6", "8",
                                                                                                                                                                                                  "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"], ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"], ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]

board = Board(b, s)


# TODO
# Make home page
# Add link back to home page
# Win popup

