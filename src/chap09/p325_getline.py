# 숫자로 시작하는 줄 찾기

import re
f = open('uscons.txt')
for line in f:    
	line = line.rstrip()    
	if re.search('^[0-9]+', line) :
		print(line)
f.close()
