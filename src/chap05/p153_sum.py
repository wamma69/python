# 1
for i in range(1, 6, 1):
    print(i, end=" ")
    
for i in range(10, 0, -1):
    print(i, end=" ")


# 2. 1부터 n까지의 합 계산 프로그램
sum = 0
n = 10
for i in range(1, n+1) :				
	sum = sum + i
print("합=", sum)


# 3. 구구단 출력 프로그램
for i in range(1, 6):
    print("9 *", i, "=", 9*i)