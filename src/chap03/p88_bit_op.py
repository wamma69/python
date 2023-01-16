# 비트 연산자

# 1
a = 0b00001101
b = 0b00001010
print( a&b, a|b, a^b )
print( bin(a&b), bin(a|b), bin(a^b) )

# 2
a = 0b00001101
print(~a, bin(~a))   # 산술적 not

# 3
a = 0b00001101
print(~a&255, bin(~a&255))    # 논리적 not 는 bit AND 연산을 추가해야 한다.
