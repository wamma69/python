# 리스트 연산들

# append
fruits = [ ] 				# 공백 리스트를 생성한다. 
fruits.append("apple")			# 리스트에 ”apple“을 추가한다. 
fruits.append("banana")		# 리스트에 ”banana“를 추가한다. 
print(fruits)


# insert
fruits = ["apple", "banana", "grape"]
fruits.insert(1, "cherry")
print(fruits)


# 리스트 탐색하기. index()
fruits = ["apple", "banana", "grape"]
n = fruits.index("banana")		# n은 1이 된다. 
print(n)

if "banana" in fruits:    # 없다면 오류 발생. 먼저 있는지 확인한 후 탐색하자
    print(fruits.index("banana"))

    
# 요소 삭제하기    
fruits = ["apple", "banana", "grape"]
item = fruits.pop(0)		# "apple"이 삭제된다. 
print(fruits)

fruits = ["apple", "banana", "grape"]
fruits.remove("banana")
print(fruits)

if "banana" in fruits:    # 삭제할 대상이 없다면 오류 발생. 먼저 있는지 확인한 후 삭제하자
	fruits.remove("banana")
