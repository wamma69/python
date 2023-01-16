# 파일을 연 후에는 무엇을 하는가?

f = open("test.txt", "r", encoding="utf-8")
s = f.read()
myList = s.split("\n")  # 리스트에 저장된다.
print(myList)
f.close()
