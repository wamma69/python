# 슬라이싱
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]

print(numbers[:3])

print(numbers[3:])

print(numbers[:])


# 고급 슬라이싱
# 1 
numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print(numbers[2:7:2])
print(numbers[::-1])

# 2 부분 변경
lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[0:3] = ["white", "blue", "red"]
print(lst)

# 3
lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[::2] = [99, 99, 99, 99]
print(lst)

# 4 삭제 효과
lst = [1, 2, 3, 4, 5, 6, 7, 8]
lst[:] = []
print(lst)

# 5 del 삭제
numbers = list(range(0, 10))
print(numbers)

del numbers[-1]
print(numbers)

del numbers[0:2]
print(numbers)

del numbers[:]
print(numbers)