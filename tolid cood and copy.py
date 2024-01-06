from tkinter import *
import random
import pyperclip
alp=['A','B','C',"D",'E',"F",'G','H','I','J','K','L',"M",'N'
'p','o','Q','R','S','T','U','V','W',
'X','Y','Z','1','2','3','4','5','6','7','8','9','0']

color=['gold','blue','red','navy','green']

root=Tk()
root.title('cood')
root.geometry('400x600')
root.resizable(0,0)
root.configure(bg=random.choice(color))
def cood():
    pa=''
    r=int(y.get())
    for i in range(r):
        pa += random.choice(alp)
        J.config(text=pa)

B=Button(root,text="Click",fg='black',bg='violet',font=('Arial',25),command=cood)
B.place(x=145,y=300)

def text():
    text=J.cget("text")
    pyperclip.copy(text)
C=Button(root,text='clipboard',font=('Arial',15),command=text,bg='silver')
C.place(x=145,y=240)
J=Label(root,text='cood :',font=("Arial",20),bg='silver')
J.place(x=15,y=150)
y=Entry(root,font=('Arial',15))
y.place(x=85,y=200)
root.mainloop()
