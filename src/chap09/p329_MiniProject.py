quiz = {
    1 : {"question" : "CPU는 무엇의 약자인가?", "answer" : "Central Processing Unit"},
    2 : {"question" : "제일 쉬운 프로그래밍 언어는?", "answer" : "파이썬"},
    3 : {"question" : "교육을 가장 많이 받은 물고기는?", "answer" : "고등어"}
}

def checkAnswer(q, a):
    if quiz[q]['answer'].lower() == a.lower():
        print(f"정답입니다.\n")
        return True
    else:
        print(f"오답입니다.\n")
        return False

score = 0
for  number in quiz:
    print(quiz[number]['question'])
    answer = input("답안을 작성하시오(또는 quit):  ")
    if answer == "quit":
        break
    result = checkAnswer(number, answer)
    if result:
        score += 1

print(f"최종 점수는 {score}\n")