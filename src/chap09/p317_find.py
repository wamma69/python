# 찾기와 바꾸기

s = 'www.naver.co.kr'
print(s.find('.kr'))	#'.kr'의 인엑스를 반환한다.

s = 'Let it be, let it be, let it be'
print(s.rfind('let'))	# 문자열의 끝에서부터 탐색한다.

s = 'www.naver.co.kr'
print(s.count('.'))		# 단어가 등장하는 횟수를 반환한다.

s = 'www.naver.com'
print(s.replace('com', 'co.kr'))	# 하나의 단어를 다른 단어로 교체한다.