# 1. join()으로 문자열 합치기

s = '-'.join(['apple', 'grape', 'banana'])  #중간에 -으로 결합
print(s)

s = ' '.join(['My', 'name', 'is', 'Kim'])     #중간에 공백으로 결합
print(s)

s = '-'.join('010.1234.5678'.split('.'))    #. 문자 대신에 - 문자 사용
print(s)


# 2. 문자들을 다시 모아서 문자열을 만들 때에서 join() 사용
s = 'hello world'
clist = list(s)
print(clist)
s = ''.join(clist)
print(s)


# 3. split()과 join()을 함께 사용하면 문자열 중에서 필요없는 공백을 제거할 수 있다.
print('Action \n\t speak louder     than words')
s = ' '.join('Action \n\t speak louder     than words'.split())
print(s)