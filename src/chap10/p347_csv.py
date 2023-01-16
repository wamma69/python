# CSV 데이터 처리하기

# 1
import csv					# CSV 모듈을 불러온다. 

f = open('weather.csv')		# CSV 파일을 열어서 f에 저장한다. 
data = csv.reader(f)		# reader() 함수를 이용하여 읽는다. 
for row in data:
	print(row)
f.close()


# 2 첫번째 행(데이터 속성 표시)을 제거
import csv					# CSV 모듈을 불러온다. 

f = open('weather.csv')		# CSV 파일을 열어서 f에 저장한다. 
data = csv.reader(f)		# reader() 함수를 이용하여 읽는다. 
header = next(data)			# 헤더를 제거한다. 
for row in data:			# 반복 루프를 사용하여 데이터를 읽는다.
	print(row)
f.close()					# 파일을 닫는다. 


# 서울이 언제 가장 추었는지 조사한다.
import csv

f = open('weather.csv')
data = csv.reader(f)
header = next(data)
temp = 1000
when = ""
for row in data:
    if temp > float(row[3]):
        temp = float(row[3])
        when = row[0]
print(temp, "날짜:", when)
f.close()
