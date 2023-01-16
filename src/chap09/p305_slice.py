# 슬라이싱

# 1
s = 'Monty Python'

print(s[6:10])

t = s[:-1]    # 생략되면 문자열의 처음부터
print(t)

t = s[-2:]    # 생략되면 문자열의 끝까지
print(t)

print(s[:2])   
print(s[4:])   

print(s[:2] + s[2:])    # s와 같다.
print(s[:4] + s[4:])

print(s[:])    # 문자열 전체

# 2
message='see you at noon'    # 5번째 문자를 기준으로 둘로 나눈다.
low = message[:5]
high = message[5:]
print(low, high)

# 3
reg= '980326'   # 주민등록 앞자리에서 출생년도와 생일 추출
print(reg[0:2]+'년')
print(reg[2:4]+'월')
print(reg[4:6]+'일')

# 4
word = 'abcdef'
# word[0] = 'A'    # 문자열의 일부를 바꾸면 오류 발생

word = 'abcdef'   # 다음처럼 하면 문제없이 해결
word = 'A' + word[1:]
print(word)
