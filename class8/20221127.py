#更改button文字內容
from tkinter import *
from PIL import Image, ImageTk
root= Tk()
root.title('Class7')
root.geometry('200x200')

#方1
# counter=0
# def clicked():
#     global counter
#     counter +=1
#     mybutton['text']='click'+str(counter)

# mybutton=Button(root,text='Click', command=clicked)
# mybutton.pack()
#方法2
# mystringvar=StringVar()
# mystringvar.set('Click')

# counter=0
# def clicked():
#     global counter
#     counter += 1
#     mystringvar.set('click'+str(counter))

# mybutton=Button(root, textvariable=mystringvar, command=clicked)
# mybutton.pack()


#way1
# mybutton=Button(root,text='Hello World')
# mybutton.pack()
# Label(root, text=mybutton['text']).pack()

#way2
# mystringvar=StringVar()
# mystringvar.set('Hello World')
# mybutton=Button(root, textvariable=mystringvar)
# mybutton.pack()
# Label(root,text=mystringvar.get()).pack()

#開啟圖片
# img=Image.open('/Users/scofield/Documents/Python_2022Autumn/class8/corgi1.jpg')
#更改圖片大小
# resized_image=img.resize((100,100))
#轉換為TK圖片物件
# tk_img=ImageTk.PhotoImage(resized_image)

#在lable中放入圖片
# label=Label(root, image=tk_img)
# label.pack()
# mybutton=Button(root, image=tk_img)
# mybutton.pack()
#已入tkinter 的 messagebox
from tkinter import messagebox
#出現message test的普通訊息匡
# messagebox.showinfo('showinfo', 'message test')

#出現message test的普通訊息匡
# messagebox.askquestion('askquestion', 'is it sunday')

# def popup():
#     # result=messagebox.askyesno('askyesno', 'Do you want to contine?')
#     result=messagebox.askquestion('askyesno', 'Do you want to contine?')
#     print(result)
# popupbutton=Button(root,text='Click to pop Up!', command=popup)
# popupbutton.pack()
# #放no.1單選按鈕
# radiobtn1=Radiobutton(root, text='Black')
# radiobtn1.pack()
# #放no.2單選按鈕
# radiobtn2=Radiobutton(root, text='Red')
# radiobtn2.pack()
#宣告文字變數
val=StringVar()
宣告文字變數
radiobtn1=Radiobutton(root, text='Black',variable=val,value='Black')
radiobtn1.pack()
radiobtn1.select()
radiobtn2=Radiobutton(root, text='Red',variable=val,value='Red')
radiobtn2.pack()



root.mainloop()