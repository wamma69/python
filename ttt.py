# x = input("문자열 입력하세요. ")
x = "jasjs?#$------khkj"

s = {"알파벳_소문자":0, "알파벳_대문자":0, "숫자":0, "공백":0}
t = ["?", "#", "$"]

for i in x:
    if i.isalpha() and i.isupper():
        s["알파벳_대문자"] = s["알파벳_대문자"] + 1
    else:
        if i.isalpha() and i.islower():
            s["알파벳_소문자"] = s["알파벳_소문자"] + 1        
        else :      
            if i.isdigit():
                s["숫자"] = s["숫자"] + 1
            else: 
                if i.isspace():
                    s["공백"] = s["공백"] + 1
                else :
                    if i in t:
                        print("good")
                    else:
                        print("bad")
                        break

print(s)
