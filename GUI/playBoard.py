from tkinter import *
from PIL import ImageTk, Image
from copy import deepcopy


class Board:
    def __init__(self):
        self.bg1 = "#39009C"
        self.bg2 = "#250064"

        self.root = Tk()

        # Image declarations
        self.undo = ImageTk.PhotoImage(
            Image.open('imgs\\undo.png').resize((32, 32)))
        self.hint = ImageTk.PhotoImage(
            Image.open('imgs\\hint.png').resize((32, 32)))
        self.icon = ImageTk.PhotoImage(Image.open('imgs\\icon.jpg'))

        # Root asset initalisation
        self.bUndo = Button(self.root, image=self.undo,
                            anchor='e', command=self.undo)
        self.bHint = Button(self.root, image=self.hint, command=self.hint)

        # Icon + title
        self.root.iconphoto(False, self.icon)
        self.root.title('Board')

        # board asset initalisation
        self.board = LabelFrame(self.root, padx=300, pady=300)
        self.grid = self.initalise_grid()

        # Root asset placement
        self.bUndo.grid(row=0, column=0)
        self.bHint.grid(row=0, column=4)

        # Board asset placement
        self.board.grid(row=1, column=1)
        self.place_grid(1, 2)

        self.root.mainloop()

    def undo(self):
        pass

    def hint(self):
        pass

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

        return grid

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
