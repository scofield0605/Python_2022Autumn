#引入tinker module
from tkinter import *
#建立主視窗 Frame
rooot=Tk()

#設定視窗標題
rooot.title('點擊按鈕次數計算')
#設定視窗大小為 300x100，視窗（左上角）在螢幕上的座標位置為（500, 150）
rooot.geometry('300x100+500+150')
mylabel= Label(rooot, text='點擊按鈕次數計算',fg='yellow', font=('courior',18,'bold'))
mylabel.pack(pady=50)
n=0
def clicked():
    global n
    n=n+1
    label1=Label(rooot, text=n)
    label1.pack()

ebutton=Button(rooot,text='Enter',command=clicked)
ebutton.pack()
#執行主程式
rooot.mainloop()