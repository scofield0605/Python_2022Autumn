from tkinter import *

root=Tk()

root.geometry('500x500')

mybutton1=Button(root,text='West')
mybutton2=Button(root,text='East')
mybutton3=Button(root,text='East2')


# #side排列方向排列方向：TOP(預設),BOTTOM,LEFT,RIGHT
# mybutton1.pack(side='left')
# mybutton2.pack(side='right')
# mybutton3.pack(side='right')

# fill填滿所分配空間之方向：：none (預設),x,y, BOTH
mybutton1.pack(fill='x')
mybutton2.pack(side='right',fill='y')
# expend填滿容器容器：true/false(預設)
mybutton1=Button(root,text='fillx')
mybutton1.pack(fill='x')

# mybutton1=Button(root,width=10)
# mybutton1.pack(fill='both', expand=0)
# mybutton2=Button(root,width=10)
# mybutton2.pack(fill='both', expand=1)

#padx/pady元件邊匡與容器之距離(px,預設=0)

# mybutton1.pack(side='left', padx=30)
# mybutton2.pack(side='right',pady=30)

# #ipadx/ipady元件內容(文字/圖像）與其編筐之距離 (px,預設＝0)
# mybutton1.pack(side='left')
# mybutton1.pack(side='right')
# mybutton1.pack(side='left', ipadx=30)
# mybutton2.pack(side='right',ipady=30)


# mybutton1=Button(root,text='1')
# mybutton2=Button(root,text='2')
# mybutton4=Button(root,text='3')
# mybutton1.pack()
# mybutton2.pack(side='left')
# mybutton4.pack(side='bottom')

root.mainloop()