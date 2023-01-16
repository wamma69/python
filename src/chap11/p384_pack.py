# 압축 배치 관리자

# 1
from tkinter import *
root = Tk()

Button(root, text="박스 #1", bg="red", fg="white").pack()
Button(root, text="박스 #2", bg="green", fg="black").pack()
Button(root, text="박스 #3", bg="orange", fg="white").pack()

root.mainloop()


# 2
from tkinter import *
root = Tk()

Button(root, text="박스 #1", bg="red", fg="white").pack(side=LEFT)
Button(root, text="박스 #2", bg="green", fg="black").pack(side=LEFT)
Button(root, text="박스 #3", bg="orange", fg="white").pack(side=LEFT)

root.mainloop()

