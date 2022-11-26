from tkinter import *

root = Tk()
root.title('oxxo.studio')
root.geometry('200x200')

n = 0               
a = StringVar()  
a.set(n)           

def add():
    global n        
    n = n + 1      
    a.set(n)        

mylabel = Label(root, textvariable=a, font=('Arial',20))  # 放入標籤
mylabel.pack()

# Button 設定 command 參數
btn = Button(root,text='betton',font=('Arial',30,'bold'),command=add)
btn.pack()

root.mainloop()