# 항목 삭제하기

# pop() 메서드 사용
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
city = capitals.pop("UK")
print(capitals)

# 키가 있는지 먼저 검사하면 없는 키 삭제할 때 에러 방지
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
if "UK"in capitals :
	capitals.pop("UK")
print(capitals)
 
# 모두 삭제. clear()
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
capitals.clear()
if len(capitals)==0 :
	print("딕셔너리가 비어 있음")
else:
	print("딕셔너리가 비어 있지 않음")