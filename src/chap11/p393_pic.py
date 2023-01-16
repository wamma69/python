# 화면에 그림 그리기

from tkinter import *

root = Tk()
w = Canvas(root,  width=300, height=200)
w.pack()

w.create_rectangle(50, 25, 200, 100, fill="blue")
root.mainloop()