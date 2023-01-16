# 1. 신호등이 색상이 녹색이 될 때까지 대기하는 프로그램
while True:
    light = input('신호등 색상을 입력하시오 ')
    if light == 'green':
        break
print( '전진!!')


# 2. 1부터 10에서 3의 배수만 빼고 출력하기
for i in range(1, 11):
    if i%3 == 0 :		# 3의 배수이면
        continue		# 다음 반복을 시작한다. 
    print(i, end=" ")	# 줄바꿈을 하지 않고 스페이스만 출력한다. 
