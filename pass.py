def check_pass(p) :
    len_check = False
    upper_check = False
    lower_check = False 
    digit_check = False   
    le = False
    upper = False
    lower = False
    digit = False       
    
    if len(p) >= 8 :
        len_check = True
        le = True
    for i in p :
        if i.isupper() :
            upper_check = True
            upper = True
    for i in p :
        if i.islower() :
            lower_check = True  
            lower = True        
    for i in p :
        if i.isdigit() :
            digit_check = True 
            digit = True 
            
    if (len_check and upper_check and lower_check and digit_check) :
        return "OK", le, upper, lower, digit
    else :
        return "NO", le, upper, lower, digit
    
x = input("비밀번호 : ")
result, l, u, lo, d = check_pass(x)
if result == "OK" :
    print("비밀번호 사용 가능합니다.")
else :
    print("비밀번호 사용할 수 없습니다")
    if l == False :
        print("길이가 8자 보다 작습니다.")
    if u == False :
        print("대문자가 없습니다.")    
    if lo == False :
        print("소문자가 없습니다.")    
    if d == False :
        print("숫자가 없습니다.")      
