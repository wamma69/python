from cryptography.fernet import Fernet

key = Fernet.generate_key()	# 키 생성

with open('secret.key', 'wb') as keyfile:	# 키를 파일에 저장한다. 
	keyfile.write(key)

with open('secret.key', 'rb') as keyfile:		# 키를 파일에서 읽는다. 
  key = keyfile.read()
  
CryptoObj = Fernet(key)			# 암호화 객체를 생성한다. 
  
with open('test.bin', 'rb') as file:		# 이진 파일을 읽는다.
    content = file.read()
      
encryptText = CryptoObj.encrypt(content)	# 키를 사용하여서 암호화시킨다. 
with open('etest.bin', 'wb') as efile:		# 이진 파일을 쓴다.
    efile.write(encryptText)