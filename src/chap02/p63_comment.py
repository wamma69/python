# 주석
#	이 프로그램은 화씨 온도를 받아서 섭씨 온도로 변환한다.
#
ftemp = 100			 # 화씨 온도 100를 변수에 저장한다.  

ctemp = (ftemp-32.0)*5.0/9.0    # 화씨온도->섭씨온도
print("섭씨온도:", ctemp)        # 섭씨온도를 화면에 출력한다.


# 실행하고 싶지 않은 문장이 있을 때 주석을 이용한다.
x = 100
y = 200
sum = x + y
#diff = x - y
print("합은 ", sum)