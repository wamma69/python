# 1. split()으로 문자열 분해하기

s = 'Welcome to Python'
print(s.split())        #공백을 분리자로 지정

s = 'Hello, World!'
print(s.split(','))     #,를 분리자로.
print(s.split(', '))    #공백도 포함해서 분리자로.

print(list('Hello, World!'))    #list()를 사용하면 문자열을 문자들로 분해


# 2. 여러줄로 이루어진 문자열을 한 줄씩 분리
lyric = '''Silent night, holy night
All is calm, all is bright
'Round yon virgin Mother and Child
Holy infant so tender and mild
Sleep in heavenly peace'''
print(lyric.split('\n'))