# 2차원 리스트

# 1. 2차원 리스트를 생성한다.(정적)
s = [ 
	[ 1, 2, 3, 4, 5 ] ,
	[ 6, 7, 8, 9, 10 ], 
	[11, 12, 13, 14, 15 ] 
]
print("s =", s)
print()


# 2. 동적으로 2차원 리스트를 생성한다.
rows = 3
cols = 5

s = [ ]
for row in range(rows): 
	s += [[0]*cols]		# 2차원 리스트끼리 합쳐진다. 
	# s += [0]*cols		# 1차원 리스트끼리 합쳐진다.(주의)

print("s =", s)


# 3. (추가) 리스트 함축을 이용하여 동적으로 2차원 리스트를 생성한다.
rows = 3
cols = 5

s = [ ([0] * cols) for row in range(rows) ]

print("s =", s)


