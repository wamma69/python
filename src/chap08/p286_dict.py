# 항목 추가하기

# 1. 가장 간편한 것
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
capitals["France"] = "Paris"
print(capitals)


# 2. 공백 딕셔너리를 생성하고 하나씩 추가해도 된다.
capitals = {}
capitals["Korea"] = "Seoul"
capitals["USA"] = "Wasington"
capitals["UK"] = "London"
capitals["France"] = "Paris"
print(capitals)


# 3. 딕셔너리에 다른 딕셔너리를 추가하려면 update()를 사용
capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
capitals.update({"France":"Paris", "Germany":"Berlin"})
print(capitals)
