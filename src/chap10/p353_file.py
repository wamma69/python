import os
arr = os.listdir()

for f in arr:
    if f.endswith(".txt") or f.endswith(".py"):     # 대상 파일을 제한
        infile = open(f, "r", encoding="utf-8")
        linecnt = 0
        for line in infile:
            linecnt += 1            # 줄번호 
            e = line.rstrip()		# 오른쪽 줄바꿈 문자를 없앤다. 
            if "Python" in e:
                print(f, linecnt, ":", e)
        infile.close()


# if os.path.exists("aa.txt"):
#     print("ok")
    
# if os.path.isfile("aa.txt"):
#     print("ok")