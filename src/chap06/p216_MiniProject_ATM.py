import sys
pin=1234
balance=0

def widthdraw():
    global balance
    amount = int(input("금액을 입력하시오: "))
    if amount > balance:
        print("잔액이 없음")
    else:
        balance = balance - amount
    print(f"잔액은 {balance}입니다.")

def deposit():
    global balance
    amount = int(input("금액을 입력하시오: "))
    balance = balance + amount
    print(f"잔액은 {balance}입니다.")

def get_balance():
    global balance
    print(f"잔액은 {balance}입니다.")


userpin = int(input('핀번호를 입력하시오: '))

if pin != userpin:
    print("잘못된 핀번호")
    sys.exit()
while True:
    query = int(input('1 - 잔액 보기	2- 인출	3- 저금	4- 종료 '))
    if query == 1:
        get_balance()
    elif query == 2:
        widthdraw()
    elif query == 3:
        deposit()
    elif query == 4:
        sys.exit()