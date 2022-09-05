#1
f = open("input.txt", "r")
for i in range(3):
    print(f.readline().strip())
f.close()
    
#2
f = open("input.txt", "r")
max_length = 0
for x in f:
    xlist = x.split()
    for i in xlist:
        if max_length <= len(i):
            max_length = len(i)
            max_word = i

print(max_length, max_word)
f.close()

#3
fname = input("파일 이름을 입력하시오.:")
lnumber = int(input("행번호를 입력하시오:"))

f = open(fname, "r")
lines = f.readlines()
cnt = 0
for line in lines:
    if cnt == lnumber:
        print(line)
        break
    cnt = cnt + 1
f.close()
    
#4
import os

print(os.getcwd())
os.mkdir("temp")
os.chdir("temp")

for i in range(26):
    f = open(chr(ord("A")+i)+".txt", "w")
    f.write("test\n")
    f.close()
    
print(os.listdir())

#5
f = open("test.txt", "r")
clist = f.read().strip().split()
f.close()

clist.insert(2, "line2-1")
f = open("test.txt", "w")
for x in clist:
    f.write(x+"\n")
f.close()

#6
import os
import random
print(os.getcwd())
f = open("numbergs.txt", "w")
for i in range(10): 
    f.write(str(random.randint(0, 100))+"\n")
f.close()

#7
while True:
    x = input("입력 파일 이름 :")
    try:
        f = open(x, "r")
        print("파일이 성공적으로 열렸습니다.")
        f.close()
        break
    except IOError:
        print("파일" + x + "이 없습니다. 다시 입력하세요")

#8
f = open("ss.txt", "r")
vlist = f.read().strip().split()
f.close()

s = 0
for x in vlist:
    s = s + float(x)
vlist.append(s)
print(vlist)

f = open("ss.txt", "w")
for x in vlist:
    f.write(str(x)+"\n")
f.close()

#9
fn = input("파일 이름을 입력하시오.:")
f = open(fn, "r")
f_list = f.readlines()
f.close()

del_str = input("삭제할 문자열을 입력하시오.:")
for i in range(len(f_list)):
    f_list[i] = f_list[i].replace(del_str, "")
       
print(f_list)

f = open(fn, "w")
for x in f_list:
    f.write(x)
f.close()

#10
fn = input("파일 이름을 입력하시오.:")
f = open(fn, "r")
space_cnt = 0
tab_cnt = 0

for line in f:
    space_cnt += line.count(" ")
    tab_cnt += line.count("\t")
    
print("스페이스 수 =", space_cnt, ", 탭의 수 =", tab_cnt)
f.close()

#11
fn = input("파일 이름을 입력하시오.:")
f = open(fn, "r")
f_list = f.readlines()
f.close()

cnt = 0
for i in range(len(f_list)):
    cnt += 1
    f_list[i] = str(cnt) + ":" + f_list[i]
    
f = open(fn, "w")
for x in f_list:
    f.write(x)
f.close()


    
    
    





