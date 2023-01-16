# 요소 접근

# 1
s = [[1, 2, 3, 4, 5] ,
	[6, 7, 8, 9, 10], 
	[11, 12, 13, 14, 15]]

# 행과 열의 개수를 구한다. 
rows = len(s)
cols = len(s[0])

for r in range(rows):
	for c in range(cols):
		print(s[r][c], end=",")
	print()


# 2. 리스트 안에 다른 리스트를 내장하는 것도 가능하다
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

print(x)