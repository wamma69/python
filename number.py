f = open("number.txt","w")
for i in range(1,101):
    if (i % 3 == 0):
        f.write(str(i) + "\n")
        
f.close()

f = open("number.txt","r")

cnt = 0

for i in f:
    if (int(i) % 5 == 0):
        print(i)
        cnt = cnt + 1
print(f"총 개수는 {cnt}개 입니다.")

f.close()
