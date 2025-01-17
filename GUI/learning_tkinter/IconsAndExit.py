from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('practicing gui')

img = ImageTk.PhotoImage(Image.open('img\\icon.jpg'))
root.iconphoto(False, img)

bExit = Button(root, text='idk', command=root.quit)


li = Label(image=img)
li.pack()
bExit.pack()
root.mainloop()
