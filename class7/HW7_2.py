from tkinter import *
#建立主視窗 Frame
root = Tk()
#設定視窗標題
root.title( 'Class6')
root.geometry ('350x100')
#Frame 元件
framel = Frame(root, pady=5, padx=10, bg='lightgreen')
frame2 = Frame(root, pady=10, padx=2, bg='lightblue')
# 放到 frame1 裡的 label
label1 = Label(framel, text='First', width=5)
label1.pack()
# 放到 frame2 裡的 label
label2 = Label( frame2, text='Second' ,width=10)
label2.pack()
# 先放 frame2
frame2.pack(side='right')
# 再放 frame1
framel.pack(side='left')
#執行主程式
root.mainloop ()