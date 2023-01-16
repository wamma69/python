# 리스트 방문

# 1. 인덱스 값을 사용하여 방문
temps =[28,31,33,35,27,26,25] 

for i in range(len(temps)):
	print(temps[i], end=', ')
print()

# 2. for-in 루프 사용하여 방문
temps =[28,31,33,35,27,26,25] 

for element in temps:
	print(element, end=', ')
