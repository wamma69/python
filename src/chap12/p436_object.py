# 객체 참조

# 1
class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on
        
    def setChanner(self, channel):
        self.channel = channel
       
t = Television(11, 10, True)

# 2
s = t   # 참조값이 복사되어 s에 저장된다. 따라서 s와 t는 동일한 객체를 가르키게 된다.
s.channel = 9

print(s.channel, t.channel) # t의 값도 변경된다.

# 3
if s is t :
    print("2개의 변수는 동일한 객체를 참조하고 있습니다.")
    
if s is not t:
    print("2개의 변수는 다른 객체를 참조하고 있습니다.")
    
    