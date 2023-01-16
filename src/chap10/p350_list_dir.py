# 1. 현재 작업 디렉토리
import os

print(os.getcwd())	# 현재 작업 디렉토리를 문자열 형식으로 반환

print(os.getcwdb())		# 바이트 배열 객체로 가져오기


# 2. 디렉토리 변경
os.chdir('C:\\')
print(os.getcwd())


# 3. 디렉토리 안의 파일 나열
# 3-1
s = os.listdir()		# 리스트 형식으로 반환
print(s)

print(os.listdir('C:\\Temp'))	

# 3-2
for filename in os.listdir():	# 하나씩 출력한다.
    print(filename)	# 폴더, 파일 모두 출력한다.

# 3-3    
for filename in os.listdir():    
    if os.path.isfile(filename):	# 파일만 처리
        print(filename)

# 3-4 .jpg 파일만 찾아서 출력
cwd = os.getcwd()
files = os.listdir()
for name in files :
	if os.path.isfile(name) :
		if name.endswith(".jpg") :
			print(name)


# 4. 새 디렉토리 만들기
os.mkdir('test')
print(os.listdir())


# 5. 디렉토리 또는 파일 이름 바꾸기
print(os.listdir())
os.rename('test', 'test2')
print(os.listdir())


# 6. 디렉토리 또는 파일 제거
print(os.listdir())
os.remove('packageTest.java')	# 파일 제거
print(os.listdir())

os.rmdir('test')	# 디렉토리 제거
print(os.listdir())