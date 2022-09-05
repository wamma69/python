#1
# cnt = 0
# for i in range(1,101):
#     if i % 3 == 0:
#         cnt+=1
# print(cnt)
print(sum([1 for i in range(1,101) if i % 3 == 0]))

#2
print(eval(input("정수나 실수를 입력하시오:")))

#3
s = [('국어', 88), ('수학', 90), ('영어', 99), ('자연', 82)]
print('원래의 리스트:\n', s)
s.sort(key=lambda x:x[1])
print('정렬된 리스트:\n', s)

#4
s = [i for i in range (1,11)]
print("원래의 리스트:\n", s)
even = list(filter(lambda x:x%2==0, s))
print("짝수:\n", even)
odd = list(filter(lambda x:x%2!=0, s))
print("홀수:\n", odd)

#5
x = [i for i in range (1,11)]
print("원래의 리스트:\n", x)
y = list(map(lambda i:i**3, x))
print("세제곱된 값:\n", y)

#6
#factorial.py
def fact(n):
    r = 1
    for i in range(1, n+1):
        r = r * i
    return r

import factorial
print(factorial.fact(3))

#9
x = [i for i in range(1,11)]
print(list(map(lambda i : i**2, x)))

#10
x = [i for i in range(1,11)]
print(list(map(lambda j:j**2, filter(lambda i:i%2==0, x))))

#13
#13-1  리스트를 먼저 만들어 놓고 사용
import random
r = ""
x = [chr(i+97) for i in range(26)]
for i in range(10):
    r = random.choice(x) + " " + r
print(r)

#13-2  리스트 없이 chr, ord 사용
import random
r = ""
for i in range(10):
    r = chr(ord('a') + random.randint(0, 26)) + " " + r
print(r)

#14
import random
print(random.sample([i for i in range(100, 201)], 5))


