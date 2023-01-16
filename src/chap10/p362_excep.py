# 예외 처리

# 1. 0으로 나누는 예외 처리
(x,y) = (2,0)
try:
    z = x/y
except ZeroDivisionError:
    print ("0으로 나누는 예외")


# 2
(x,y) = (2,0)
try:
    z = x/y
except ZeroDivisionError as e:  # 시스템이 내보내는 예외 메시지 출력
    print (e)


# 3. 입력 오류를 예외 처리
while True:
    try:
        n = input("숫자를 입력하시오 :  ")
        n = int(n)
        break
    except ValueError:
        print("정수가 아닙니다. 다시 입력하시오. ")
print("정수 입력이 성공하였습니다!")


# 4. 파일 열기에서 예외 처리
try:
	fname = input("파일 이름을 입력하세요: ")
	infile = open(fname, "r")
except IOError:
	print("파일 " + fname + "을 발견할 수 없습니다.")