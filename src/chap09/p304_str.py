# 1. 문자열

s1 = 'Hello'   # 단일 인용부호(single quotation)
s2 = "Hello"   # 이중 인용부호(double quotation)

s3 = "This is Kim's dog."		# 문자열 안에 인용 기호가 있는 경우
print(s3)

s = 'This is Kim\'s dog.'		# 같은 인용부호를 쓰면 이스케이프 문자로 구분
print(s)


# 2. 원시 문자열
print(r'This is Kim\'s dog')   # r을 두면 원시 문자열(raw string)으로 인식


# 3. 인덱싱
s = 'Monty Python'
print(s[0])
print(s[-1])


