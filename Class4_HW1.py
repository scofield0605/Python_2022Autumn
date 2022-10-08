#引入tinker module
from tkinter import *
#建立主視窗 Frame
rooot=Tk()

#設定視窗標題
rooot.title('enter birthdate')
#設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為（500, 150）
rooot.geometry('300x100+500+150')
mylabel= Label(rooot, text='Enter birth date:\ninput format is yyyy.mm.dd',fg='silver', font=('Arial',18,'bold'))
mylabel.pack(pady=50)



#建立 input Entry Boxes
e=Entry(rooot, width=30, font=('Comic Sans  MS',16))
e.pack()
def clicked():
    label1=Label(rooot, text=e.get())
    label1.pack()

ebutton=Button(rooot,text='Enter',command=clicked)
ebutton.pack()
#執行主程式
rooot.mainloop()