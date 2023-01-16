# 리스트 함축의 단점

# 1
print(sum([i * i for i in range(1000)]))


# 2 
import time
start = time.time()
print("1번 방법=", sum([i * i for i in range(10000000)]))
end = time.time()
print("소요시간=", end-start)

start = time.time()
sum = 0         # 같은 문제지만 이 방식이 훨씬 빠르다.
for i in range(10000000):
    sum += i*i
print("2번 방법=", sum)
end = time.time()
print("소요시간=", end-start)