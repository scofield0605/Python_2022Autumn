from tkinter import *

root=Tk()

root.geometry('500x500')

mybutton1=Button(root,text='1')
mybutton2=Button(root,text='2')
mybutton4=Button(root,text='3')
mybutton1.pack()
mybutton2.pack(side='left')
mybutton4.pack(side='bottom')

root.mainloop()