# 1. 문자열 검사 메소드

print('HELLO'.isupper())   	#대문자 검사

print('hello'.islower())	#소문자 검사

print('abc'.isalpha())		#영문자 검사

print('abc123'.isalpha())	

print('abc123'.isalnum())	#영문자와 숫자 검사

print('123'.isdecimal())	#숫자 검사

print(' \n'.isspace())		#공백, 탭, 줄바꿈 문자 검사
      

# 2. 입력의 유효성 검사하기
while True:
	print('새로운 패스워드를 선택하시오 (문자와 숫자만 가능)')
	password = input()
	if password.isalnum():
		break
	print('문자와 숫자만을 이용하여 패스워드를 선택하시오.')
