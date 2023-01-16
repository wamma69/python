# 세트의 연산

# 1
fruits ={"apple","banana","grape"}
size =len(fruits)			# size는 3이 된다. 


# 2
fruits = { "apple", "banana", "grape" }
if "apple" in fruits:
	print("집합 안에 apple이 있습니다.")


# 3
fruits ={"apple","banana","grape"}
for x in fruits:
	print(x, end=" ")   # 입력 순서와 출력 순서가 다를 수 있다.
print()


# 4
fruits ={"apple","banana","grape"}
for x in sorted(fruits):    # 정렬된 순서로 출력
	print(x, end=" ")   
 

