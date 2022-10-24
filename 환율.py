from tkinter import *

def convert1(x):
    y = str(round(x/1432.20,2))
    f2.delete(0,END)
    f2.insert(END,y)

def convert2(x):
    y = str(round(x*1432.20,2))
    f1.delete(0,END)
    f1.insert(END,y)
    
def reset(a):
    f1.delete(0,END)
    f2.delete(0,END)
    print(a)

i = "리셋합니다..."
win = Tk()

Label(win,text="한국 원화").grid(row=0,column=0)
f1 = Entry(win)
f1.grid(row=0,column=1)
Label(win,text="=").grid(row=0,column=2)
Label(win,text="미국 달러").grid(row=0,column=3)
f2 = Entry(win)
f2.grid(row=0,column=4)

b1 = Button(win, text="원화 => 달러", command=lambda:convert1(float(f1.get())))
b1.grid(row=1,column=2)
b2 = Button(win, text="달러 => 원화", command=lambda:convert2(float(f2.get())))
b2.grid(row=2,column=2)
b3 = Button(win, text="초기화", command=lambda:reset(i))
b3.grid(row=3,column=2)

win.mainloop()
