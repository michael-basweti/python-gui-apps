from tkinter import *

root = Tk()

e=Entry(root,width=20)
e.pack()
e.insert(0,"Name...")

def myClick():
    label = Label(root, text=e.get())
    label.pack()

# you can make a button disabled by adding 'state=DISABLED' 
myButton = Button(root,text='Enter Your Name',padx=50, command=myClick, fg='#439cd3')
myButton.pack()

root.mainloop()