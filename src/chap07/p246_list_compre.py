# 리스트 함축

# 1
squares = [x * x for x in range(10)]
print(squares)

# 2
squares = []
for x in range(10):
    squares.append(x * x)
print(squares)

# 3 
squares = [x * x for x in range(10) if x % 2 == 0]
print(squares)