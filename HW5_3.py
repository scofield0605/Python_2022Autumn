from tkinter import *

root=Tk()


root.geometry('300x100')

mylabel=Label(root,text='三人座沙發 綠色 / 灰色 / 黑色') 
mylabel2=Label(root,text='NT. 28,900') 
mybutton=Button(root,text='+')
mylabel3=Label(root,text='0') 
mybutton2=Button(root,text='-')
mylabel.pack()
mylabel2.pack(side='left')
mybutton.pack(side='right')
mylabel3.pack(side='right')
mybutton2.pack(side='right')



root.mainloop()