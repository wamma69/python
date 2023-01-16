# 튜플 패킹과 언패킹

# 1
x = ("apple", "banana", "grape")   # 튜플 패킹
(s1, s2, s3) = x   # 튜플 언패킹


# 2 서로 다른 자료형에 대해서도 패킹과 언패킹이 가능
student = ("Kim" , [3.1, 3.6, 4.0, 0.0])   
name, grades = student
print(name)
print(grades)


# 3 데이터 순서 바꾸기에 이용
n1 = 10
n2 = 90
n1, n2 = (n2, n1)
print(n1, n2)