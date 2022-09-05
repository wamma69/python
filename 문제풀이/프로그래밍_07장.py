#1
x = [80, 20, 20, 30, 60, 30]
print("주어진 리스트 :", x)
print("정리된 리스트 :", sorted(list(set(x))))

#2
x = dict()
for i in range(1,11):
    x[i] = i*i
print(x)
#or
print({x:x*x for x in range(1,11)})

#3
d = {"Apple":1, "Banana":2, "Grape":3}
for k, v in d.items():
    print(k, "->", v)
#or
d = {"Apple":1, "Banana":2, "Grape":3}
for k in d:
    print(k, "->", d[k])
    
#4
d = {x:x*10 for x in range(1, 7)}
print(d)
k = int(input("키를 입력하시오: "))
if k in d :
    print("키", k, "는 딕셔너리에 있습니다.")
    
#5
myDict = {"옷":100, "컴퓨터":2000, "모니터":320}
s = 0
for k, v in myDict.items():
    s = s + v
print("총합계=", s)

#6
colors = {"red", "green", "blue"}
values = {"#FF0000", "#008000", "#0000FF"}
print(dict(zip(colors, values)))

#7
diary = {}
while True:
    v_list = []
    k = input("날짜를 입력하시오:")
    if k in diary:
        v_list = diary[k]
       
    v = input("일정을 입력하시오:")
    v_list.append(v)
    diary[k] = v_list
    print(diary)
    
    ans = input("계속하시겠습니까?(y/n)")
    if ans == "n" or ans == "N" :
        break

#8
cal = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
k = int(input("달의 번호: "))
if k in cal:
    print("달의 문자:", cal[k])
else:
    print("Error")

#9
s1 = input("첫번째 문자열: ")
s2 = input("두번째 문자열: ")
print("모두 포함된 글자:",set(s1) & set(s2))

#10
s1 = {10, 20, 30, 40, 50, 60}
s2 = {30, 40, 50, 60, 70, 80}
print("어느 한쪽에만 있는 요소들 ", ((s1-s2) | (s2-s1)))

#12
a = input("문자열을 입력하시오: ")
b = list(input("금칙어를 입력하시오: ").split())
for i in b:
    a = a.replace(i, "***")
print(a)

#13
s = "Hello World123"
dict = {}
letter_cnt = 0
digit_cnt = 0
for i in s:
    if i.isalpha():
        letter_cnt += 1
    if i.isnumeric():
        digit_cnt += 1
dict["LETTERS"] = letter_cnt
dict["DIGITS"] = digit_cnt
print(dict)
#or
s = "Hello World123"
dict = {}
dict["LETTERS"] = sum(1 for i in s if i.isalpha())
dict["DIGITS"] = sum(1 for i in s if i.isnumeric())
print(dict)

#14
x = "05/21/2020"
d,m,y = x.split("/")
print("".join((y,m,d)))

#15
studentList = {
    "Park": "Korea",
    "Sam": "USA",
    "Sakura": "Japan"}
for k, v in studentList.items() :
    print(f'"Hi I\"{k}, and I\"m from {v}"')
    
#16
import random
s = "abcdefghijklimopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*"
print("생성된 암호=", "".join(random.sample(s, 8)))