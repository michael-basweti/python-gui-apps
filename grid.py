from tkinter import *

root = Tk()

label = Label(root, text="Hello World")
label2 = Label(root, text="My name is Mike")
label3 = Label(root, text="I like python")

label.grid(row=0,column=0)
label2.grid(row=1,column=0)
label3.grid(row=0,column=1)

root.mainloop()