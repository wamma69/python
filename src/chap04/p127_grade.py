# 성적을 받아서 학점을 결정하는 프로그램

score = 83

# 1
if score >= 90 :
	print("학점 A")
elif score >= 80 :
	print("학점 B")
elif score >= 70 :
	print("학점 C")
elif score >= 60 :
	print("학점 D")
else :
	print("학점 F")

 
# 2. if문에서는 순서가 중요하다. -> 잘못된 결과 !
if score >= 60 :
	print("학점 D")
elif score >= 70 :
	print("학점 C")
elif score >= 80 :
	print("학점 B")
elif score >= 90 :
	print("학점 A")
else :
	print("학점 F")


# 3. 독립적인 if문을 사용한 경우. -> 엉뚱한 결과 !
if score >= 90 :
	print("학점 A")
if score >= 80 :
	print("학점 B")
if score >= 70 :
	print("학점 C")
if score >= 60 :
	print("학점 D")
if score < 60 :
	print("학점 F")