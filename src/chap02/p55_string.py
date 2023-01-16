# 문자열 <-> 수치값
"Student"+str(26)

price = int("123")
height = float("3.14")

# 문자열의 반복
line = "=" * 50
print(line)

message = "Congratulations! "
print(message*3)

# 문자열 메서드
message = "Merry Christmas!"
print(len(message))         # 문자열의 길이를 반환한다.
print(message.upper())      # 문자열을 대문자로 만들어서 반환한다.
print(message.find("Ch"))   # 문자열 안에서 "Ch"를 찾는다.

# 문자열 안의 문자에 접근하기
s = "Python"
print(s[0])
print(s[1])
print(s[-1])

# 문자열 안의 변수 출력
price = 10000
print(f"상품의 가격은 {price}원 입니다.")

product = "coffee"
count = 3
price = 10000
print(f"상품 {product} {count}개의 가격은 {count*price}원입니다.")

pi = 3.141592
print(f"원주율={pi:.2f}")   # 소수점 두번째 자리까지 출력


# + 또는 ,로 연결해서 출력하는 방법도 있다.
