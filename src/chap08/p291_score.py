score_dic = {}

while True:
    name = input("이름 : ")
    score = list(map(int, input("점수: ").split()))  # 공백으로 구분하며 연속 입력
    score_dic[name] = score
    ans = input("다음 입력을 또 있습니까?(y/n)")
    if ans == "n" :
        break

print(score_dic)

for name, score in score_dic.items():
    print(name, "의 평균 성적 = ", sum(score)/len(score))