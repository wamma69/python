# 사용자의 대답을 변수에 저장한다. 
stadium = input("경기장은 어디입니까?")
winner = input("이긴팀은 어디입니까?")
loser = input("진팀은 어디입니까?")
vip = input("우수선수는 누구입니까?")
score = input("스코어는 몇대몇입니까?")

# 변수와 문자열을 연결하여 기사를 작성한다. 
print("")
print("===========================================")
print(f"오늘 {stadium}에서 야구 경기가 열렸습니다.")
print(f"{winner}와 {loser}는 치열한 공방전을 펼쳤습니다.")
print(f"{vip}이 맹활약을 하였습니다.")
print(f"결국 {winner}가 {loser}를 {score}로 이겼습니다.")
print("===========================================")
