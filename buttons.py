from tkinter import *

root = Tk()

def myClick():
    label = Label(root, text="You clicked me")
    label.pack()

# you can make a button disabled by adding 'state=DISABLED' 
myButton = Button(root,text='Click Me',padx=50, command=myClick, fg='#439cd3')
myButton.pack()

root.mainloop()