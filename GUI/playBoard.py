from tkinter import *
from PIL import ImageTk, Image
from copy import deepcopy


class Board:
    def __init__(self):
        self.bg1 = "#39009C"
        self.bg2 = "#250064"

        self.root = Tk()

        # Declares images
        self.images()

        # Declares assets used in the root
        self.root_asset_declaration()

        # Root asset placement
        self.root_asset_placement()

        # board asset initalisation
        self.board_asset_declaration()

        # Board asset placement
        self.board_asset_placement()

        # Icon + title
        self.sys_init()

        self.root.mainloop()

    def images(self):
        # Image declarations
        self.undo = ImageTk.PhotoImage(
            Image.open('imgs\\undo.png').resize((32, 32)))
        self.hint = ImageTk.PhotoImage(
            Image.open('imgs\\hint.png').resize((32, 32)))
        self.icon = ImageTk.PhotoImage(Image.open('imgs\\icon.jpg'))

    def root_asset_declaration(self):

        self.bUndo = Button(self.root, image=self.undo,
                            anchor='e', command=self.undo)
        self.bHint = Button(self.root, image=self.hint, command=self.hint)
        self.bCheck = Button(self.root, text="Check",
                             command=self.check, width=35, height=2)

    def root_asset_placement(self):
        self.bUndo.grid(row=0, column=0)
        self.bHint.grid(row=0, column=4)
        self.bCheck.grid(row=2, column=1)

    def board_asset_declaration(self):
        self.board = LabelFrame(self.root, padx=20, pady=20)
        self.grid = self.initalise_grid()

    def board_asset_placement(self):
        self.board.grid(row=1, column=1, padx=15, pady=15)
        self.place_grid(0, 0)

    def sys_init(self):
        self.root.iconphoto(False, self.icon)
        self.root.title('Board')

    def undo(self):
        pass

    def hint(self):
        pass

    def clear(self):
        first = True
        for i in range(9):
            for j in range(9):
                self.grid[i][j].config(bg=self.bg1 if first else self.bg2)
                first = not first

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

        for i in range(9):
            for j in range(9):
                grid[i][j].bind('<KeyRelease>', lambda event,
                                x=i, y=j: self.maintainStack(x, y))

        return grid

    def maintainStack(self, x, y):
        print(x)
        print(y)
        # print(self.grid[x][y].get())

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
