def display_menu() :    # 메뉴를 화면에 출력한다. 
    print("---------------")
    print("1. 연락처 추가")   
    print("2. 연락처 삭제")   
    print("3. 연락처 검색")   
    print("4. 연락처 출력")   
    print("5. 종료")   
    select = int(input("메뉴 항목을 선택하시오: "))
    return select

def main():
    address_book ={} 				# 공백 딕셔너리를 생성한다. 
    while True :
       user = display_menu()
       if user ==1 :
           name =input("이름: ")
           number =input("전화번호:")
           address_book[name]= number		
       elif user ==2 :
           pass	
       elif user ==3 :
           name =input("이름: ")
           if name in address_book:
               print(name, address_book[name])
           else :
               print("없는 사람")
       elif user ==4 :
           for key in sorted(address_book):	
               print(key,"의 전화번호:", address_book[key])
       else :
           break       

main()