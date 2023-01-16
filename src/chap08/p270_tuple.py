# 튜플
fruits = ("apple", "banana", "grape")

single_tuple = ("apple",) 	# 쉼표가 끝에 있어야 한다.
print(single_tuple)

no_tuple = ("apple")		# 쉼표가 없으면 튜플이 아니라 수식이 된다.
print(no_tuple)

# fruits[1] = "pear"   		# 오류 발생

for f in fruits:
	print(f, end=" ")  		# apple banana grape 출력
 