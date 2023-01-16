# 대소문자 변환하기

# 1
s = 'Breakfast At Tiffany'
print(s.upper())
print(s.lower())


# 2
print('게임을 계속하시겠어요?')
response = input()
if response.lower() == 'yes':
	print('게임을 계속합니다.')
else:
	print('다음에 또 뵈요.')
