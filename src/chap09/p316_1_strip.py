# strip()으로 공백 문자 제거하기

# 1
s = '   Hello, World!   '
print(s)
s = s.strip()   #왼쪽, 오른쪽 양쪽에서 공백 문자 제거
print(s)


# 2
s = '###$$$this is exampe$$$###'

print(s.strip('#$'))    # 특정문자 삭제

print(s.lstrip('#'))    # 왼쪽 문자만 삭제

print(s.rstrip('#'))    # 오른쪽 문자만 삭제
