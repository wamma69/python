# 리스트 복사하기

# 1. 얕은 복사
temps = [28, 31, 33, 35, 27, 26, 25] 
values = temps

print(temps)
values[3] = 39			# values 리스트 변경
print(values)
print(temps)			# temps 리스트가 변경되었다. 
print()


# 2. 깊은 복사
temps = [28, 31, 33, 35, 27, 26, 25] 
values = list(temps)

values[3] = 39			# values 리스트 변경
print(values)
print(temps)			# temps 리스트가 변경되지 않는다. 
