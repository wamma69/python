from tkinter import *
window = Tk()
window.geometry("600x200")

def execute():
    texts = entry.get()
    label2["text"] = entry.get()
    starts = startEntry.get()
    ends = endEntry.get()
    if starts > ends:
        label6["text"] = "범위를 잘못 입력하였습니다."
    else:
        label6["text"] = texts[int(starts)-1:int(ends)]
 
label1 = Label(window, text="글 : ")
label1.grid(row=0,column=0)

label2 = Label(window, text="매화는 매서운 추위에도 향기를 팔지 않는다")  
label2.grid(row=0,column=1)

label3 = Label(window, text="추출할 문장 : ")
label3.grid(row=1,column=0)

entry = Entry(window)
entry.grid(row=1, column=1)

label4 = Label(window, text="시작범위 : ")
label4.grid(row=2, column=0)

startEntry = Entry(window)
startEntry.grid(row=2, column=1)

label5 = Label(window, text="끝범위 : ")
label5.grid(row=2, column=2)

endEntry = Entry(window)
endEntry.grid(row=2,column=3)

button = Button(window, text = "추출하기", command=execute)
button.grid(row=3,column=1 )

label6 = Label(window, text="")
label6.grid(row=4, columnspan=3)

window.mainloop()
