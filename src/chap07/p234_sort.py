#정렬

# 1. sort()
a = [ 3, 2, 1, 5, 4 ]
a.sort()			# 원본이 변경된다.
print(a)

a = [ 3, 2, 1, 5, 4 ]
a.sort(reverse=True)
print(a)


# 2. sorted()
numbers = [10,3,7,1,9,4,2,8,5,6]
ascending_numbers = sorted(numbers)   # 원본은 바뀌지 않는다.
print(ascending_numbers)
print(numbers)
