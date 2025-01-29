from tkinter import *
from PIL import ImageTk, Image
from solve import Solver
from boardGeneration import Generator
from playBoard import Board as PlayBoard
from copy import deepcopy

class Menu:
    def __init__(self):
        self.declarations()
        self.placements()

        self.root.mainloop()

    def declarations(self):
        # Var declarations
        self.ezColour = "#1CBABA"
        self.medColour = "#F2942E"
        self.hardColour = "#F63737"
        self.path = "Imgs\\"
        
        # Instance declarations
        self.solver = Solver()
        self.generator = Generator()
        
        # Asset declarations
        self.root = Tk()
        self.bEasy = Button(self.root, bg=self.ezColour, width=150, height=5, text='Easy', command=lambda: self.play(49))
        self.bMed = Button(self.root, bg=self.medColour, width=150, height=5, text='Meduim', command=lambda: self.play(35))
        self.bHard = Button(self.root, bg=self.hardColour, width=150, height=5, text='Hard', command=lambda: self.play(22))
        self.imgIcon = ImageTk.PhotoImage(
            Image.open(self.path + 'icon.jpg'))

    def placements(self):
        self.root.iconphoto(False, self.imgIcon)
        self.root.title('Menu')

        self.bEasy.grid(row=1, column=1)
        self.bMed.grid(row=2,column=1)
        self.bHard.grid(row=3,column=1)
    
    def play(self, n):
        board = self.generator.generate(h=n)
        # Board itself without True/False - prevents the origonal board from being changed
        sol = self.solver.solveSudoku(deepcopy(board))[1]
        # switch to playBoard.py
        self.root.destroy()
        play = PlayBoard(board, sol)

        

menu = Menu()
