import zipfile
         
choice = input("어떤 작업을 하겠습니까?(1-압축 또는 2-해제): ")
if choice == "1":
	fname = input("압축할 파일 이름을 입력하시오: ")
	obj = zipfile.ZipFile('test.zip', 'w')	# 파일 압축
	obj.write(fname)
	obj.close()
elif choice == "2":
	fname = input("압축을 풀 파일 이름을 입력하시오: ")	# 압축 풀기
	obj = zipfile.ZipFile(fname, 'r')
	obj.extract("test.txt")
	obj.close()