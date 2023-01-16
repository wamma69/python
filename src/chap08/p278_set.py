# 요소 추가하고 삭제하기

# 1
fruits ={"apple","banana","grape"}
fruits.add("kiwi")
print(fruits)

# 2
fruits ={"apple","banana","grape", "kiwi"}
fruits.remove("kiwi")
print(fruits)

# 3
fruits ={"apple","banana","grape","kiwi"}
fruits.clear()		# 공백 세트가 된다. 
print(fruits)


# 세트 함축 연산
aList  =[1,2,3,4,5,1,2 ]
result ={ x for x in aList if x%2==0 }
print(result)