# 1. 부분 집합 연산
A ={"apple","banana","grape"}
B ={"apple","banana","grape","kiwi"}

if A < B : 			# 또는 A.issubset(B) :
	print("A는 B의 부분 집합입니다.")


# 2. 같은지 검사
A ={"apple","banana","grape"}
B ={"apple","banana","grape","kiwi"}

if A == B : 
	print("A와 B는 같습니다.")
else :
    print("A와 B는 같지 않습니다.")
    

# 3. 교집합, 합집합, 차집합
A ={"apple","banana","grape"}
B ={"apple","banana","kiwi"}

C = A | B     # 또는 C = A.union(B)
print(C)

C = A & B     # 또는 C = A.intersection(B)
print(C)

C = A - B     # 또는 C = A.diffeence(B)
print(C)


# 4. 리스트 <-> 세트
list1 = [1,2,3,4,5,1,2,4]
print(set(list1))
print(len(set(list1)))		# 서로 다른 정수의 갯수를 구할 수 있다.


# 4-1. 두개의 리스트에 공통으로 있는 숫자 찾기
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]
print(set(list1) & set(list2))


# 4-2. (추가) 세트를 정렬하면 결과는 리스트로 바뀐다.
A = {3, 5, 1, 6, 2}
print(sorted(A))