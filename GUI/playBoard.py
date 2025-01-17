from tkinter import *
from PIL import ImageTk, Image
from copy import deepcopy


class Board:
    def __init__(self):
        # Declares all variables + assests
        self.declarations()

        # Places all variables + assets on game board/root window
        self.placements()

        self.root.mainloop()

    def declarations(self):
        # Var declarations
        self.bg1 = "#39009C"
        self.bg2 = "#250064"

        # Image declarations
        self.undo = ImageTk.PhotoImage(
            Image.open('imgs\\undo.png').resize((32, 32)))
        self.hint = ImageTk.PhotoImage(
            Image.open('imgs\\hint.png').resize((32, 32)))
        self.icon = ImageTk.PhotoImage(Image.open('imgs\\icon.jpg'))

        # Root asset declarations
        self.root = Tk()
        self.bUndo = Button(self.root, image=self.undo,
                            anchor='e', command=self.undo)
        self.bHint = Button(self.root, image=self.hint, command=self.hint)
        self.bCheck = Button(self.root, text="Check",
                             command=self.check, width=35, height=2)

        # Game board asset declaration
        self.board = LabelFrame(self.root, padx=20, pady=20)
        self.grid = self.initalise_grid()

    def placements(self):
        # Icon + title setup
        self.root.iconphoto(False, self.icon)
        self.root.title('Board')

        # Root placements
        self.bUndo.grid(row=0, column=0)
        self.bHint.grid(row=0, column=4)
        self.bCheck.grid(row=2, column=1)

        # Game board placements
        self.board.grid(row=1, column=1, padx=15, pady=15)
        # Places grid squares starting from 0,0 in the grid
        self.place_grid(0, 0)

    def undo(self):
        pass

    def hint(self):
        pass

    # Resets all game squares to origonal colour
    def clear(self):
        first = True
        for i in range(9):
            for j in range(9):
                self.grid[i][j].config(bg=self.bg1 if first else self.bg2)
                first = not first

    # Finds squares that are not valid, highlights them red
    def check(self):
        board = [[""]*9 for _ in range(9)]
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        squares = [[{} for _ in range(3)]for __ in range(3)]

        self.clear()

        for i in range(9):
            for j in range(9):
                board[i][j] = self.grid[i][j].get()

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

    # Declares all grid square. Uses factory pattern to ensure all instances are unique.
    def initalise_grid(self):
        def s1():
            return Entry(self.board, font=('Helvetica', 50),
                         width=2, fg='white', bg=self.bg1)

        def s2():
            return Entry(self.board, font=('Helvetica', 50),
                         width=2, fg='white', bg=self.bg2)

        # Row style 1 - [s1(), s2(), s1(), s2(), s1(), s2(), s1(), s2(), s1()]
        # Row style 2 - [s2(), s1(), s2(), s1(), s2(), s1(), s2(), s1(), s2()]

        grid = []

        # First 8 rows
        for i in range(4):
            grid.append([s1(), s2(), s1(), s2(), s1(), s2(), s1(), s2(), s1()])
            grid.append([s2(), s1(), s2(), s1(), s2(), s1(), s2(), s1(), s2()])
        # Last row
        grid.append([s1(), s2(), s1(), s2(), s1(), s2(), s1(), s2(), s1()])

        # Sets up binds in a way where we get the index of the location the event was trigered
        # They are used to maintain a stack of alterations for undo function
        for i in range(9):
            for j in range(9):
                grid[i][j].bind('<KeyRelease>', lambda event,
                                x=i, y=j: self.maintainStack(x, y))

        return grid

    def maintainStack(self, x, y):
        print(x)
        print(y)
        # print(self.grid[x][y].get())

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


board = Board()
