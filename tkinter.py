from tkinter import *

root = Tk()


def Hello(event):
    print ("Yet another hello world")



btn = Button (root, text = 'click me',
              width=10, height=2,
              bg='red', fg='navy')

btn.bind("<Button-1>", Hello)

lab = Label(root, text='Your name')

Edit = Entry (root, width=20)


btn.pack()
lab.pack()
Edit.pack()
root.mainloop
