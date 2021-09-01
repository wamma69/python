def getMoneyText(amount):
    # 백자리 구하기
    c = money // 100
    if (c == 1):
        print("일백", end=" ")
    elif (c == 2):
        print("이백", end=" ")
    elif (c == 3):
        print("삼백", end=" ")
    elif (c == 4):
        print("사백", end=" ")
    elif (c == 5):
        print("오백", end=" ")
    elif (c == 6):
        print("육백", end=" ")
    elif (c == 7):
        print("칠백", end=" ")
    elif (c == 8):
        print("팔백", end=" ")
    elif (c == 9):
        print("구백", end=" ")
        
    #십자리 구하기
    a = (money % 100) // 10
    if (a == 1):
        print("일십", end=" ")
    elif (a == 2):
        print("이십", end=" ")
    elif (a == 3):
        print("삼십", end=" ")
    elif (a == 4):
        print("사십", end=" ")
    elif (a == 5):
        print("오십", end=" ")
    elif (a == 6):
        print("육십", end=" ")
    elif (a == 7):
        print("칠십", end=" ")
    elif (a == 8):
        print("팔십", end=" ")
    elif (a == 9):
        print("구십", end=" ")
        
    # 일자리 구하기
    b = money % 10
    if (b == 1):
        print("일원")
    elif (b == 2):
        print("이원")
    elif (b == 3):
        print("삼원")
    elif (b == 4):
        print("사원")
    elif (b == 5):
        print("오원")
    elif (b == 6):
        print("육원")
    elif (b == 7):
        print("칠원")
    elif (b == 8):
        print("팔원")
    elif (b == 9):
        print("구원")
    elif (b == 0):
        print("영원")

#입력받기
money = int(input("숫자를 입력하시오.(세자리)"))
getMoneyText(money)


    
