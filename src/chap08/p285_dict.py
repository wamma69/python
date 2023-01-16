# 항목 탐색하기
 
capitals = { "Korea": "Seoul" , "USA": "Washington", "UK": "London" } 

# 1
print(capitals["Korea"])

# 2
# print(capitals["France"])   #에러 발생

print(capitals.get("France", "해당 키가 없습니다."))   # get()을 쓰면 에러 방지할 수 있다.

# 3
if "France" in capitals :    # 키가 있는지 확인하는 방법
	print( "딕셔너리에 포함됨" )
else: 
	print( "딕셔너리에 포함되지 않음" )

