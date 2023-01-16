# 변수의 범위

# 1. 지역변수
def func():
  x = 100
  print(x)

func()
# print(x)  # Error

# 2. 전역변수
gx = 100

def func1():
  print(gx)		# 전역 변수 사용 가능

def func2():
  print(gx)		# 전역 변수 사용 가능

func1()
func2()

# 3. 함수 안에서 전역 변수 변경하기
# 3-1
gx = 100

def myfunc1() :
    print("func1() :", gx)

def myfunc2() :
    gx = 200			# 여기서 지역 변수 gx가 생성된다. 
    print("func2() :", gx)	# 지역 변수 gx를 사용한다. 

myfunc1()
myfunc2()
print("외부: ", gx)

# 3-2
gx = 100

def myfunc1() :
    print("func1() :", gx)

def myfunc2() :
    global gx			# 전역 변수 gx를 사용하겠음
    gx = 200			# 전역 변수 gx가 200으로 변경
    print("func2() :", gx)

myfunc1()
myfunc2()
print("외부: ", gx)