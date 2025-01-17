from tkinter import *

# Base window
root = Tk()

# Simple text
myLabal1 = Label(root, text="Hello World")
myLabal1.grid(row=0, column=0)
# You can also do myLabel1.pack()

# Runs the GUI
root.mainloop()


def onClick():
    myLabel = Label(root, text="You clicked")
    myLabel.grid(row=1, column=0)


# fore ground colour, background colour, pading for the x cords, poadding for y cords
myButton = Button(root, text="idk", padx=50, pady=50,
                  command=onClick, fg="ffffff", bg="000000")


e = Entry(root, width=50)
e.pack()
e.insert(0, "Deafult text")


def OnClick():
    ml = Label(root, text=e.get())
    ml.pack()


myButton = Button(root, text="enter", command=OnClick)
