# 튜플 <-> 리스트
myList = [1,2,3,4]
myTuple = tuple(myList)   #tuple()는 튜플을 생성하는 함수이다.
print(myTuple)

myTuple = (1, 2, 3, 4)
myList = list(myTuple)
print(myList)


# 튜플 연산들
fruits = ("apple", "banana", "grape")
fruits += ("pear", "kiwi")
print(fruits)