# 2의 배수이면서 3의 배수인 수 찾기
numbers = [x for x in range(100) if x % 2 == 0 and x % 3 == 0]
print(numbers)
print()


# 합계 리스트 생성
list1=[10, 20, 30, 40, 50]
list2=[sum(list1[0:x+1]) for x in range(0, len(list1))]

print("원래 리스트: ",list1)
print("새로운 리스트: ",list2)
print()


# 직각 삼각형 찾기
print([(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30) if x**2 + y**2 == z**2])

