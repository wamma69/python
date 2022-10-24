from tkinter import*
w = Tk()

def re():
    ki = float(e1.get())
    che = int(e2.get())
    bmi = round(che/(ki*ki),2)
    res = " "
    if (bmi < 20):
        res = "저체중 입니다."
    elif (bmi > 20)  and (bmi < 24.9):
        res = "정상 입니다."
    elif (bmi > 25) and (bmi < 29.9):
        res = "과체중 입니다."
    else:
        res = "비만 입니다."
    
    bmi1["text"] = bmi
    res1["text"] = res
        
Label(w, text="키").grid(row=0, column=0)
Label(w, text="체중").grid(row=1, column=0)
Label(w, text="m").grid(row=0, column=2)
Label(w, text="kg").grid(row=1, column=2)


e1 = Entry(w)
e1.grid(row=0, column=1)

e2 = Entry(w)
e2.grid(row=1, column=1)

b1 = Button(text="판정하기",command=re)
b1.grid(row=2, column=1)

Label(text="BMI").grid(row=3, column=0)

bmi1 = Label(text=" ")
bmi1.grid(row=3, column=1)
Label(text="판정결과").grid(row=4, column=0)
res1 = Label(text=" ")
res1.grid(row=4, column=1)
w.mainloop()
