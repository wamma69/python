# enumerate() 사용하기

fruits = ["apple","banana","grape"]
for index, value in enumerate(fruits):
	print(index, value)
 
 
fruits = ["apple","banana","grape"]
result = list(enumerate(fruits))   # enumerate() 결과를 리스트에 담기
print(result)