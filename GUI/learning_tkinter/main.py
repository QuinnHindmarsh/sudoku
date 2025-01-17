from tkinter import *

# Base window
root = Tk()
e = Entry(root, width=50)
e.pack()
e.insert(0, "Deafult text")


def OnClick():
    ml = Label(root, text=e.get())
    ml.pack()


myButton = Button(root, text="enter", command=OnClick)


myButton.pack()
root.mainloop()
