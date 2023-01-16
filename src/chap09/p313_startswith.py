# startswith()와 endswith() 메소드

# 1
print('Breakfast At Tiffany'.startswith('Breakfast'))

print('Breakfast At Tiffany'.endswith('Tiffany'))


# 2 파이썬 소스 파일 확인하기
s = input('파이썬 소스 파일 이름을 입력하시오: ')
if s.endswith('.py'):
	print('올바른 파일 이름입니다')
else :
	print('올바른 파일 이름이 아닙니다.')
