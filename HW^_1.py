from tkinter import *

root = Tk()
root.geometry('200x200')

n = 0               
a = StringVar()  
a.set(n)           

def add():
    global n        
    n = n + 1      
    a.set(n)        

mylabel = Label(root, textvariable=a)
mylabel.pack()


btn = Button(root,text='button',command=add)
btn.pack()

root.mainloop()