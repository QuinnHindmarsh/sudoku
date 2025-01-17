from tkinter import *

root = Tk()
root.title('Calculator')


def button_click(opp):
    cur = numEntry.get()
    numEntry.delete(0, END)
    numEntry.insert(0, str(cur) + str(opp))


def eq():
    equation = numEntry.get()
    numEntry.delete(0, END)
    numEntry.insert(0, eval(equation))


numEntry = Entry(root, width=35, borderwidth=5)
numEntry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# numEntry.insert(2, "Enter numbers")


b0 = Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
b1 = Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
b2 = Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
b3 = Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
b4 = Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
b5 = Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
b6 = Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
b7 = Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
b8 = Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
b9 = Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))

bAdd = Button(root, text='+', padx=39, pady=20,
              command=lambda: button_click('+'))
bMinus = Button(root, text='-', padx=39, pady=20,
                command=lambda: button_click('-'))
bMulti = Button(root, text='x', padx=39, pady=20,
                command=lambda: button_click('*'))
bDiv = Button(root, text='/', padx=39, pady=20,
              command=lambda: button_click('/'))
bMod = Button(root, text='%', padx=39, pady=20,
              command=lambda: button_click('%'))

bEqual = Button(root, text='=', padx=87, pady=20,
                command=eq)
bClear = Button(root, text='Clear', padx=175, pady=20,
                command=lambda: numEntry.delete(0, END))

b0.grid(row=1, column=0)
b1.grid(row=1, column=1)
b2.grid(row=1, column=2)
bAdd.grid(row=1, column=3)

b3.grid(row=2, column=0)
b4.grid(row=2, column=1)
b5.grid(row=2, column=2)
bMinus.grid(row=2, column=3)

b6.grid(row=3, column=0)
b7.grid(row=3, column=1)
b8.grid(row=3, column=2)
bMulti.grid(row=3, column=3)

b9.grid(row=4, column=0)
bEqual.grid(row=4, column=1, columnspan=2)
bDiv.grid(row=4, column=3)

bClear.grid(row=5, column=0, columnspan=4)


root.mainloop()
