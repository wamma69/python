# 정규식을 사용하여 스마트폰 번호 찾기

import re

pattern = r'010-\d\d\d\d-\d\d\d\d'
found = re.search(pattern, '제 휴대폰 번호는 010-1234-5678입니다.')   # 문자열에서 pettern에 해당하는 문자열만 찾아서 found에 반환
print('발견된 휴대폰 번호: ' + found.group())
