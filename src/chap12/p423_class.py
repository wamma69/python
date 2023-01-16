# 클래스 작성하기

class Counter:
    def __init__(self) :    # 생성자 정의
        self.count = 0  # 인스턴스 변수 생성

    def increment(self) :   # 메소드 정의
        self.count += 1

a = Counter()

a.increment()   # 객체의 멤버 접근
print("카운트의 값=", a.count) 