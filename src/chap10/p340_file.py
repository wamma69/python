# 1. 파일에 쓰기
f = open("test.txt", "w")
f.write("파이썬은 강력합니다.\n")
f.close()


# 2. 파일에서 읽기
f = open("test.txt", "r")
s = f.read()
print(s)
f.close()


# 3. 파일에 추가하기
f = open("test.txt", "a")
f.write("파이썬은 간결합니다.\n")
f.close()
f = open("test.txt", "r")
s = f.read()
print(s)
f.close()


# 4. with 문으로 파일 열기
with open("test.txt", "w") as f:
    f.write("파이썬은 간결합니다.\n")
    
    # f.close()를 호출하지 않아도 된다.
