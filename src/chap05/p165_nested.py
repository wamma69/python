# 1. 사각형 패턴 출력하기
for y in range(5) :
	for x in range(10) :
		print("*", end="" )			# 내부 반복문이 종료될 때마다 실행
	print("")


# 2. 삼각형 패턴 출력하기
for y in range(1, 6) :
	for x in range(y) :
		print("*", end="" )
	print("")			# 내부 반복문이 종료될 때마다 실행