# 특수 메소드
class Circle:
    def __init__(self, r):
        self.radius = r
        
    def __eq__(self, other):
        return self.radius == other.radius
        
c1 = Circle(10)
c2 = Circle(10)
if c1 == c2:    # == 연산자를 이용하여 __eq__() 메소드로 정의된 연산을 수행한다.
    print("원의 반지름은 동일합니다.")


# __str()__ 메소드
class Counter:
    def __init__(self, x) :
        self.count = x
    def increment(self):
        self.count += 1
    def __str__(self):
        msg = "카운트값:"+ str(self.count)
        return msg

a = Counter(100)	
print(a)
