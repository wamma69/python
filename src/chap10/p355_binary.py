# 이진 파일

# 1. 이진 파일에서 바이트 읽기
filename = "cat.jpg"
infile = open(filename, "rb")   #이진파일 읽기
bytesArray = infile.read(8)      #입력파일에서 8바이트 읽기
byte1 = bytesArray[0]       # 첫번째 바이트 꺼내기
infile.close()


# 2. 이진 파일에 바이트 저장하기
filename = "out.aaa"
outfile = open(filename, "wb")
bytesArray = bytes([255, 128, 0, 1])
outfile.write(bytesArray)
outfile.close()


# 3. 이진 파일 복사하기
infile = open("123.png", "rb")
outfile = open("kkk.png", "wb")


# 4. 입력 파일에서 1024 바이트씩 읽어서 출력 파일에 쓴다. 
while True:
    copy_buffer = infile.read(1024)
    if not copy_buffer:
        break
    outfile.write(copy_buffer)

infile.close()
outfile.close()
print(str(infile)+"를 " +str(outfile)+"로 복사하였습니다. ")

