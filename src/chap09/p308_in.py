# 1. in과 not in 연산자

print('Hello' in 'Hello World')

print('WORLD' in 'Hello world')

print('WORLD' not in 'Hello world')


# 2. 문자열 안에 문자열 넣기

# 2-1. + 연산자 사용
name = 'Kim'
age = 21
r = '제 이름은 ' + name + '입니다. 저는 ' + str(age) + '살입니다.'
print(r)

# 2-2. %s 기호 사용
name = 'Kim'
age = 21
r = '제 이름은 %s입니다. 저는 %s살입니다.' % (name, age)
print(r)

# 2-3. f-문자열 사용
name = 'Kim'
age = 21
r = f'제 이름은 {name}입니다. 저는 {age}살입니다.'
print(r)