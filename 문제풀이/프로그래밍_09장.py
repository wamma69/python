#1
from tkinter import *				
window = Tk()					

def goo():
    l['text'] = "clicked"
    
l = Label(window, text="Hi!")
l.pack(side=LEFT)

#이벤트 처리 대상은 pack()을 따로 코딩해야 한다. 아래처러 한줄로 하면 error발생한다.
#l = Label(window, text="Hi!").pack(side=LEFT)

b = Button(window, text="click me", command=goo).pack(side=LEFT)					

window.mainloop()	

#2
from tkinter import *
window = Tk()

Label(window, text="Hello, I'm Label", bg="orange", fg="blue", width="50", height="3").pack()
window.mainloop()

#3
from tkinter import *
window = Tk()

for i in range(3):
    for j in range(10):
        Button(window, text=str(i)+"행,"+str(j)+"열").grid(row=i, column=j)
window.mainloop()

#4
from tkinter import *
window  = Tk()

# 레이블 생성, 내부의 글자 정렬은 anchor
Label(window, text="이름:", anchor=E, width=8).grid(row=0, column=0)
Label(window, text="주소:", anchor=E, width=8).grid(row=1, column=0)
Label(window, text="도:", anchor=E, width=8).grid(row=2, column=0)
Label(window, text="우편번호:", anchor=E, width=8).grid(row=3, column=0)
Label(window, text="국가:", anchor=E, width=8).grid(row=4, column=0)

# 엔트리 생성
e1 = Entry(window, width=30).grid(row=0, column=1)
e2 = Entry(window, width=30).grid(row=1, column=1)
e3 = Entry(window, width=30).grid(row=2, column=1)
e4 = Entry(window, width=30).grid(row=3, column=1)
e5 = Entry(window, width=30).grid(row=4, column=1)

# 프레임 생성, 전체영역 쓰기는 sticky, 간격띄우기는 padx
f = Frame(window)
Button(f, text='submit').pack(side=RIGHT, padx=5)
Button(f, text='clear').pack(side=RIGHT, padx=5)
f.grid(row=5, column=0, columnspan=5, sticky=E+W, padx=5)

window.mainloop( )

#5
from tkinter import *
window  = Tk()

def down():
    x['text'] = int(x['text']) - 1

def up():
    x['text'] = int(x['text']) + 1


Button(text='감소', command=down).pack(side=LEFT)
x = Label(window, text=0, width=8)
x.pack(side=LEFT)
Button(text='증가', command=up).pack(side=LEFT)

window.mainloop( )

#6
from tkinter import *
window  = Tk()
import random

def rnd():
    x['text'] = random.randint(1, 6)

x = Label(window, text=0, width=8)
x.pack(side=LEFT)
b1 = Button(text='굴리기', command=rnd).pack(side=LEFT)

window.mainloop( )

#7
from tkinter import *
window  = Tk()

def conv():
    la['text'] = float(e1.get()) * 2.54

Label(window, text="인치를 입력하시오:").grid(row=0, column=0)
e1 = Entry(window, text="", width=10)
e1.grid(row=0, column=1)
Label(window, text="변환결과").grid(row=1, column=0)
la = Label(window, text="")
la.grid(row=1, column=1)
Button(text='변환', command=conv).grid(row=2, column=0, columnspan=2)

window.mainloop( )

#8
from tkinter import *
window  = Tk()

def login():
    if e1.get()=="" :
        e1.insert(0, "아이디를 입력하세요")
    else :
        if e2.get()=="":
            e2.insert(0, "비밀번호를 입력하세요")
        else:
            pass
                      
def cancel():
    e1.delete(0, END)
    e2.delete(0, END)

Label(window, text="아이디").grid(row=0, column=0)
Label(window, text="패스워드").grid(row=1, column=0)

e1 = Entry(window, text="", width=10)
e1.grid(row=0, column=1)
e2 = Entry(window, text="", width=10)
e2.grid(row=1, column=1)

f = Frame(window)
Button(f, text='로그인', command=login).pack(side=LEFT)
Button(f, text='취소', command=cancel).pack(side=LEFT)
f.grid(row=2, column=0, columnspan=2, sticky=E+W, padx=5)

window.mainloop( )

#10
from tkinter import *
window  = Tk()

size = 50
Cwidth = 500
Cheight = 500

def sizeUp(event):
    global size
    size += 50
    if size <= Cwidth : 
        canvas.delete('all')
        canvas.create_rectangle(10,10,size,size)
    else :
        canvas.create_text(150,150, text="최대크기입니다.", fill='red', font=20)

def sizeDown(event):
    global size
    size -= 50
    if size <= 50 : 
        canvas.create_text(150,150, text="최소크기입니다.", fill='red', font=20)
    else:
        canvas.delete('all')
        canvas.create_rectangle(10,10,size,size)
    
canvas = Canvas(window, width=Cwidth, height=Cheight)
canvas.pack()

window.bind("<Button-1>", sizeUp)
window.bind("<Button-3>", sizeDown)

window.mainloop( )

#11
from tkinter import *
window  = Tk()
import time

canvas = Canvas(window, width=500, height=100)
canvas.pack()

dx = 5
msg = canvas.create_text(150,50, text="최대크기입니다.", fill='red', font=20)

while True:
    x0, y0 = canvas.coords(msg)
    print(x0, y0)
    if x0 <= 0 or x0 >= 500:
        dx = -dx
    canvas.move(msg, dx, 0)
    window.update()
    time.sleep(0.05)

window.mainloop( )

#12
from tkinter import *
window  = Tk()
import time

canvas = Canvas(window, width=500, height=500)
canvas.pack()
dx = 10
dy = 10

def left():
    canvas.move(target, -dx, 0)    
    
def right():
    canvas.move(target, dx, 0)

def up():
    canvas.move(target, 0, -dy)    
    
def down():
    canvas.move(target, 0, dy)
    
target = canvas.create_rectangle(220,220,260,260)

f = Frame(window)
Button(f, text='<-(left)', command=left).pack(side=LEFT)
Button(f, text='->(right)', command=right).pack(side=LEFT)
Button(f, text='^(up)', command=up).pack(side=LEFT)
Button(f, text='v(down)', command=down).pack(side=LEFT)
f.pack()

window.update()
window.mainloop( )
#추가퀴즈: 경계선 인식후 백워드 처리해보기.

#13
from tkinter import *
window  = Tk()

canvas = Canvas(window, width=500, height=500)
canvas.pack()
dx = 10
dy = 10

def left(event):
    canvas.move(target, -dx, 0)    
    
def right(event):
    canvas.move(target, dx, 0)

def up(event):
    canvas.move(target, 0, -dy)    
    
def down(event):
    canvas.move(target, 0, dy)
    
target = canvas.create_rectangle(220,220,260,260)

window.bind("<Left>", left)
window.bind("<Right>", right)
window.bind("<Up>", up)
window.bind("<Down>", down)

window.mainloop( )
#추가퀴즈: 경계선 인식후 백워드 처리해보기.

