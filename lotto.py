import random, os

lotto = open("lotto.txt", "w")


for i in range(3):
    for j in range(6):
        rand = random.randint(1, 45)
        lotto.write(f"{str(rand)} ")
    lotto.write("\n")

lotto.close()

lotto = open("lotto.txt", "r")

lines = lotto.readlines()

while True:
    num = int(input("몇 번 세트를 출력할까요?(0 : 종료) : "))
    
    if num == 0:
        break
    
    print(lines[num - 1])

lotto.close()
