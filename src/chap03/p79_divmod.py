# 몫과 나머지
x = int(input('피젯수: '))
y = int(input('젯수: '))

q = x // y
r = x % y
print(f"{x}을 {y}로 나눈 몫={q}" )
print(f"{x}을 {y}로 나눈 나머지={r}" )

# divmod() 함수를 이용해서 몫과 나머지를 구할수도 있다.
x = 10
y = 3
quotient,remainder = divmod(x, y)	
print(quotient, remainder)

# 나머지 연산자는 짝수/홀수 판별이나 요일 계산 등에 이용한다.
today = 0
print( (today + 10) % 7 )

