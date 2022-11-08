f = open("f.txt","w", encoding="utf-8")

for i in range(5):
    a = input("요일 : ")
    b = input("최고기온 : ")
    f.write(f"{a} ")
    f.write(f"{b}\n")

f.close()

rf = open("f.txt","r", encoding="utf-8")
x = rf.readline()
day = []
temp = []
while x != "":
    rl = x.split()
    day.append(rl[0])
    temp.append(int(rl[1]))
    x = rf.readline()

maxday = temp.index(max(temp))
print(day[maxday], temp[maxday])

rf.close()
