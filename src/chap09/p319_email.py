# 1. 아이디와 도메인 구분하기

address=input('이메일 주소를 입력하시오: ')
(id, domain) = address.split('@')

print(address)
print('아이디:'+id)
print('도메인:'+domain)


# 2. 문자열의 공통 문자 찾기

s1=input('첫 번째 문자열:')
s2=input('두 번째 문자열:')

list1 = list( set(s1) & set(s2) )		# 세트로 만들고 교집합 연산을 한다. 

print('\n공통적인 글자:', end=' ')
for i in list1:
    print(i, end=' ')
