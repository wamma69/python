# 상속

class Person():
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
    
    def isStudent(self):
        return False
   

class Student(Person):  # 상속
   def __init__(self, name, gpa):
       super().__init__(name)   # 부모 클래스 생성자 호출
       self.gpa = gpa

   def isStudent(self):     # 메소드 오버라이딩
       return True
   
obj1 = Person("Kim")  
print(obj1.getName(), obj1.isStudent())
   
obj2 = Student("Park", 4.3) 
print(obj2.getName(), obj2.isStudent())
