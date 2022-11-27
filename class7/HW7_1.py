from tkinter import *

root = Tk()
root.geometry()

number=0


def add():
    numlabel['text']=int(numlabel['text'])+1
    amountLabel['text']="總額: $"+str(int(numlabel['text'])*120)

def minus():
    if int(numlabel['text'])>0:
        numlabel['text']




titlelabel=Label(root, text='Kube shop')
productnamelabel=Label(root, text='$ 1200')
pricelabel=Label(root, text='0')
