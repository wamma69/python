text_data ='Create the highest, grandest vision possible for your life, because you become what you believe'

# text_data = '파이썬은 비교적 최근에 나온 언어이다. 파이썬은 라이브러리가 매우 다양하고 활용도가 높다. 파이썬은 데이터 분석과 AI에 매우 강력한 언어이다.'

word_dic = {}				# 단어들과 출현 횟수를 저장하는 딕셔너리를 생성
for w in text_data.split():		# 텍스트를 단어들로 분리하여 반복한다. 
     if w in word_dic:			# 단어가 이미 딕셔너리에 있으면
         word_dic[w]  += 1  		# 출현 횟수를 1 증가한다. 
     else:				# 처음 나온 단어이면 1로 초기화한다. 
         word_dic[w]   = 1  

for w, count in sorted(word_dic.items()):	# 키와 값을 정렬하여 반복 처리한다. 
     print(w, '의 등장횟수=', count)
