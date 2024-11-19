import os
from tkinter import * 
root = Tk()
root.geometry("700x400")

def restart() :
    root.destroy()
    os.system('C:/Users/USER/Desktop/tk.py')

def human() :
    if h.get() == 1 :
        c4.pack_forget()
        c5.pack_forget()
    elif h.get() == 2 :
        c4.pack(side=LEFT)
        c5.pack(side=LEFT)


def kkk() :
    s = ""
    if x.get() == 1 :
        s = s + "아메리카노 "
    if y.get() == 1 :
        s = s + "라떼 "
    if z.get() == 1 :
        s = s + "물 "
    if a1.get() == 1 :
        s = s + "맥주 "
    if a2.get() == 1 :
        s = s + "소주 "

    l2["text"] = s


l1 = Label(root, text="카페 메뉴")
l1.pack()

f1 = Frame(root)

h = IntVar()
r1 = Radiobutton(f1, variable=h, value=1, text="미성년자", command=human)
r1.pack(side=LEFT)
r2 = Radiobutton(f1, variable=h, value=2, text="성인", command=human)
r2.pack(side=LEFT)

f1.pack()


f2 = Frame(root)

x = IntVar()    # 정수 IntVar(), 실수 DoubleVar(), 문자열 StringVar(), 부울 BooleanVar()
y = IntVar()
z = IntVar()
a1 = IntVar()
a2 = IntVar()

c1 = Checkbutton(f2, variable=x, text="아메리카노(1000원)", command=kkk)
c1.pack(side=LEFT)
c2 = Checkbutton(f2, variable=y, text="라떼(2000원)", command=kkk )
c2.pack(side=LEFT)
c3 = Checkbutton(f2, variable=z, text="물(500원)" , command=kkk)
c3.pack(side=LEFT)

c4 = Checkbutton(f2, variable=a1, text="맥주(3000원)", command=kkk )
c4.pack(side=LEFT)
c5 = Checkbutton(f2, variable=a2, text="소주(3500원)" , command=kkk)
c5.pack(side=LEFT)

f2.pack()

l2 = Label(root, text="주문을 하세요")
l2.pack()

b = Button(root, text="다시하기", command=restart)
b.pack()


root.mainloop()
