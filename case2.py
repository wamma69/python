#.Quiz 추출할 문장을 가지고 시작범위와 끝 범위를 입력해 추출하는 것 start>end일시 error 출력
from tkinter import *

w = Tk()

def ttt():
    a = str(L2["text"])
    b = int(E2.get())
    c = int(E3.get())
    d = str(E4)
    
    if b <= c:
        e = str(a[b:c])
        E4.insert(0,e)
    else:
        E4.delete(0,END)
        E4.insert(0,"error")
        
L1=Label(w,text="글:")
L1.grid(row=0,column=0)

L2=Label(w,text="매화는 매서운 추위에도 향기를 팔지 않는다.")
L2.grid(row=0,column=1)

L3=Label(w,text="추출할 문장")
L3.grid(row=1,column=0)

L4=Label(w,text="시작범위:")
L4.grid(row=2,column=0)

L5=Label(w,text="끝범위:")
L5.grid(row=2,column=2)

E2=Entry(w)
E2.grid(row=2,column=1)

E3=Entry(w)
E3.grid(row=2,column=3)

E4=Entry(w)
E4.grid(row=3,column=1)

B1=Button(w,text="추출하기",command=ttt)
B1.grid(row=3,column=0)



w.mainloop()
